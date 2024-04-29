#upper()_case
nm="Prith"
print(nm.upper())
print("\n")

#lower()_case
print(nm.lower())
print("\n")

#rstrip()
nm1="Hey!!!!!!!!!!!!!!"
print(nm1)
print(nm1.rstrip("!"))
nm2="!!!!!!!Hey!!!!!!!" #only strips after Hey
print(nm2)
print(nm2.rstrip("!"))
print("\n")

#replace()
a="Prith"
print(a)
print(a.replace("Prith","Chouhan"))
print("\n")

# slit()
a1="Hello How Are You?"
print(a1.split(" "))
print("\n")

# capitaalize()
a2="Hello How Are You doing"
print(a2)
print(a2.capitalize())
print("\n")

# center()
a3="Hello How Are You doing?"
print(a3)
print(len(a3))
print(a3.center(50))
print(len(a3.center(50)))#length of the string becomes 50
print("\n")

# count()
a="Hello hello hello hi hi hi hi"
print(a.count("Hello"))
print(a.count("hello"))
print(a.count("hi"))
print("\n")

# endswith()
a3="Hello How Are You doing?"
print(a3.endswith("?"))
print(a3.endswith("How",1,15))
a3="Hello to How Are You doing?"
print(a3.endswith("to",4,8))
print("\n")

# find()
a4="Hello to How Are You doing?"
print(a4.find("How"))
print(a4.find("how"))#o/p:-1-->No accurance
print("\n")

# index()
print(a4.index("How"))
# print(a4.index("how"))#Substring not found error --->Line was commented out bcoz it rising exception will running the code
print("\n")

#isalnum()
a5="WelCome12"
a5_1="WelCome12#"
print(a5.isalnum())
print(a5_1.isalnum())
print("\n")

# islower()
a6="welcome"
print(a6.islower())
print("\n")

#isprintable()
a7="\n"
print(a7.isprintable())#We cannot print \n or \t
print("\n")

#issplace()
a8="    "
print(a8.isspace())
print("\n")

#istittle()
a9='Types Of Blog Post Titles That Get Clicked A Beginner\'S Guide'
print(a9)
print(a9.istitle())
print("\n")

#startswith()
print(a9.startswith("Types"))
print("\n")

#swapcase()
a10="welcome to my blog"
print(a10.swapcase())
print("\n")

#title()
print(a10.title())
print("\n")