import requests

url = 'https://detik.com'
try:
    response = requests.get('%s' % url)
    print(f'success! Request Code = {response.status_code}')
    print(f'Content {response.text}')
except Exception as e:
    print('There is an error', e)
print('Program Ended')