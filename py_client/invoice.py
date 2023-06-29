import requests

url = 'http://localhost:8000/authentication/login'
jwt_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3ODUwNjMzLCJpYXQiOjE2ODc4NTAzMzMsImp0aSI6IjRiM2Q3MWRhMTk0MzRhNTRhMjFiNDhhZTkyZDcxNzgwIiwidXNlcl9pZCI6MX0.Eoqi0odINYeEuEYcyFgklnAcxaNBYduDSEmr4KTYz_w'

headers = {
    'Authorization': f'Bearer {jwt_token}',
}
print(headers)
response = requests.get(url, headers=headers)
