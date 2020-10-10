import requests

# Search Github's repositories
response = requests.get(
    'https://api.github.com/search/repositories',
    #params={'q': 'requests+language:python'},
    params={'q': 'HTTP for Humans+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

# View the new 'text-matches array which provides information about
# your search terms within the results


# Inspect some attributes of the repository
json_response = response.json()
repository = json_response['items'][0] #are you feeling lucky?
# print(f'Repository name: {repository["name"]}') # Python 3.6+
# print(f'Repository description: {repository["description"]}')
print(f'Text matches: {repository["text_matches"]}')