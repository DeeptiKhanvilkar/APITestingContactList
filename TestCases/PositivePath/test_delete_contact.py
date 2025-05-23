from Utilities.ConfigReader import read_config
from Utilities.ReadJson import read_json_file, get_add_contacts_payload
from Utilities.apiUtils import postAPIData, deleteAPIData, postAPIData_withToken


class TestDeleteContact:

    def test_delete_contact(self):
        baseurl = read_config("baseUrl", "url")
        valid_json_file = '../../TestData/validLogin.json'
        sheetname = "add_contacts_valid"
        row = 3
        payload = read_json_file(valid_json_file)
        login_endpoint = read_config("endpoints", "login")
        login_response = postAPIData(baseurl, login_endpoint, payload)
        assert login_response.status_code == 200
        response_data = login_response.json()
        token = response_data["token"]
        add_contacts_endpoint = read_config("endpoints", "contacts")
        print(get_add_contacts_payload(sheetname, row))
        add_contacts_response = postAPIData_withToken(baseurl, add_contacts_endpoint,
                                                      get_add_contacts_payload(sheetname, row), token)
        response_data = add_contacts_response.json()
        print(response_data)
        assert add_contacts_response.status_code == 201
        assert add_contacts_response.elapsed.total_seconds() <= 500
        id = response_data["_id"]
        print(id)
        get_specific_contacts_endpoint = read_config("endpoints", "specific_contacts")
        delete_contact_response = deleteAPIData(baseurl, get_specific_contacts_endpoint +f"{id}" , token)
        assert delete_contact_response.status_code== 200
        assert delete_contact_response.elapsed.total_seconds() <= 500
        # print(delete_contact_response.text)
        assert delete_contact_response.text == "Contact deleted"
