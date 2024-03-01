from django_grpc_framework import proto_serializers
from monitor.models import Monitor
from monitor_proto import monitor_pb2
from command_proto import command_pb2
from rest_framework import serializers


class MonitorProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Monitor
        proto_class = monitor_pb2.Monitor
        fields = ['id', 'name', 'status', 'cpu_utilization', 'training_process', 'error_log']
        

class PredictResponseSerializer(serializers.Serializer):
    lucky_number = serializers.IntegerField()