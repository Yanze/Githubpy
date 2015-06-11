import requests

user_answer = input("Enter user name:")
response = requests.get('https://api.github.com/users/{}'.format(user_answer))

user_json = response.json()
print('Your user name is {}'.format(user_json['name']))
