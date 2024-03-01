import requests

data = {
    'grant_type': 'password',
    'username': 'admin',
    'password': 'pass',
}
auth = ('v6mLpeV040t3NaasxdM30yBeYVaqeqRieamvPMah', '9DlALUa5jOfLPpzNjgXFFyzsC95NWafOQufrkPttVLRzTEzAO30tHoHpXTZQ7vmemWKbidxYHNRIO4GpcLd3R5dCSJYHt9DVGYXbkLfiM5DyIkYHDNrewaGNamkDz3ch')

response = requests.post('http://localhost:8080/o/token/', data=data, auth=auth)

token = response.json()
print(token)