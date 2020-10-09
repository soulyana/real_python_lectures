import requests
from requests.exceptions import HTTPError

#response = requests.get(url)

#if response.status_code == 200:
#    print('Success!') #shorthand that it was succesful not that you got conent back
#elif response.status_code == 404:
#    print('Not found.')
#else:
#    print('An error has occured')

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # if the response was successful, no Exxception will be raise
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}') #python 3.6
    except Exception as err: 
        print(f'Other error occurred: {err}')
    else:
        print('Success!')