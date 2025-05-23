import json
import jsonschema
import pytest
import requests
from Utilities.ReadExcel import get_cell_data
from Utilities.ConfigReader import read_config
from Utilities.ReadJson import read_json_file
from Utilities.apiUtils import postAPIData
from schemas.login_schema import login_schema
from TestData import *


class TestLogin:
    baseurl = read_config("baseUrl", "url")
    endpoint = read_config("endpoints", "login")

    # @pytest.mark.skip
    def test_verify_login(self):
        valid_json_file = '../TestData/validLogin.json'
        payload = read_json_file(valid_json_file)
        response = postAPIData(self.baseurl, self.endpoint, payload)
        assert response.status_code == 200
        assert response.elapsed.total_seconds() <= 500
        response_data = response.json()
        json_data = json.dumps(response_data, indent=4)
        print(json_data)
        # assert response_data["user"]["email"] == get_cell_data("Login", 2,1)
        assert response_data['user']['email'] == payload["email"]
        # print(response_data["token"])
        jsonschema.validate(response_data, schema= login_schema)
        # 660296f0639ed8001378a9ac

