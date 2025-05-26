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

    sheetname = "add_contacts_invalid_phone"
    valid_json_file = '../TestData/validLogin.json'
    add_contacts_endpoint = read_config("endpoints", "contacts")


    def test_add_contacts_empty_phoneNumber(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        row = 2
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]

        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = postAPIData_withToken(baseurl, self.add_contacts_endpoint,
                                            get_add_contacts_payload(self.sheetname, row), token)
        response_data = add_contacts_response.json()

        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Contact validation failed"
        assert response_data["message"] ==  "Contact validation failed: phone: Expected a string but received a null"


    def test_add_contacts_with_min_digits_phoneNumber(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        # entering phone number less than 6 digits
        row = 3
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = postAPIData_withToken(baseurl, self.add_contacts_endpoint,
                                            get_add_contacts_payload(self.sheetname, row), token)
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Contact validation failed"
        assert response_data["message"] ==  "Contact validation failed: phone: Phone number is invalid"


    def test_add_contacts_with_more_than_max_digits_phoneNumber(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        # entering phone number more than 15 digits
        row = 4
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = postAPIData_withToken(baseurl, self.add_contacts_endpoint,
                                            get_add_contacts_payload(self.sheetname, row), token)
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Contact validation failed"
        assert response_data["message"] ==  "Contact validation failed: phone: Path `phone` (`1234567891234567`) is longer than the maximum allowed length (15)."

    def test_add_contacts_with_special_chars_phoneNumber(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        # entering phone number with special chars
        row = 5
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = postAPIData_withToken(baseurl, self.add_contacts_endpoint,
                                            get_add_contacts_payload(self.sheetname, row), token)
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Contact validation failed"
        assert response_data["message"] ==  "Contact validation failed: phone: Phone number is invalid"


    def test_add_contacts_with_decimal_number_phoneNumber(self):
        # entering phone number with decimal number
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        row = 6
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = postAPIData_withToken(baseurl, self.add_contacts_endpoint,
                                            get_add_contacts_payload(self.sheetname, row), token)
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Contact validation failed"
        assert response_data["message"] ==  "Contact validation failed: phone: Phone number is invalid"

    def test_add_contacts_with_negative_number_phoneNumber(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        # entering phone number with negative numbers
        row = 7
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = postAPIData_withToken(baseurl, self.add_contacts_endpoint,
                                            get_add_contacts_payload(self.sheetname, row), token)
        response_data = add_contacts_response.json()

        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Contact validation failed"
        assert response_data["message"] ==  "Contact validation failed: phone: Phone number is invalid"

    def test_add_contacts_with_alphabets_phoneNumber(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        # entering phone number with alphabets
        row = 8
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = postAPIData_withToken(baseurl, self.add_contacts_endpoint,
                                            get_add_contacts_payload(self.sheetname, row), token)
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Contact validation failed"
        assert response_data["message"] ==  "Contact validation failed: phone: Phone number is invalid"

    def test_add_contacts_with_alphanumberic_phoneNumber(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        # entering phone number with alphanumberic
        row = 9
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = postAPIData_withToken(baseurl, self.add_contacts_endpoint,
                                            get_add_contacts_payload(self.sheetname, row), token)
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Contact validation failed"
        assert response_data["message"] ==  "Contact validation failed: phone: Phone number is invalid"
