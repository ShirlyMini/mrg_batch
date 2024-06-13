# collection of key and value pair
# unordered - access the value using key
# muatable - add, remove, copy
# key should be unique
# duplicates of key not allowed

### create
# d1={"product1":100, "product2":110, "production3":200}
# print(d1)
# print(type(d1))

## empty dict
# d2={}
# d3=dict()
# print(d2)
# print(d3)


#####

# d1={"product1":100, "product2":110, "production3":200}
# d2={1:"one", 2:"two"}
# d4={1:[1,3,5,7], 2:(2,4,6)}
# d3={[1,2,3]:"one", (2,4,6):"two"}#TypeError: unhashable type: 'list'
#
# print(d1,d2,d4)

####dup keys
# d1={"brand":"Maruthi", "year": "2023", "model":1102, "brand":"Audi", "brand":"Hyundai"}
# print(d1)#{'brand': 'Hyundai', 'year': '2023', 'model': 1102}

###reading values

# d1={'brand': 'Hyundai', 'year': '2023', 'model': 1102}
#
# print(d1['brand'])
# print(d1['year'])
# print(d1['model'])
#
# print(d1.get('brand'))
# print(d1.get('year'))
# print(d1.get('model'))

###with for loop
# d1={'brand': 'Hyundai', 'year': '2023', 'model': 1102}

# print(d1.keys())#dict_keys(['brand', 'year', 'model'])
# print(d1.values())#dict_values(['Hyundai', '2023', 1102])
# print(d1.items())#dict_items([('brand', 'Hyundai'), ('year', '2023'), ('model', 1102)])
#
# for i in d1.keys():
#     print(i)
#
# for i in d1.values():
#     print(i)
#
# for k, v in d1.items():
#     print(k,v)

####check the exsistent
# d1={'brand': 'Hyundai', 'year': '2023', 'model': 1102}

# print("year" in d1)
# print("year" not in d1)
#
# print("2023" in d1)
# print("2023" not in d1)
#
# print("year" in d1.keys())
# print("year" not in d1.keys())
#
# print("2023" in d1.values())
# print("2023" not in d1.values())
#
# print(('year', '2023') in d1.items())
# print(('year', '2023') not in d1.items())
#
# ###len
# print(len(d1))

###add or update
# d1 = {'brand': 'Hyundai', 'year': '2023', 'model': 1102}

## add/update - single items
# d1["seat"]=4
# print(d1)

# d1['brand']="Maruthi"
# print(d1)

## add/update - mutilple items
# d1.update({"seat": 4, "color": "Black"})
# print(d1)

# d1.update({'brand': 'audi', 'year': '2024'})
# print(d1)

###remove

# d1 = {'brand': 'Hyundai', 'year': '2023', 'model': 1102, 'model': 1103, 'model': 1104}

# pop
# d1.pop("year")
# print(d1)


# popitem
# d1.popitem()
# print(d1)

# clear
# d1.clear()
# print(d1)

#del statement
# del d1['model']
# print(d1)

###combine 2 dict

# d1 = {'brand': 'Hyundai', 'year': '2023', 'model': 1102}
# d2 = {'brand1': 'audi', 'year1': '2024', 'model1': 1103}
#
# d1.update(d2)
# print(d1)


### copy dict(mutable)
d1 = {'brand': 'Hyundai', 'year': '2023', 'model': 1102}
# d2=d1# shallow copy
# print(f"d1{d1} id {id(d1)}")
# print(f"d2{d2} id {id(d2)}")
# d2.popitem()
# print(f"d1{d1} id {id(d1)}")
# print(f"d2{d2} id {id(d2)}")

# d2=d1.copy()# deep copy
d2=dict(d1)# deep copy
print(f"d1{d1} id {id(d1)}")
print(f"d2{d2} id {id(d2)}")
d2.popitem()
print(f"d1{d1} id {id(d1)}")
print(f"d2{d2} id {id(d2)}")