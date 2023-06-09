import requests
import json


class TestCreateSuperhero:

    def test_create_superhero(self):

        data = {
            "fullName": "Dr Pepper",
            "birthDate": "2020-02-22",
            "city": "New York",
            "mainSkill": "Soda",
            "gender": "M",
            "phone": "+79456675588"
        }
        data_as_json = json.dumps(data)

        response = requests.post('https://superhero.qa-test.csssr.com/superheroes', data=data_as_json,
                                 headers={"Content-Type": "application/json" })

        assert response.status_code == 200, \
            f"Expected status code: 200. Actual status code is {response.status_code}"

        response_as_dict = response.json()

        assert 'id' in response_as_dict

        assert 'fullName' in response_as_dict
        assert response_as_dict['fullName'] == data['fullName']

        assert 'birthDate' in response_as_dict
        assert response_as_dict['birthDate'] == data['birthDate']

        assert 'city' in response_as_dict
        assert response_as_dict['city'] == data['city']

        assert 'mainSkill' in response_as_dict
        assert response_as_dict['mainSkill'] == data['mainSkill']

        assert 'gender' in response_as_dict
        assert response_as_dict['gender'] == data['gender']

        assert 'phone' in response_as_dict
        assert response_as_dict['phone'] == data['phone']

    def test_create_superhero_only_with_mainskill(self):

        data = {
            "mainSkill": "Thunder"
        }
        data_as_json = json.dumps(data)

        response = requests.post('https://superhero.qa-test.csssr.com/superheroes', data=data_as_json,
                                 headers={"Content-Type": "application/json" })

        assert response.status_code == 403, \
            f"Expected status code: 403. Actual status code is {response.status_code}"

        response_as_dict = response.json()

        assert 'message' in response_as_dict
        assert response_as_dict['message'] == 'Incorrect request data'

        assert 'code' in response_as_dict
        assert response_as_dict['code'] == 'BAD_REQUEST'

    def test_create_superhero_without_mainskill(self):

        data = {
            "fullName": "Thor",
            "birthDate": "2020-02-22",
            "city": "New York",
            "gender": "M",
            "phone": "+79456675588"
        }
        data_as_json = json.dumps(data)

        response = requests.post('https://superhero.qa-test.csssr.com/superheroes', data=data_as_json,
                                 headers={"Content-Type": "application/json" })

        assert response.status_code == 403, \
            f"Expected status code: 403. Actual status code is {response.status_code}"

        response_as_dict = response.json()

        assert 'message' in response_as_dict
        assert response_as_dict['message'] == 'Incorrect request data'

        assert 'code' in response_as_dict
        assert response_as_dict['code'] == 'BAD_REQUEST'
