import requests

response = requests.post('http://localhost:5000/user/add', json={'name': 'bob', 'password': 'woirdshfsdf', 'email': 'aklshdou@gemashdf'})
print(response.status_code, response.content)