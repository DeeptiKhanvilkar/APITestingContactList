from Utilities.ConfigReader import read_config
from Utilities.ReadJson import read_json_file
from Utilities.apiUtils import postAPIData, getAPIData


class TestGetSpecificContact:

    def test_get_specific_contact_no_found(self):
        baseurl = read_config("baseUrl", "url")
        valid_json_file = '../../TestData/validLogin.json'
        payload = read_json_file(valid_json_file)
        login_endpoint = read_config("endpoints", "login")
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]
        get_specific_contacts_endpoint = read_config("endpoints", "specific_contacts")
        id = "6821138fdf49e700157f1274"
        get_specifi_contact_response = getAPIData(baseurl, get_specific_contacts_endpoint + f"{id}", token)
        assert get_specifi_contact_response.status_code == 404
        assert get_specifi_contact_response.elapsed.total_seconds() <= 500



