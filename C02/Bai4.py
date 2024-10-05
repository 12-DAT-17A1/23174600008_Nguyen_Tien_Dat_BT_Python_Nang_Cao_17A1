import xml.dom.minidom as md 


doc = md.parse('sample.xml')

nameCompany = doc.getElementsByTagName('name')[0].firstChild.data
print('Tên công ty:',nameCompany)
list_employees = doc.getElementsByTagName('staff')
for tag_employee in list_employees:
    id_employee = tag_employee.getAttribute('id')
    name_employee = tag_employee.getElementsByTagName('name')[0].firstChild.data 
    salary_employee = tag_employee.getElementsByTagName('salary')[0].firstChild.data
    type_salary = salary_employee.split()[-1]
    print(f'ID: {id_employee}\nTên nhân viên: {name_employee}\nLương: {salary_employee.rsplit(sep=' ',maxsplit=1)[0]}\nĐơn vị: {type_salary}')
    print('-'*30)