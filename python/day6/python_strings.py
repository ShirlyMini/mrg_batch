# str1="welcome"
# print(len(str1))
#
# #####exsistence of substing
# str1="this is python"
# print("python" in str1)
# print("python" not in str1)

#####comapare two strings

# print("string"=="strong")
# print("string"!="strong")
# print("string">"strong")
# print("string"<"strong")

####testing strings

# print("welcome".isalpha())
# print("welcome11131".isalpha())
# print("welcome".isalnum())
# print("11131".isalnum())
# print("welcome11131".isalnum())
# print("welcome".isdigit())
# print("11131".isdigit())
# print("welcome11131".isdigit())

# print("   ".isspace())
# print("   kldsmk   ".isspace())

# print("welcome".islower())
# print("welcome11".islower())
# print("welcome11AAA".islower())

# print("welcome".isupper())
# print("welcome11".isupper())
# print("welcome11AAA".isupper())
# print("AAA".isupper())


#####searching substring

# str1="welcome to python to to to"

# print(str1.startswith("wel"))
# print(str1.startswith("to"))
# print(str1.endswith("python"))
# print(str1.endswith("come"))
#
# print(str1.index("wel"))
# print(str1.index("to"))
# print(str1.index("o"))
# print(str1.index("o",5))
# print(str1.index("o",10))

# print(str1.count("o"))
# print(str1.count("to"))

#####converting strings

# str1="welcome"

# str2=str1.upper()
# print(str2[2:4])

# print("WELCOME".lower())
# print("WELCOME".capitalize())
# print("WELCOME to python".title())
# print("WELCOME to python".swapcase())

# str1="welcome to python python python"
# print(str1.replace("python", "java"))

# str1="001200300"
#
# print(str1.strip("0"))
# print(str1.lstrip("0"))
# print(str1.rstrip("0"))


str1="001200300"
# print(str1.removeprefix("0"))
# print(str1.removesuffix("0"))

print(str1.replace("00", ""))