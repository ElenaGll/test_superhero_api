import requests
import pytest


class TestGetSuperheroes:

    def test_get_all_superheroes(self):

        response = requests.get('https://superhero.qa-test.csssr.com/superheroes')

        assert response.status_code == 200, \
            f"Expected status code: 200. Actual status code is {response.status_code}"

    @pytest.mark.parametrize('ids', [1, 3, 5])
    def test_get_superhero_by_id(self, ids):

        response = requests.get(f"https://superhero.qa-test.csssr.com/superheroes/{ids}")

        assert response.status_code == 200, \
            f"Expected status code: 200. Actual status code is {response.status_code}"

        response_as_dict = response.json()

        assert 'id' in response_as_dict
        assert response_as_dict['id'] == ids

        assert 'fullName' in response_as_dict
        assert 'birthDate' in response_as_dict
        assert 'city' in response_as_dict
        assert 'mainSkill' in response_as_dict
        assert 'gender' in response_as_dict
        assert 'phone' in response_as_dict
