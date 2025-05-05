#Juedeja Richard - Module8.2 - 4/27/25
#This function oops through the .json class list and prints out each value
#then the JSON dump() function will append new data to the .json file
#while sending a notification the student list and json file was updated

import json
#open and read json file data
with open('student.json') as f:
#returns JSON object from array as python dictionary(loading a file)
 data = json.load(f)

#iterates/loops through list in json and prints only value results
print("--This is the Original Student List--\n")
for i in data:
    print(i['L_Name'],',', i['F_Name'],': ID =', i['Student_ID'], i['Email'])

#What will be written to the student json file in memory
data.append({
    "F_Name": "Juedeja",
    "L_Name": "Richard",
    "Student_ID": "456123",
    "Email": "jrichard@my365.bellevue.edu"
})

#Notification for List Update
print("\n*New Data has been added to the Student List*\n")
print("--Displaying Updated Student List--\n")
#Display new list
for i in data:
    print(i['L_Name'],',', i['F_Name'],': ID =', i['Student_ID'], i['Email'])

#Acutally writes the new data to json file with dump function
with open('student.json','w') as f:
   json.dump(data, f, indent = 4)

print("\n*Your JSON File has been Updated*\n")

#Read, Write and Parse JSON using Python. (2019, December 27). GeeksforGeeks.
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/‌

#https://www.facebook.com/fewlines4biju. (2024, November 29). How To Get Values From A JSON Array In Python? Python Guides.
# https://pythonguides.com/json-data-in-python/‌