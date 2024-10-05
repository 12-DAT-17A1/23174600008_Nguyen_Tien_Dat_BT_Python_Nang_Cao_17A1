import xml.etree.ElementTree as et


tree = et.parse('sample.xml')
root = tree.getroot()
nameCompany = root.find('name').text
print('Tên công ty:',nameCompany)
print('Tên các nhân viên:')
listname_employees = root.findall('staff')
for tagName in listname_employees:
    print(tagName.find('name').text)