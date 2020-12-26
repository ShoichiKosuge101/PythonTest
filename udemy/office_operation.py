import openpyxl as px

wb = px.load_workbook('excel_sample.xlsx')
ws = wb.active
ws['A1']= 'Hello!'
ws.title = 'sample_title1'
wb.save('excel_sample.xlsx')