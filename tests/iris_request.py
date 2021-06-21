import requests
import numpy as np

model_name = "iris-deploy-test"
service_hostname = "iris-deploy-test.jupyterhub.example.com"
ingress_ip = "10.0.11.211"
ingress_port = "31988"

x_0 = np.array([[6.8, 2.8, 4.8, 1.4]])
inference_request = {
    "inputs": [
        {
          "name": "predict",
          "shape": x_0.shape,
          "datatype": "FP32",
          "data": x_0.tolist()
        }
    ]
}

request_headers = {
    "Content-Type": "aplication/json",
    "Accept": "application/json",
    "Host": service_hostname
}
endpoint = f"http://{ingress_ip}:{ingress_port}/v2/models/{model_name}/infer"
response = requests.post(endpoint, headers=request_headers, json=inference_request)
print(response)

print(response.json())
