import xmltodict

fr = open(r"C:\Users\user\PycharmProjects\pythonProject_March_mrng_batch\python\handling_testdata\xml_data.xml")
xml_content = fr.read()

xml_dict = xmltodict.parse(xml_content)
print(xml_dict['login_data'])
for data in xml_dict['login_data'].values():
    print(data)
    print(data['user'])
    print(data['password'])
    print(data['expected'])