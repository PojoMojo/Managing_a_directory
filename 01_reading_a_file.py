#!/usr/bin/python

# Script written by John
# This script is intended to help manage dictionary files by looking for duplicate 'ID's
# The script can: read a file, identify IDs, identify duplicate ID's and the line they are on, provide a summary
# Next steps:
# 1) allow the user to remove the duplicates/duplicate sections (inc progress indicator for large files and report)
# 2) perform other formatting checks on the file
#

from shutil import copyfile         # Used for backup
import os                           # User for filename and ext
import re                           # Used for regex
import time                         # User for time/stamping



idExtracted = 0                     # Number of IDs identified
idListIndex = 0                     # Number of unique IDs
dupeIdListIndex = 0                 # Number of duplicate IDs
lineNumber = 0                      # Number of total rows

loadedFile = []                     # This is the file, loaded line by line
idList = []                         # List of ID/Line/Count of dupes
dupeIdList = []                     # List of duplicates/line references
dupeLineIdList = []                 # List of duplicates/line references

source = "C:\\Documents\\London Job\\Training\\Python\\ReadingAFile\\TestFile.txt"

# Making a backup, just in case...
basename = os.path.basename(source)
filename, file_extension = os.path.splitext(basename)
backupFilename = filename+"-Backup-"+time.strftime("%Y%m%d-%H%M%S")+file_extension
backupFile = "C:\\Documents\\London Job\\Training\\Python\\ReadingAFile\\"+backupFilename
copyfile(source, backupFile)


file = open(source, "r")            # Load the file

# For each row of the file...
for line in file:

    #loadedFile[lineNumber] = line

    # Check the line; if it has an ID value, extract the ID
    matchObj = re.match(r'(.*ID:\s)(.*)', line, re.M | re.I)

    # If there is an ID, do some checks
    if matchObj:

        print("ID: "+str(matchObj.group(2))+" Line: "+str(lineNumber))

        # If the ID is already in the list...
        if matchObj.group(2) in idList:

            # Print a warning of duplicate
            #print("Duplicate identified: "+str(matchObj.group(2))+" on line: "+str(lineNumber))

            # If a duplicate ID, add the ID and the line where it was found, to the relevant lists
            dupeIdList.insert(dupeIdListIndex, matchObj.group(2))
            dupeLineIdList.insert(dupeIdListIndex, lineNumber)

            # A dupelicate ID was found - the counter must be incremented
            dupeIdListIndex += 1

        else:
            # If ID is new, add it
            idList.insert(idListIndex, matchObj.group(2))
            idListIndex += 1

        # An ID was extracted
        idExtracted += 1

    lineNumber += 1

print("\nFile summary:"
      "\nThere were " + str(lineNumber) + " lines in this file."
      "\nThere were " + str(idExtracted) + " IDs in this file."                                    
      "\nThere were " + str(idExtracted-idListIndex) + " duplicate IDs extracted from this file.")

if dupeIdListIndex>0:
    print("\nThe following ID's were found to be duplicates:")

    for a in range(dupeIdListIndex):
        print("Duplicated ID: "+str(dupeIdList[a])+" found on line: "+str(dupeLineIdList[a]))

else: print("\nNo duplicate detail to be printed.\n")

