import argparse
import json

import grpc
import inference_pb2
import inference_pb2_grpc

parser = argparse.ArgumentParser(prog='QA bot')
parser.add_argument(
    '--grpc-server', default='localhost:7070', dest='grpc_server')
parser.add_argument(
    '--model-name', default='my_tc', dest='model_name')
args = parser.parse_args()


def get_inference_stub():
    channel = grpc.insecure_channel(args.grpc_server)
    stub = inference_pb2_grpc.InferenceAPIsServiceStub(channel)
    return stub


while True:
    print("Question: ", end=" ")
    stub = get_inference_stub()
    s = input()
    input_data = {"data": json.dumps(
        {"question": s, "context": ""}, ensure_ascii=False).encode()}

    try:
        response = stub.Predictions(
            inference_pb2.PredictionsRequest(
                model_name=args.model_name, input=input_data)
        )
        prediction = response.prediction.decode("utf-8")
        print("Answer: " + prediction)
    except grpc.RpcError as e:
        print(e)
