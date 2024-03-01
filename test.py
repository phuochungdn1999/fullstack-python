import grpc
from upload_proto import upload_pb2, upload_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')

    stub = upload_pb2_grpc.UploadServiceStub(channel)

    files = []
    for filename in ['views.py', 'urls.py', 'models.py']:
        with open('./blog/' + filename, 'rb') as f:
            chunk = f.read()
        files.append(upload_pb2.File(filename=filename, data=chunk))
    request = upload_pb2.UploadRequest(files=files)

    response = stub.UploadFiles(request)

    print("UploadFile response: ", response)

if __name__ == '__main__':
    run()