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


class TestAddContactsInvalid:
    sheetname = "add_contacts_invalid_postalcode"
    valid_json_file = '../TestData/validLogin.json'


    def test_add_contacts_empty_postal(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        add_contacts_endpoint = read_config("endpoints", "contacts")
        # Entering empty string
        row = 2
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = postAPIData_withToken(baseurl, add_contacts_endpoint,
                                            get_add_contacts_payload(self.sheetname, row), token)
        response_data = add_contacts_response.json()

        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Contact validation failed"
        assert response_data["message"] ==  "Contact validation failed: postalCode: Expected a string but received a null"


    def test_add_contacts_with_min_digits_postalcode(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        add_contacts_endpoint = read_config("endpoints", "contacts")
        # entering postalcode less than 3 digits
        row = 3
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = postAPIData_withToken(baseurl, add_contacts_endpoint,
                                            get_add_contacts_payload(self.sheetname, row), token)
        response_data = add_contacts_response.json()

        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Contact validation failed"
        assert response_data["message"] ==  "Contact validation failed: postalCode: Postal code is invalid"


    def test_add_contacts_with_more_than_max_digits_postalcode(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        add_contacts_endpoint = read_config("endpoints", "contacts")
        # entering postal code more than 10 digits
        row = 4
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = postAPIData_withToken(baseurl, add_contacts_endpoint,
                                            get_add_contacts_payload(self.sheetname, row), token)
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Contact validation failed"
        assert response_data["message"] ==  "Contact validation failed: postalCode: Path `postalCode` (`52410012457`) is longer than the maximum allowed length (10)."

    def test_add_contacts_with_special_chars_postalcode(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        add_contacts_endpoint = read_config("endpoints", "contacts")
        # entering postal code with special chars
        row = 5
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = postAPIData_withToken(baseurl, add_contacts_endpoint,
                                            get_add_contacts_payload(self.sheetname, row), token)
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Contact validation failed"
        assert response_data["message"] ==  "Contact validation failed: postalCode: Postal code is invalid"


    def test_add_contacts_with_decimal_number_postalcode(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        add_contacts_endpoint = read_config("endpoints", "contacts")
        row = 6
        payload = read_json_file(self.valid_json_file)

        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = postAPIData_withToken(baseurl, add_contacts_endpoint,
                                            get_add_contacts_payload(self.sheetname, row), token)
        response_data = add_contacts_response.json()

        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Contact validation failed"
        assert response_data["message"] ==  "Contact validation failed: postalCode: Postal code is invalid"

    def test_add_contacts_with_negative_number_postalcode(self):
        # entering postal code with negative number
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        add_contacts_endpoint = read_config("endpoints", "contacts")
        row = 7
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = postAPIData_withToken(baseurl, add_contacts_endpoint,
                                            get_add_contacts_payload(self.sheetname, row), token)
        response_data = add_contacts_response.json()

        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Contact validation failed"
        assert response_data["message"] ==  "Contact validation failed: postalCode: Postal code is invalid"

    def test_add_contacts_with_alphabets_postalcode(self):
        # entering postal code alphabets
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        add_contacts_endpoint = read_config("endpoints", "contacts")
        row = 8
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = postAPIData_withToken(baseurl, add_contacts_endpoint,
                                            get_add_contacts_payload(self.sheetname, row), token)
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Contact validation failed"
        assert response_data["message"] ==  "Contact validation failed: postalCode: Postal code is invalid"

    def test_add_contacts_with_alphanumberic_phoneNumber(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        add_contacts_endpoint = read_config("endpoints", "contacts")
        # entering postal code with alphanumeric
        row = 9
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = postAPIData_withToken(baseurl, add_contacts_endpoint,
                                            get_add_contacts_payload(self.sheetname, row), token)
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Contact validation failed"
        assert response_data["message"] ==  "Contact validation failed: postalCode: Postal code is invalid"
