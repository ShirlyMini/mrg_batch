#{login_data:{row1:{user...}}}

import yaml



fr = open(r"C:\Users\user\PycharmProjects\pythonProject_March_mrng_batch\python\handling_testdata\test_data_yaml.yml")
yml_content = fr.read()

print(yml_content)
# convert yaml to python dict
yaml_dict = yaml.load(yml_content, Loader=yaml.FullLoader)
print(yaml_dict['login_data'])
for data in yaml_dict['login_data'].values():
    print(data)
    print(data['user'])
    print(data['password'])
    print(data['expected'])



