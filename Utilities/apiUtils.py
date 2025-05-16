import requests
from Utilities.ConfigReader import read_config
from Utilities.ReadExcel import get_cell_data
from Utilities.ReadJson import read_json_file, get_add_contacts_payload


def getAPIData(url, endpoint, token):
    header = {"Content-Type": "application/json", "Authorization" : token}
    response = requests.get(url+ endpoint, headers=header)
    print("RequestURL: " , url + endpoint)
    print("Request Header: " , response.request.headers)
    return response


def postAPIData(url, endpoint, body):
    header = {"Content-Type": "application/json"}
    response = requests.post(url + endpoint, json=body, headers=header)
    print("RequestURL: ", url + endpoint)
    print("Request Header: ", response.request.headers)
    return response

def deleteAPIData(url, endpoint, token):
    header = {"Content-Type": "application/json", "Authorization": token}
    response = requests.delete(url + endpoint, headers=header)
    print("RequestURL: ", url + endpoint)
    print("Request Header: ", response.request.headers)
    return response

def postAPIData_withToken(url, endpoint, body, token):
    header = {"Content-Type": "application/json", "Authorization": token}
    response = requests.post(url + endpoint, json=body, headers=header)
    print("RequestURL: ", url + endpoint)
    # print("Request Header: ", response.request.headers)
    return response

def putAPIData_withToken(url, endpoint, body, token):
    header = {"Content-Type": "application/json", "Authorization": token}
    response = requests.put(url + endpoint, json=body, headers=header)
    print("RequestURL: ", url + endpoint)
    # print("Request Header: ", response.request.headers)
    return response

def add_contacts():
    sheetname = "add_contacts_valid"
    baseurl = read_config("baseUrl", "url")
    login_endpoint = read_config("endpoints", "login")
    valid_json_file = '../TestData/validLogin.json'
    add_contacts_endpoint = read_config("endpoints", "contacts")
    row = 3
    payload = read_json_file(valid_json_file)
    login_response = postAPIData(baseurl, login_endpoint, payload)
    assert login_response.status_code == 200
    response_data = login_response.json()
    token = response_data["token"]
    print(get_add_contacts_payload(sheetname, row))
    add_contacts_response = postAPIData_withToken(baseurl, add_contacts_endpoint,
                                        get_add_contacts_payload(sheetname, row), token)
    response_data = add_contacts_response.json()
    print(response_data)
    assert add_contacts_response.status_code == 201
    assert add_contacts_response.elapsed.total_seconds() <= 500
    id = response_data["_id"]  # 6821138fdf49e700157f1274   68211566b8b48600157dd24d 682115acb8b48600157dd24f
    param_list = [token, id]
    return param_list