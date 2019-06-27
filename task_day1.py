print("***** write a program to capture any filename(with extension) from the keyboard and display the filename *****")
filename= input("Enter any filename : ")
print("File that you entered is : ", filename)

print("----------------------------------------------------------------------------")
print("***** write a program to capture any filename(with extension) from keyboad and display the filename and extension seperately *****")
alist = filename.split(".")
print("Output : ")
print("filename : ", alist[0])
print("extension : ", alist[1])

print("----------------------------------------------------------------------------")
print("write a program to capure 2 numbers from the keyboard and display its number")
firstnumber = int(input("Enter first number : "))
secondnumber = int(input("Enter Second number : "))

print("Sum of the numbers", firstnumber + secondnumber)

print("----------------------------------------------------------------------------")
print("write a program to perform the below operations define string as below")

name = "Python programming"
print("Original string : ", name)
print("replace 'python' to 'scala' and display the string : ", name.replace("Python", "scala"))
print("display the string in upper case : ", name.upper())
namelist = name.split(" ")
print("split the string and display the output : ", namelist)
print("length of the string : ", len(name))
print("reverse of the string : ", name [::-1])
print("display the no. of occurences of p in the string : ", name.count("p"))

print("----------------------------------------------------------------------------")
print("display tuple as below - ('unix','oracle')")
atup = ('unix','oracle')
print("tuple : ", atup)
alist=list(atup)
alist.append("hadoop")
print("append hadoop to the list", alist)
alist.append("scala")
print("append scala to the list", alist)
alist.extend(["Ruby", "Python", "Matlab"])
print("add ruby, python , matlab to thelist", alist)
alist.append("mongodb")
print("append mongodb to the list", alist)
print("display the no. of the elements inside the list", len(alist))
print("count the no. of occurences of 'unix' in the list", alist.count("unix"))
alist.remove("oracle")
print("removed oracle", alist)
alist.remove("Python")
print("removed python", alist)

print ("display the no. of the elements inside the list", alist)


print("----------------------------------------------------------------------------")
print("write a program to remove all the duplicates from the list - alist = [10,20,20,30,40,40,10,50,60]")
alist = [10,20,20,30,40,40,10,50,60]
alist = list(set([10,20,20,30,40,40,10,50,60]))

print("distinct list : ", alist)
print("----------------------------------------------------------------------------")
print("write a program to capture filename(with extension) from the keyboard and replace its extension as below")
filenamewithextn = input("Enter any filename : abc.doc : ")
filenamelist = filenamewithextn.split(".")
print("fter changing the extension : abc.docx : ", filenamelist[0] + ".docx")
print("----------------------------------------------------------------------------")
print("write a program to capture 2 strings from the keyboard and concatenate the strings.")
firststring = input("Enter first string : ")
secondstring = input("Enter second string : ")
print("Output : ", firststring + " " + secondstring)
print("----------------------------------------------------------------------------")
print("write a program to capture any string from keyboard and display the upper or lower")
inputstring = input("Enter String : ")
if inputstring.isupper():
    print("Entered word is in Upper case")
elif inputstring.islower():
    print("Entered word is in lower case")
else:
    print("Entered word is in normal case")

print("----------------------------------------------------------------------------")
print("write a program to check the file extension.")
filename = input("Enter file name with extension : ")
splittedfname = filename.split(".")
if splittedfname[1] == "py":
    print("It is Python file")
elif splittedfname[1] == "sh":
    print("It is bash shell file")
elif splittedfname[1] == "pl":
    print("It is perl file")
else:
    print("It is files with other than .py, .sh and .pl extension")
    print("----------------------------------------------------------------------------")

print("write a program to display all the numbers from 50 to 1 using")
for val in range(50, 0, -1):
    print(val, end=";")
    print("----------------------------------------------------------------------------")
    print("write a program to display all the even numbers from 90 to 80")
for val in range(90, 80, -2):
    print(val, end=";")

    print("----------------------------------------------------------------------------")
    print("write a program to prefix 'http://' and postfix '.com' to all the elements of the list")
alist = ['google','linkedin','facebook']
print(alist)
print("Output : ")
for val in alist:
    print("http://" + val + ".com")

print("----------------------------------------------------------------------------")
print("write a program to check and prefix 'http://' if the element is not starting with 'http://' and postfix '.com' to all the elements of the list")
alist = ['google','http://linkedin','facebook']

for val in alist:
    sitename = val
if not val.startswith("http://"):
    sitename="http://" + val

if not val.endswith(".com"):
    sitename= sitename + ".com"

print(sitename)
print("----------------------------------------------------------------------------")
print("write a program to display the below output")
for val in range(1, 11):
    print(str(val) + ".py")
    print("----------------------------------------------------------------------------")

print("write a program to display the series of IP addresses in the below format.")
for val in range(1, 101):
    print("192.168.0." + str(val), end=";")

print("----------------------------------------------------------------------------")

print("write a program to display the IPs in the below format.")
for val in range(0, 2):
    for val1 in range(1, 11):
        print("192.168." + str(val) + "." + str(val1))
        print("----------------------------------------------------------------------------")
        print("-------------------***** THANK YOU *****--------------------")

## IP Address check program --
ipadd=input ("Enter IP Address:")
list1=ipadd.split(".")
length=len(list1)
if length>4:
    print("Incorrect IP Address!!!")
    exit()
for x in list1:
    if int(x) not in range(0,256):
        print ("Incorrect IP Address!!!")
        break
print("Correct IP Address")