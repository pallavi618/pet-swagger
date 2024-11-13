import requests
import json

def fetch_endpoints(https://petstore.swagger.io/v2/swagger.json):
    response = requests.get(https://petstore.swagger.io/v2/swagger.json)
    if response.status_code == 200:
        swagger_data = response.json()
        endpoints = swagger_data.get("paths", {}).keys()
        return list(endpoints)
    else:
        print("Failed to fetch Swagger JSON.")
        return []

if __name__ == "__main__":
    swagger_url = "http://petstore.swagger.io/v2/swagger.json"
    endpoints = fetch_endpoints(swagger_url)
    print("Endpoints available in Swagger JSON:")
    for endpoint in endpoints:
        print(endpoint)

