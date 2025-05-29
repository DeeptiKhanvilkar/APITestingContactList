import jsonschema
import pytest

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
from Utilities.apiUtils import postAPIData, putAPIData_withToken, add_contacts
from schemas.add_contacts_schema import add_contacts_schema


class TestAddContactsInvalid:
    sheetname = "add_contacts_invalid_phone"
    valid_json_file = '../TestData/validLogin.json'




    def test_update_contacts_empty_phonenumber(self):
        param_list = add_contacts()
        baseurl = read_config("baseUrl", "url")
        add_contacts_endpoint = read_config("endpoints", "specific_contacts")
        row = 2
        print(param_list)
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = putAPIData_withToken(baseurl, add_contacts_endpoint+param_list[1],
                                            get_add_contacts_payload(self.sheetname, row), param_list[0])
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Validation failed"
        assert response_data["message"] ==  "Validation failed: phone: Expected a string but received a null"


    # @pytest.mark.skip
    def test_update_contacts_with_min_digits_phonenumber(self):
        param_list = add_contacts()
        baseurl = read_config("baseUrl", "url")
        add_contacts_endpoint = read_config("endpoints", "specific_contacts")
        # entering phone number less than 6 digits
        row = 3
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = putAPIData_withToken(baseurl, add_contacts_endpoint+param_list[1],
                                            get_add_contacts_payload(self.sheetname, row), param_list[0])
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Validation failed"
        assert response_data["message"] ==  "Validation failed: phone: Phone number is invalid"

    # @pytest.mark.skip
    def test_update_contacts_with_more_than_max_digits_phonenumber(self):
        param_list = add_contacts()
        baseurl = read_config("baseUrl", "url")
        add_contacts_endpoint = read_config("endpoints", "specific_contacts")
        # entering phone number more than 15 digits
        row = 4
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = putAPIData_withToken(baseurl, add_contacts_endpoint+param_list[1],
                                            get_add_contacts_payload(self.sheetname, row), param_list[0])
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Validation failed"
        assert response_data["message"] ==  "Validation failed: phone: Path `phone` (`1234567891234567`) is longer than the maximum allowed length (15)."

    # @pytest.mark.skip
    def test_update_contacts_with_special_chars_phonenumber(self):
        param_list = add_contacts()
        baseurl = read_config("baseUrl", "url")
        add_contacts_endpoint = read_config("endpoints", "specific_contacts")
        # entering phone number with special chars
        row = 5
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = putAPIData_withToken(baseurl, add_contacts_endpoint+param_list[1],
                                            get_add_contacts_payload(self.sheetname, row), param_list[0])
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Validation failed"
        assert response_data["message"] ==  "Validation failed: phone: Phone number is invalid"

    # @pytest.mark.skip
    def test_update_contacts_with_decimal_number_phonenumber(self):
        param_list = add_contacts()
        baseurl = read_config("baseUrl", "url")
        add_contacts_endpoint = read_config("endpoints", "specific_contacts")
        # entering phone number with decimal number
        row = 6
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = putAPIData_withToken(baseurl, add_contacts_endpoint + param_list[1],
                                                     get_add_contacts_payload(self.sheetname, row), param_list[0])
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Validation failed"
        assert response_data["message"] ==  "Validation failed: phone: Phone number is invalid"

    # @pytest.mark.skip
    def test_update_contacts_with_negative_number_phonenumber(self):
        param_list = add_contacts()
        baseurl = read_config("baseUrl", "url")
        add_contacts_endpoint = read_config("endpoints", "specific_contacts")
        # entering phone number with negative numbers
        row = 7
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = putAPIData_withToken(baseurl, add_contacts_endpoint + param_list[1],
                                                     get_add_contacts_payload(self.sheetname, row), param_list[0])
        response_data = add_contacts_response.json()

        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Validation failed"
        assert response_data["message"] ==  "Validation failed: phone: Phone number is invalid"

    # @pytest.mark.skip
    def test_update_contacts_with_alphabets_phonenumber(self):
        param_list = add_contacts()
        baseurl = read_config("baseUrl", "url")
        add_contacts_endpoint = read_config("endpoints", "specific_contacts")
        # entering phone number with alphabets
        row = 8
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = putAPIData_withToken(baseurl, add_contacts_endpoint + param_list[1],
                                                     get_add_contacts_payload(self.sheetname, row), param_list[0])
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Validation failed"
        assert response_data["message"] ==  "Validation failed: phone: Phone number is invalid"

    # @pytest.mark.skip
    def test_update_contacts_with_alphanumberic_phonenumber(self):
        param_list = add_contacts()
        baseurl = read_config("baseUrl", "url")
        add_contacts_endpoint = read_config("endpoints", "specific_contacts")
        # entering phone number with alphanumberic
        row = 9
        print(get_add_contacts_payload(self.sheetname, row))
        add_contacts_response = putAPIData_withToken(baseurl, add_contacts_endpoint + param_list[1],
                                                     get_add_contacts_payload(self.sheetname, row), param_list[0])
        response_data = add_contacts_response.json()
        print(response_data["message"])
        assert add_contacts_response.status_code == 400
        assert add_contacts_response.elapsed.total_seconds() <= 500
        assert response_data["_message"] == "Validation failed"
        assert response_data["message"] ==  "Validation failed: phone: Phone number is invalid"
