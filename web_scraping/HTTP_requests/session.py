import requests
from getpass import getpass

from requests.sessions import session

# By using context manager, you can use the statment "with"
# so that the resources used by the session will be released after use
with requests.Session() as session:
    session.auth = ('soulyana', getpass())

    # Instead of requests.get(), you'll use session.get()
    response = session.get('https://api.github.com/user')
    response2 = session.get('https://api.github.com/user/repos')

# You can inspect the response just like before
print(response.headers)
# print(response.json())
print('This is my first repo!')
print(response2.json()[0]['url']) # results in key error 