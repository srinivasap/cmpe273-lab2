import grpc

import calculator_pb2
import calculator_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.AddNumbers(calculator_pb2.AddRequest(num1=1, num2=1))
    print("Calculator add result: " + str(response.result))


if __name__ == '__main__':
    run()