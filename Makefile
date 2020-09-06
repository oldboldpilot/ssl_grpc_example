stubs:
	python -m grpc.tools.protoc -I/usr/local/include -I. --python_out=./ --grpc_python_out=./ service.proto

client:
	python client.py

server:
	python server.py

gen_key:
	 mkcert -key-file key.pem -cert-file cert.pem localhost
