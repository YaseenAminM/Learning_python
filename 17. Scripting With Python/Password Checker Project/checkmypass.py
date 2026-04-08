import requests
import hashlib

h = hashlib.sha1(b"password123")

url = 'https://api.pwnedpasswords.com/range/' + h.hexdigest()

res = requests.get(url)

print(res)
