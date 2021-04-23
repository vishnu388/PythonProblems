"""
date = '20/04/2021'
modified_date = '21/04/2021'
author = 'vishnu'
description = 'User Input and Replace String Template “Hello <<UserName>>, How are you?”'
"""
string = "“Hello <<UserName>>, How are you?”"
print("Enter the name to change : ")
st = input()
# using string replace method to replace string
String = string.replace("<<UserName>>", st)
print(String)
