# sample_calc_grpc_py

Instructions:
1. Install gRpc $ python3 -m pip install grpcio
2. Install gRpc tools $ python3 -m pip install grpcio-tools googleapis-common-protos
3. Generate skeleton and stub from proto file $ python3 -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. proto/calculator.proto
4. Run server $ python3 calculator_server.py
5. Run client $ python3 calculator_client.py

Ref: 
1. https://grpc.io/docs/quickstart/python.html#install-grpc-tools
2. https://github.com/grpc/grpc/tree/master/examples/python/helloworld
