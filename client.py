import grpc

import service_pb2
import service_pb2_grpc


def main():
    host = 'localhost'
    port = 1337

    with open('rootCA.pem', 'rb') as f:
        trusted_certs = f.read()

    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    channel = grpc.secure_channel('{}:{}'.format(host, port), credentials)

    stub = service_pb2_grpc.ServerStub(channel)
    stub.Foo(service_pb2.Empty())

if __name__ == '__main__':
    main()
