import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from monitor.models import Monitor
from monitor.serializers import MonitorProtoSerializer, PredictResponseSerializer
from upload_proto import upload_pb2, upload_pb2_grpc
from concurrent import futures
from django.utils import timezone
from oauth2_provider.models import AccessToken
from grpc import StatusCode
import random
from command_proto import command_pb2


class MonitorService(Service):
    def get_token_from_header(self, header):
        token_type, _, token = header.partition(' ')
        if token_type.lower() != 'bearer':
            raise ValueError('Invalid authorization header')
        return token

    def validate_token(self, token):
        if not AccessToken.objects.filter(token=token, expires__gt=timezone.now()).exists():
            raise ValueError('Invalid token')

    def validate(self, request, context):
        metadata = dict(context.invocation_metadata())
        authorization = metadata.get('authorization')

        if not authorization:
            context.abort(StatusCode.UNAUTHENTICATED, 'Missing authorization header')

        try:
            token = self.get_token_from_header(authorization)
            self.validate_token(token)
        except ValueError as e:
            context.abort(StatusCode.UNAUTHENTICATED, str(e))
 
    def List(self, request, context):
        self.validate(request, context)
        posts = Monitor.objects.all()
        serializer = MonitorProtoSerializer(posts, many=True)
        for msg in serializer.message:
            yield msg

    def Create(self, request, context):
        self.validate(request, context)
        serializer = MonitorProtoSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def get_object(self, pk):
        self.validate(request, context)
        try:
            return Monitor.objects.get(pk=pk)
        except Monitor.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND, 'Monitor:%s not found!' % pk)

    def Retrieve(self, request, context):
        self.validate(request, context)
        post = self.get_object(request.id)
        serializer = MonitorProtoSerializer(post)
        return serializer.message

    def Update(self, request, context):
        post = self.get_object(request.id)
        serializer = MonitorProtoSerializer(post, message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def Destroy(self, request, context):
        post = self.get_object(request.id)
        post.delete()
        return empty_pb2.Empty()

class UploadService(upload_pb2_grpc.UploadServiceServicer):
    def UploadFiles(self, request, context):
        for file in request.files:
            with open('./upload_file/' + file.filename, 'wb') as f:
                f.write(file.data)
        return upload_pb2.UploadResponse(success=True)
    
class CommandService(Service):
    def Predict(self, request, context):
        lucky_number = random.randint(0, 2147483647)
        return command_pb2.PredictResponse(lucky_number=lucky_number)

    def Logs(self, request, context):
        return command_pb2.LogResponse(log='This is log')
