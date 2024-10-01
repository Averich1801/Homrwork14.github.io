import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '64f01f1577d779ae358906ff3a13ccd3'
HEADER = {'Content_Type' : 'application_json', 'trainer_token':TOKEN }
body_registration = {
    "trainer_token": TOKEN,
    "email": "nepuking@yandex.ru",
    "password": "Fregile1801"
}
body_conformation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_rename = {

    "pokemon_id": '76918',
    "name": "Барабара",
    "photo_id": 2
}
body_pokeball = {
    "pokemon_id": '76918',
}
'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''pokemon_id = response_create.json()['id']
print(pokemon_id)'''

'''response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)

