import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

#*******************************************************************************
#*******************************************************************************
#*****************************Generate Check OUT XML****************************
#*******************************************************************************
#*******************************************************************************
# Read the list of file paths from a text file
with open('modifiedPathFile.txt', 'r') as f:
    file_paths = [line.strip() for line in f.readlines()]

# Create the XML file and add the root element
root = ET.Element('files')

# Loop through the file paths and add an element for each file
for file_path in file_paths:
    file_name = os.path.basename(file_path)
    file_element = ET.SubElement(root, 'file', {'cmd': 'si co', ' cpid' : ' --cpid='+ '' , 'Macro': ' --forceConfirm=Yes' , 'path': file_path , 'name': file_name})

# Create the XML string with pretty formatting
xml_string = minidom.parseString(ET.tostring(root)).toprettyxml(indent='    ')

# Write the XML string to disk
with open('xmlPathGenerator_CheckOut.xml', 'w') as f:
    f.write(xml_string)
print('Successfully Generated xml File for Check Out')


#*******************************************************************************
#*******************************************************************************
#*****************************Generate Check IN XML*****************************
#*******************************************************************************
#*******************************************************************************
# Read the list of file paths from a text file
with open('modifiedPathFile.txt', 'r') as f:
    file_paths = [line.strip() for line in f.readlines()]

# Create the XML file and add the root element
root = ET.Element('files')

# Loop through the file paths and add an element for each file
for file_path in file_paths:
    file_name = os.path.basename(file_path)
    file_element = ET.SubElement(root, 'file', {'cmd': 'si ci', ' cpid' : ' --cpid=' + '' , 'label' : ' --label="Check In ParCode"',  'description' : ' --description="Check In ParCode" ', 'Macro': ' --forceConfirm=Yes', 'path': file_path, 'name': file_name})

# Create the XML string with pretty formatting
xml_string = minidom.parseString(ET.tostring(root)).toprettyxml(indent='    ')

# Write the XML string to disk
with open('xmlPathGenerator_CheckIn.xml', 'w') as f:
    f.write(xml_string)
print('Successfully Generated xml File for Check IN')



