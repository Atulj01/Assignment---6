#  Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

import json

Dict = {"Maharastra":"Mumbai","Madhya Pradesh":"Bhopal","Gujrat":"Gandhinagar","Bihar":"Patna","Goa":"Panaji","Manipur":"Imphal","Meghalaya":"Shillong"}
with open('G:\\data science 290822B\\assignment_6\\_2_result.json', 'w') as file:
    json.dump(Dict, file,indent=7)
    print(dict)



