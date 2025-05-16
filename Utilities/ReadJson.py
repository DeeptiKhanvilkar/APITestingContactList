import json

from Utilities.ReadExcel import get_cell_data


def read_json_file(filepath):
    with open (filepath, "r") as file:
        return json.load(file)

def get_add_contacts_payload(sheetname, row):
    add_contacts_payload = {
        "firstName": get_cell_data(sheetname,row,1),
        "lastName": get_cell_data(sheetname,row,2),
        "birthdate": get_cell_data(sheetname,row,3),
        "email": get_cell_data(sheetname,row,4),
        "phone": get_cell_data(sheetname,row,5),
        "street1": get_cell_data(sheetname,row,6),
        "street2": get_cell_data(sheetname,row,7),
        "city": get_cell_data(sheetname,row,8),
        "stateProvince": get_cell_data(sheetname,row,9),
        "postalCode": get_cell_data(sheetname,row,10),
        "country": get_cell_data(sheetname,row,11)
    }
    return add_contacts_payload

def get_add_contacts_payload_missing_firstname(sheetname, row):
    add_contacts_payload = {
        "lastName": get_cell_data(sheetname,row,2),
        "birthdate": get_cell_data(sheetname,row,3),
        "email": get_cell_data(sheetname,row,4),
        "phone": get_cell_data(sheetname,row,5),
        "street1": get_cell_data(sheetname,row,6),
        "street2": get_cell_data(sheetname,row,7),
        "city": get_cell_data(sheetname,row,8),
        "stateProvince": get_cell_data(sheetname,row,9),
        "postalCode": get_cell_data(sheetname,row,10),
        "country": get_cell_data(sheetname,row,11)
    }
    return add_contacts_payload

def get_add_contacts_payload_missing_lastname(sheetname, row):
    add_contacts_payload = {
        "firstName": get_cell_data(sheetname,row,1),
        "birthdate": get_cell_data(sheetname,row,3),
        "email": get_cell_data(sheetname,row,4),
        "phone": get_cell_data(sheetname,row,5),
        "street1": get_cell_data(sheetname,row,6),
        "street2": get_cell_data(sheetname,row,7),
        "city": get_cell_data(sheetname,row,8),
        "stateProvince": get_cell_data(sheetname,row,9),
        "postalCode": get_cell_data(sheetname,row,10),
        "country": get_cell_data(sheetname,row,11)
    }
    return add_contacts_payload

def get_add_contacts_invalid_birthdate_payload(sheetname, row):
    add_contacts_payload = {
        "firstName": get_cell_data(sheetname,row,1),
        "birthdate": get_cell_data(sheetname,row,3),
        "email": get_cell_data(sheetname,row,4),
        "phone": get_cell_data(sheetname,row,5),
        "street1": get_cell_data(sheetname,row,6),
        "street2": get_cell_data(sheetname,row,7),
        "city": get_cell_data(sheetname,row,8),
        "stateProvince": get_cell_data(sheetname,row,9),
        "postalCode": get_cell_data(sheetname,row,10),
        "country": get_cell_data(sheetname,row,11)
    }
    return add_contacts_payload

# def get_add_contacts_phoneNumber_payload(sheetname, row):
#     add_contacts_payload = {
#         "firstName": get_cell_data(sheetname,row,1),
#         "lastName": get_cell_data(sheetname,row,2),
#         "birthdate": get_cell_data(sheetname,row,3),
#         "email": get_cell_data(sheetname,row,4),
#         "phone": get_cell_data(sheetname,row,5),
#         "street1": get_cell_data(sheetname,row,6),
#         "street2": get_cell_data(sheetname,row,7),
#         "city": get_cell_data(sheetname,row,8),
#         "stateProvince": get_cell_data(sheetname,row,9),
#         "postalCode": get_cell_data(sheetname,row,10),
#         "country": get_cell_data(sheetname,row,11)
#     }
#     return add_contacts_payload


