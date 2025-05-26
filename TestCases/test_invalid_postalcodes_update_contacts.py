from Utilities.ConfigReader import read_config
from Utilities.ReadJson import *
# from Utilities.ReadJson import get_add_contacts_payload, read_json_file,  \
#     get_add_contacts_payload_missing_firstname, get_add_contacts_payload_missing_lastname, \
#     get_add_contacts_payload_missing_birthdate, get_add_contacts_payload_missing_email, \
#     get_add_contacts_payload_missing_phone, get_add_contacts_payload_missing_street1, \
#     get_add_contacts_payload_missing_street2, get_add_contacts_payload_missing_city, \
#     get_add_contacts_payload_missing_stateProvince, get_add_contacts_payload_missing_postalCode, \
#     get_add_contacts_payload_missing_country
from Utilities.apiUtils import postAPIData, add_contacts, putAPIData_withToken


class TestAddContactsInvalid:
    sheetname = "add_contacts_invalid_postalcode"
    valid_json_file = '../TestData/validLogin.json'
    param_list = add_contacts()

    def test_add_contacts_empty_postal(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        add_contacts_endpoint = read_config("endpoints", "specific_contacts")
        # Entering empty string
        row = 2
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = putAPIData_withToken(baseurl, add_contacts_endpoint + self.param_list[1],
                                                     get_add_contacts_payload(self.sheetname, row), self.param_list[0])
        response_data = add_contacts_response.json()

        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Validation failed"
        assert response_data["message"] ==  "Validation failed: postalCode: Expected a string but received a null"


    def test_add_contacts_with_min_digits_postalcode(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        add_contacts_endpoint = read_config("endpoints", "specific_contacts")
        # entering postalcode less than 3 digits
        row = 3
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = putAPIData_withToken(baseurl, add_contacts_endpoint + self.param_list[1],
                                                     get_add_contacts_payload(self.sheetname, row), self.param_list[0])
        response_data = add_contacts_response.json()

        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Validation failed"
        assert response_data["message"] ==  "Validation failed: postalCode: Postal code is invalid"


    def test_add_contacts_with_more_than_max_digits_postalcode(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        add_contacts_endpoint = read_config("endpoints", "specific_contacts")
        # entering postal code more than 10 digits
        row = 4
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = putAPIData_withToken(baseurl, add_contacts_endpoint + self.param_list[1],
                                                     get_add_contacts_payload(self.sheetname, row), self.param_list[0])
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Validation failed"
        assert response_data["message"] ==  "Validation failed: postalCode: Path `postalCode` (`52410012457`) is longer than the maximum allowed length (10)."

    def test_add_contacts_with_special_chars_postalcode(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        add_contacts_endpoint = read_config("endpoints", "specific_contacts")
        # entering postal code with special chars
        row = 5
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200

        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = putAPIData_withToken(baseurl, add_contacts_endpoint + self.param_list[1],
                                                     get_add_contacts_payload(self.sheetname, row), self.param_list[0])
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Validation failed"
        assert response_data["message"] ==  "Validation failed: postalCode: Postal code is invalid"


    def test_add_contacts_with_decimal_number_postalcode(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        add_contacts_endpoint = read_config("endpoints", "specific_contacts")
        row = 6
        payload = read_json_file(self.valid_json_file)

        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = putAPIData_withToken(baseurl, add_contacts_endpoint + self.param_list[1],
                                                     get_add_contacts_payload(self.sheetname, row), self.param_list[0])
        response_data = add_contacts_response.json()

        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Validation failed"
        assert response_data["message"] ==  "Validation failed: postalCode: Postal code is invalid"

    def test_add_contacts_with_negative_number_postalcode(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        add_contacts_endpoint = read_config("endpoints", "specific_contacts")
        # entering postal code with negative number
        row = 7
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = putAPIData_withToken(baseurl, add_contacts_endpoint + self.param_list[1],
                                                     get_add_contacts_payload(self.sheetname, row), self.param_list[0])
        response_data = add_contacts_response.json()

        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Validation failed"
        assert response_data["message"] ==  "Validation failed: postalCode: Postal code is invalid"

    def test_add_contacts_with_alphabets_postalcode(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        add_contacts_endpoint = read_config("endpoints", "specific_contacts")
        # entering postal code alphabets
        row = 8
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = putAPIData_withToken(baseurl, add_contacts_endpoint + self.param_list[1],
                                                     get_add_contacts_payload(self.sheetname, row), self.param_list[0])
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Validation failed"
        assert response_data["message"] ==  "Validation failed: postalCode: Postal code is invalid"

    def test_add_contacts_with_alphanumberic_phonenumber(self):
        baseurl = read_config("baseUrl", "url")
        login_endpoint = read_config("endpoints", "login")
        add_contacts_endpoint = read_config("endpoints", "specific_contacts")
        # entering postal code with alphanumeric
        row = 9
        payload = read_json_file(self.valid_json_file)
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = putAPIData_withToken(baseurl, add_contacts_endpoint + self.param_list[1],
                                                     get_add_contacts_payload(self.sheetname, row), self.param_list[0])
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Validation failed"
        assert response_data["message"] ==  "Validation failed: postalCode: Postal code is invalid"
