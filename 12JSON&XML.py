"""
 JSON and XML
"""

import os
import xml.etree.ElementTree as xml
import json

data = {
    "name": "Angel Morales",
    "age": 36,
    "birth_date": "01-01-1987",
    "programming_languages": ["Pyhton", "Kotlin", "Swift"]
}

xml_file = "MoreDev.xml"
json_file = "MoreDev.json"

"""
/*
* EXERCISE:
* Develop a program capable of creating an XML and JSON file that saves the
* following data (using the correct syntax in each case):
* - Name
* - Age
* - Date of birth
* - List of programming languages
* Show the content of the files.
* Delete the files.
*
* EXTRA DIFFICULTY (optional):
* Using the creation logic of the previous files, create a
* program capable of reading and transforming the data stored in the XML and JSON into the same custom class of your
* language.
* Delete the files.
*/
"""

def create_xml():
    root = xml.Element("Data")

    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item

        else:
            child.text = str(value)
    
    tree = xml.Elementree(root)
    tree.write(xml_file)

create_xml()

with open(xml_file, "r") as xml_data:
    print(xml_data.read())

os.remove(xml_file)

