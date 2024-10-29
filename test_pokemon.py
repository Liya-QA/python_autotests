import requests
import pytest

url = 'https://api.pokemonbattle.ru/v2'
token = '2eb381c48b291478d1f68dc764bc4c25'
header = {'Content-Type': 'application/json', 'trainer_token': token}
trainer_id = '7146'


def test_status_code():
    response = requests.get(url = f'{url}/trainers', params = {'trainer_id' : trainer_id})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{url}/trainers', params = {'trainer_id' : trainer_id})
    assert response_get.json()["data"][0]["trainer_name"] == 'Лилу'