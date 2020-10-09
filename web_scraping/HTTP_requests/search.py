import requests

# Search Github's repositories
response = requests.get(
    'https://api.github.com/search/repositories',
    #params={'q': 'requests+language:python'},
    params={'q': 'schedule+user:dbader'}
)

# Inspect some attributes of the repository
json_response = response.json()
repository = json_response['items'][0] #are you feeling lucky?
print(f'Repository name: {repository["name"]}') # Python 3.6+
print(f'Repository description: {repository["description"]}')