import requests 
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def _init_(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API to custom auth header."""
        r.headers['X-TokenAuth'] = f'{self.token}' #Python 3.6+
        return r

response = requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token')) #doesn't work
print(response)