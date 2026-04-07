import requests


url = 'https://api.pwnedpasswords.com/range/' + "_password123_"

res = requests.get(url)

print(res)
