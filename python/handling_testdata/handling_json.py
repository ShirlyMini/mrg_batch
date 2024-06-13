import json # inbuilt package

fr = open(r"C:\Users\user\PycharmProjects\pythonProject_March_mrng_batch\python\handling_testdata\testdata_json.json")
json_content = fr.read()
print(json_content)

# convert json to python dict

json_dict = json.loads(json_content)
print(json_dict['login_data'])
for data in json_dict['login_data'].values():
    print(data)
    print(data['user'])
    print(data['password'])
    print(data['expected'])