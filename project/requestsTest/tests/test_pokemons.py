import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '64f01f1577d779ae358906ff3a13ccd3'
HEADER = {'Content_Type' : 'application/json', 'trainer_token':TOKEN }
TRAINER_ID = '11012'
NAME = 'Averich'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

