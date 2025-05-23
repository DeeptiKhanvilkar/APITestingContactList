from Utilities.ConfigReader import read_config
from Utilities.ReadJson import read_json_file
from Utilities.apiUtils import postAPIData
from Utilities.apiUtilsNegative import getAPIData_withoutToken


class TestGetAllContacts:
    baseurl = read_config("baseUrl", "url")
    get_contact_endpoint = read_config("endpoints", "contacts")
    # token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NjAyOTZmMDYzOWVkODAwMTM3OGE5YWMiLCJpYXQiOjE3NDY2NTA4NzJ9.pkNYHewub-8q0eL-BXYj9no18BhZEuPO51YI__zodxk"
    def test_verify_get_all_contacts_unauthorized(self):
        valid_json_file = '../../TestData/validLogin.json'
        payload = read_json_file(valid_json_file)
        login_endpoint = read_config("endpoints", "login")
        login_response = postAPIData(self.baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        contact_id = response_data["user"]["_id"]
        response = getAPIData_withoutToken(self.baseurl, self.get_contact_endpoint )
        assert response.status_code == 401
        assert login_response.elapsed.total_seconds() <= 500
        response_data = response.json()
        assert response_data["error"] == "Please authenticate."
