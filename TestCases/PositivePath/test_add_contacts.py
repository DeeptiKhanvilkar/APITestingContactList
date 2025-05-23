import jsonschema

from Utilities.ConfigReader import read_config
from Utilities.ReadExcel import get_cell_data
from Utilities.ReadJson import get_add_contacts_payload, read_json_file
from Utilities.apiUtils import postAPIData, postAPIData_withToken
from schemas.add_contacts_schema import add_contacts_schema


class TestAddContacts:

    def test_add_contacts(self):
        baseurl = read_config("baseUrl", "url")
        sheetname = "add_contacts_valid"
        row = 3
        valid_json_file = '../../TestData/validLogin.json'
        payload = read_json_file(valid_json_file)
        login_endpoint = read_config("endpoints", "login")
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]
        add_contacts_endpoint = read_config("endpoints","contacts")
        print(get_add_contacts_payload(sheetname, row))
        add_contacts_response = postAPIData_withToken(baseurl, add_contacts_endpoint,
                                            get_add_contacts_payload(sheetname, row), token)
        response_data = add_contacts_response.json()
        print(response_data)
        assert add_contacts_response.status_code == 201
        assert add_contacts_response.elapsed.total_seconds() <= 500
        id = response_data["_id"]  # 6821138fdf49e700157f1274   68211566b8b48600157dd24d 682115acb8b48600157dd24f
        print(id)
        assert response_data["firstName"] == get_cell_data(sheetname,row,1)
        assert response_data["lastName"] == get_cell_data(sheetname,row,2)
        assert response_data["birthdate"] == get_cell_data(sheetname,row,3)
        assert response_data["email"] == get_cell_data(sheetname,row,4)
        assert response_data["phone"] == str((get_cell_data(sheetname,row,5)))
        assert response_data["street1"] == get_cell_data(sheetname,row,6)
        assert response_data["street2"] == get_cell_data(sheetname,row,7)
        assert response_data["city"] == get_cell_data(sheetname,row,8)
        assert response_data["stateProvince"] == get_cell_data(sheetname,row,9)
        assert response_data["postalCode"] == str((get_cell_data(sheetname,row,10)))
        assert response_data["country"] == get_cell_data(sheetname,row,11)
        jsonschema.validate(response_data, schema=add_contacts_schema)


