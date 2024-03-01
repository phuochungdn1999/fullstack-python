from monitor.services import MonitorService, UploadService, CommandService
from monitor_proto import monitor_pb2_grpc
from upload_proto import upload_pb2_grpc
from command_proto import command_pb2_grpc


def grpc_handlers(server):
    monitor_pb2_grpc.add_MonitorControllerServicer_to_server(MonitorService.as_servicer(), server)
    upload_pb2_grpc.add_UploadServiceServicer_to_server(UploadService(), server)
    command_pb2_grpc.add_CommandControllerServicer_to_server(CommandService.as_servicer(), server)
    
    
