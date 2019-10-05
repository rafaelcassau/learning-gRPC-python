import time
import grpc
from concurrent import futures


import square_pb2
import square_pb2_grpc


import square


class SquareServicer(square_pb2_grpc.SquareServicer):

    def SquareRoot(self, request, context):
        response = square_pb2.Number()
        response.value = square.square_root(request.value)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

square_pb2_grpc.add_SquareServicer_to_server(SquareServicer(), server)


print("Starting server, Listening on port 50051.")
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
        server.stop(0)

