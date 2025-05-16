import jsonschema

from Utilities.ConfigReader import read_config
from Utilities.ReadExcel import get_cell_data
from Utilities.ReadJson import *
# from Utilities.ReadJson import get_add_contacts_payload, read_json_file,  \
#     get_add_contacts_payload_missing_firstname, get_add_contacts_payload_missing_lastname, \
#     get_add_contacts_payload_missing_birthdate, get_add_contacts_payload_missing_email, \
#     get_add_contacts_payload_missing_phone, get_add_contacts_payload_missing_street1, \
#     get_add_contacts_payload_missing_street2, get_add_contacts_payload_missing_city, \
#     get_add_contacts_payload_missing_stateProvince, get_add_contacts_payload_missing_postalCode, \
#     get_add_contacts_payload_missing_country
from Utilities.apiUtils import postAPIData, postAPIData_withToken
from schemas.add_contacts_schema import add_contacts_schema


class TestAddContacts:

    def test_add_contacts_missing_info(self):
        baseurl = read_config("baseUrl", "url")
        sheetname = "add_contacts_valid"
        row = 2
        valid_json_file = '../TestData/validLogin.json'
        payload = read_json_file(valid_json_file)
        login_endpoint = read_config("endpoints", "login")
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]
        add_contacts_endpoint = read_config("endpoints","contacts")
        print(get_add_contacts_payload(sheetname, row))
        for i in range(0,2):
            if i == 0:
                add_contacts_response = postAPIData_withToken(baseurl, add_contacts_endpoint,
                                                    get_add_contacts_payload_missing_firstname(sheetname, row), token)
                response_data = add_contacts_response.json()
            elif i == 1:
                add_contacts_response = postAPIData_withToken(baseurl, add_contacts_endpoint,
                                                              get_add_contacts_payload_missing_lastname(sheetname,
                                                                                                         row), token)
                response_data = add_contacts_response.json()
            print(response_data["message"])
            assert add_contacts_response.status_code == 400
            assert add_contacts_response.elapsed.total_seconds() <= 500
            assert response_data["_message"] == "Contact validation failed"
            # assert response_data["message"] == "Contact validation failed: firstName: Path `firstName` is required."


