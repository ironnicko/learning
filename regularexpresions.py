import re

#to find email address from the sentence.

string = "his email someone@gmail.com address is his@hotmail.co.in and he is now also using his.mail@ibm.ca"

a = re.findall("(?<=\s)\w+?\.?\w+@\w+[\.\w+]+", string)
length = len(a) 
count = 0
for i in a:
    count += 1 
    print(i, end=("\n", ",\n")[count != length])
