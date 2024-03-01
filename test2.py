import requests

data = {
    'grant_type': 'password',
    'username': 'admin',
    'password': 'pass',
}
auth = ('q2bpM21XRSIDCnQQLgxl3Og6x64T2WylNKtqzlpd', '8c9oQUJW28xnAufsGdQWDnADOYnOTRmK7jnX8dINxhnvyofFI2YkAbTOihmNjUi71lz4LGGELDzpI9yzIjyXwasfEPgFa5bt82BAEualaBFSzEL3jIi04eB0eZMrcEyC')

response = requests.post('http://localhost:8080/o/token/', data=data, auth=auth)

token = response.json()
print(token)