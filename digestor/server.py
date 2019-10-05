import grpc
import time
import hashlib
import digestor_pb2
import digestor_pb2_grpc
from concurrent import futures


class DigestorServicer(digestor_pb2_grpc.DigestorServicer):
    """
    gRPC server for Digestor Service
    """
    def __init__(self, *args, **kwargs):
        self.server_port = 46001

    def GetDigestor(self, request, context):
        """
        Implementation of the rpc GetDigestor declared in the proto file
        """

        hasher = hashlib.sha256()
        hasher.update(request.ToDigest.encode())
        digested = hasher.hexdigest()
        
        print(digested)

        result = {
            "Digested": digested,
            "WasDigested": True
        }
        return digestor_pb2.DigestedMessage(**result)

    def start_server(self):
        """
        Function which actually starts the gRPC server, and preps it for
        serving incoming connections
        """
        digestor_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        # attach this server object into gRPC server
        digestor_pb2_grpc.add_DigestorServicer_to_server(self, digestor_server)
        
        digestor_server.add_insecure_port(f"[::]:{self.server_port}")
        digestor_server.start()

        print(f"Digestor server running on port {self.server_port}")

        try:
            while True:
                time.sleep(60*60*60)
        except KeyboardInterrupt:
            digestor_server.stop(0)
            print("Digestor server stopped")


current_server = DigestorServicer()
current_server.start_server()
