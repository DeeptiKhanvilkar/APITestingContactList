import openpyxl

def get_cell_data(sheetname, row, col):
    workbook = openpyxl.load_workbook("../TestData/TestData.xlsx")
    sheet = workbook[sheetname]
    return sheet.cell(row, col).value

