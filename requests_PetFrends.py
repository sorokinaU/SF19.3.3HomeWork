import requests

#метод get
url = 'https://petfriends.skillfactory.ru/api/key'
headers = {
    'auth_key': '5737ede0a835f93247d2afac1ec96074226bef7b18cf4b149ad58f98',
}

headers = {
    'email': 'corokina@inbox.ru',
    'password': '77777776'
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())


#метод post
status = 'available'

url = 'https://petfriends.skillfactory.ru/api/create_pet_simple'
headers = {
    'auth_key': '5737ede0a835f93247d2afac1ec96074226bef7b18cf4b149ad58f98',
}

data = {
    'name': 'Тоша',
    'animal_type': 'Кот',
    'age': '11'
}


response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())


#метод delete

url = 'https://petfriends.skillfactory.ru/api/pets/f5a4ef74-583c-490f-8628-27a52b41a410'

headers = {
    'auth_key': '5737ede0a835f93247d2afac1ec96074226bef7b18cf4b149ad58f98'
}

response = requests.delete(url, headers=headers)


print(response.status_code)
print(response.json())

#метод put

status = 'available'

url = 'https://petfriends.skillfactory.ru/api/pets/f4859cbd-4105-41b9-9162-db2940326cc8'
headers = {
    'auth_key': '5737ede0a835f93247d2afac1ec96074226bef7b18cf4b149ad58f98',
}

data = {
    'name': 'Кыся',
    'animal_type': 'кошка',
    'age': '5'
}


response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
