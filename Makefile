install:
	pipenv install --dev --python=3.7.4


compile-calculator:
	cd calculator && python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. square.proto


compile-unary-digestor:
	cd digestor && python -m grpc_tools.protoc --proto_path=. ./digestor.proto --python_out=. --grpc_python_out=.
