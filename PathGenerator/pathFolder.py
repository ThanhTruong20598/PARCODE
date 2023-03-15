import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

#Input Path Of The Project
print "Add Path of the project:"
sourcelink = raw_input(">")

#Include path 
startpath_XCP = sourcelink + '\\RBP\\GEN6\\SW\\CUS\\ASW\\SRV_PAR\\MAZDA_J30_4M_F_V_S'
startpath_WOX = sourcelink + '\\RBP\\GEN6\\SW\\CUS\\ASW\\SRV_PAR\\MAZDA_J30_4M_F_V_S_WOX'
startpath_xmlFile_XCP = sourcelink + '\\RBP\\GEN6\\SYS\\CUS\\CAL_NVM_PAR\\SHARCC\\SHARCC_XML\\Mazda_J30_4M'
startpath_xmlFile_WOX = sourcelink + '\\RBP\\GEN6\\SYS\\CUS\\CAL_NVM_PAR\\SHARCC\\SHARCC_XML\\Mazda_J30_4M_WOX'

def export_file_paths_XCP(startpath_XCP, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(startpath_XCP):
            for file in files:
                f.write(os.path.join(root, file) + '\n')

def export_file_paths_WOX(startpath_WOX, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(startpath_WOX):
            for file in files:
                f.write(os.path.join(root, file) + '\n')              

def export_xmlfile_paths_XCP(startpath_xmlFile_XCP, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(startpath_xmlFile_XCP):
            for file in files:
                f.write(os.path.join(root, file) + '\n')

def export_xmlfile_paths_WOX(startpath_xmlFile_WOX, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(startpath_xmlFile_WOX):
            for file in files:
                f.write(os.path.join(root, file) + '\n')
#*******************************************************
#*******************************************************                
#***************Export Output File**********************
#*******************************************************
#*******************************************************

#Export Output File Parcode XCP
print('Successfully Generated Path File Of Parcode XCP')
export_file_paths_XCP(startpath_XCP, 'pathFiles_XCP.txt')

#Export Output File Parcode WOX
print('Successfully Generated Path File Of Parcode WOX ')
export_file_paths_WOX(startpath_WOX, 'pathFiles_WOX.txt')
 
#Export Output xml File XCP
print('Successfully Generated Path File Of xml File XCP')
export_file_paths_XCP(startpath_xmlFile_XCP, 'xmlFiles_XCP.txt')

#Export Output xml File WOX 
print('Successfully Generated Path File Of xml File WOX ')
export_file_paths_WOX(startpath_xmlFile_WOX, 'xmlFiles_WOX.txt')


#*******************************************************
#*******************************************************                
#***************Export Full Path File*******************
#*******************************************************
#*******************************************************

def fullPathFile(input_files, output_file):
    with open(output_file, 'w') as outfile:
        for input_file in input_files:
            with open(input_file, 'r') as infile:
                outfile.write(infile.read())

# Input txt file and Create Name of the file
input_files = ['pathFiles_XCP.txt', 'pathFiles_WOX.txt', 'xmlFiles_XCP.txt', 'xmlFiles_WOX.txt']
output_file = 'fullPathFile.txt'
print('*************************************************')
print('Successfully Generated Full Path File ')
fullPathFile(input_files, output_file)


#*******************************************************
#*******************************************************                
#***************Export Modified Path File***************
#*******************************************************
#*******************************************************
input_file = "fullPathFile.txt"
modifiedPathFile = "modifiedPathFile.txt"

# Open the file containing the file paths
with open('fullPathFile.txt', 'r') as f:
    # Read the file paths into a list
    file_paths = f.readlines()

# Remove the path you want
prefix = sourcelink
new_file_paths = [path.replace(prefix, '') for path in file_paths]

# Write the updated file paths to the new file
with open('modifiedPathFile.txt', 'w') as f:
    f.writelines(new_file_paths)   
print('Successfully Generated Modified Path File ')

