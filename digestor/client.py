import grpc
import digestor_pb2
import digestor_pb2_grpc


class DigestorClient:
    """
    Client for acessing the gRPC funcionality
    """
    def __init__(self):
        self.host = "localhost"
        self.port = 46001
        
        # instantiate a communication channel
        self.channel = grpc.insecure_channel(f"{self.host}:{self.port}")

        # bind the client to the server channel
        self.stub = digestor_pb2_grpc.DigestorStub(self.channel)

    def get_digest(self, message):
        """
        Client function to call the rpc for GetDigest 
        """
        to_digest_message_request = digestor_pb2.DigestMessage(ToDigest=message)

        response = self.stub.GetDigestor(to_digest_message_request)
        return response


digestor_client = DigestorClient()

digestor_client.get_digest("Rafael Cassau")
digestor_client.get_digest("gRPC is a greather choice than REST to internal communication between microservices")

