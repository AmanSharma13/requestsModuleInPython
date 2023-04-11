import requests

r = requests.get('https://api.github.com/users/AmanSharma13')
print(r.status_code)

print(r.headers['content-type'])
# 'application/json; charset=utf8'
print(r.encoding)
'utf-8'
print(r.text)
# '{"type":"User"...'
r.json()
# {'private_gists': 419, 'total_private_repos': 77, ...}