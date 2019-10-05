install:
	pipenv install --dev --python=3.7.4


compile:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. square.proto
