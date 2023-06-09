import requests
import json


class TestUpdateSuperhero:

    def test_update_superhero(self):

        data = {
            "id": 1,
            "fullName": "Dr Pepper New",
            "birthDate": "2020-02-22",
            "city": "Moscow",
            "mainSkill": "Soda",
            "gender": "M",
            "phone": None}

        data_as_json = json.dumps(data)

        response = requests.put('https://superhero.qa-test.csssr.com/superheroes/1', data=data_as_json,
                                headers={"Content-Type": "application/json" })

        assert response.status_code == 200, \
            f"Expected status code: 200. Actual status code is {response.status_code}"

        response2 = requests.get(f"https://superhero.qa-test.csssr.com/superheroes/1")

        response_as_dict = response2.json()

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
