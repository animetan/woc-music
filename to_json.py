import json

ar = []

with open("cenz.txt", encoding="uft-8") as r:
  for i in r:
    n = i.lower().split('\n')[0]
    if n !='':
    ar.append(n)


with open('cenz.json', 'w', encoding="uft-8") as e:
  json.dump(ar, e)