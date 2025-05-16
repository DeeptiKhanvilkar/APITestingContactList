import requests


def getAPIData_withoutToken(url, endpoint):
    header = {"Content-Type": "application/json"}
    response = requests.get(url+ endpoint, headers=header)
    print("RequestURL: " , url + endpoint)
    print("Request Header: " , response.request.headers)
    return response