#!/usr/bin/python
import re

idListIndex=0						# Number of IDs
lineNumber=0						# Number of total rows
idList=[]							# ID List
dupelicateList=[]					# List of IDs duplicates


file = open("C:\\Documents\\London Job\\Training\\Python\\ReadingAFile\\TestFile.txt","r") 

# For each row of the file...
for line in file: 
	
	lineNumber=lineNumber+1
	
	# If the row has an ID value, extract the ID
	matchObj = re.match(r'(.*ID:\s)(.*)',line,re.M|re.I)
	
	# If the ID is already in the list...
	if matchObj in idList:
		# Add to the count of duplicates for that ID
		dupelicateList.insert(idListIndex,1)
	elif 		
		# If the ID is not in the list, add it
		idList.insert(idListIndex,matchObj.group(2))
		print("Element: "+str(idList[idListIndex])+" Index: "+str(idListIndex))
		idListIndex=idListIndex+1

	
print("\nFile summary:"
"\nThere were "+str(lineNumber)+" lines in this file."
"\nThere were "+str(idListIndex)+" IDs extracted from this file.")

# Test update to GitHub. Update received.
