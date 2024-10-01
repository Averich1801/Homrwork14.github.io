import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '64f01f1577d779ae358906ff3a13ccd3'
HEADER = {'Content_Type' : 'application/json', 'trainer_token':TOKEN }
TRAINER_ID = '11012'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_status_code():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Averich'

@pytest.mark.parametrize('key, value', [('trainer_name', 'Averich'),('id', f'{TRAINER_ID}')])
def test_parametrize(key,value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value
