import requests


class TestDeleteSuperhero:

    def test_delete_superhero(self):

        ids = 13

        response = requests.delete(f"https://superhero.qa-test.csssr.com/superheroes/{ids}")

        assert response.status_code == 200, \
            f"Expected status code: 200. Actual status code is {response.status_code}"

        response2 = requests.get(f"https://superhero.qa-test.csssr.com/superheroes/{ids}")

        assert response2.status_code == 400, \
            f"Expected status code: 400. Actual status code is {response.status_code}"

        response2_as_dict = response2.json()

        assert 'message' in response2_as_dict
        assert response2_as_dict['message'] == f"Superhero with id '{ids}' was not found"

        assert 'code' in response2_as_dict
        assert response2_as_dict['code'] == 'NOT_FOUND'
