import requests

endpoint = "http://localhost:8000/api/"

r = requests.post(endpoint, json={"product_id": "1"})
print(r.json())
#print(r.status_code)
#print(r.text)
