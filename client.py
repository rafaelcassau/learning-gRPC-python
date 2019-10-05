import grpc

import square_pb2
import square_pb2_grpc


# open a gRPC channel
channel = grpc.insecure_channel("localhost:50051")

# create a stub (client)
stub = square_pb2_grpc.SquareStub(channel)

# create a valid request message
number = square_pb2.Number(value=16)

# make the call
response = stub.SquareRoot(number)
print(response)

