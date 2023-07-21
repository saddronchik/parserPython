import xlsxwriter
from main import array_items

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook("parsing.xlsx")
worksheet = workbook.add_worksheet("товар")

def writer(parametr):


    row = 0
    column = 0

    worksheet.set_column("A:A",20)
    worksheet.set_column("B:B",20)
    worksheet.set_column("C:C",50)
    worksheet.set_column("D:D",50)

    for item in parametr():
        worksheet.write(row,column, item[0])
        worksheet.write(row,column+1, item[1])
        worksheet.write(row,column+2, item[2])
        worksheet.write(row,column+3, item[3])
        row += 1
        
writer(array_items)

workbook.close()