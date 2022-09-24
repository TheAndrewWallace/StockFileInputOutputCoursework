#json is imported in at start. This will be needed in the main code for the files that the user has chosen to load in.
import json

######################################################################################################################################################################################################################################

#These are the variable that have been decleared to use in the global code.

option = 0								#This will determine which file that it is currently dealing with. This will increase by 1 each time through the loop to move on to next option to get new file from user and deal with it.
accept = True							#Will be set to False if there is an error. Will cause program to stop processing the data if there is an error.
repeat = True							#Once while loop has got all files name and created new version names for them this will be set to False to tell the program to stop while loop.
true = True								#So that the program knows that a true in the data means True.
false = False							#So that the program knows that a false in the data means False.
noreorder = True						#Will be set to False if there has been reorders. If it is note changed then it will output a message telling the user there has been no reorders.
stockname = None						#User inputs name of file they want to load for the stock It is assigned to this variable as a string.
stockfile = None						#The file the user wants to load for the stock is opened and assigned to this value.
filename = None							#File names are assigned to this whilst they are dealth with and are used in the versionupdate function.
salesname = None						#User inputs name of file they want to load for the sales file. It is assigned to this variable as a string.
salesfile = None						#The file the user want to load for the sales is opened and assigned to this value.
reordername = None						#User inputs name of file they want to load for the reorder file. It is assigned to this variable as a string.
loadedstock = None						#json is used to load the stock and then it is assigned to this variable.
loadedsales = None						#json is used to load the sales and then it is assigned to this variable.
loadedreorder = None					#json is used to load the reorder and then it is assigned to this variable.
reorderfile = None						#reorder file is opened and assigned to this
salesItemDict = None					#For the items sold
item = None								#For the item
numbersold = None						#The number that has been sold and needs to be moved to the shelf is assigned to this variable
createstockreport = None				#The new file for stock is created and opened to be written to. It is assigned to this variable.
createreorderreport = None				#The new file for reordering is created and opened to be written to. It is assigned to this variable.
newstockname = None						#The updated stock file name to the next version is assigned to this value. It will be used to create the new stock file.
newreordername = None					#The updated reorder file name to the next version is assigned to this value. It will be used to create the new reorder file.
salesreport = ("\n#############################\n#   Shelf Stocking Report   #\n#############################\n")				#All shelf restocking values are added to this as a string. This allows report to be printed seperate from reordering report.
reorderreport = ("################################\n#   Stock Re-ordering Report   #\n################################\n")		#All reordering values are added to this as a string. This allows report to be printed seperate from shelf restocking values. 

######################################################################################################################################################################################################################################

#####################################################################################################################################################################################
#Function - 		versionupdate																																					#
#Description - 		This function will check that the file name is in the correct format.																							#
#					This function will create a new file name for the new version of the files. This will be what the new files will be called. It									#
#					will be 1 version higher than the version that has been input into the program.																					#
#Input variable -	Will take the filename variable in that contains the string of what the file is called that the user has chosen.												#
#Output variables - Outputs the newstockname variable that contains a string of what the new stock file will be called. Will be 1 version higher than that entered.					#
#					Outputs the newreordername variable that contains a string of what the new re-stock file will be called. Will be 1 version higher than that entered.			#
#					Outputs accept variable to determine if it was valid or if the program should exit. If there was an error with the name format, this will be set to False.		#
#					Outputs repeat. Will be set to False after final file has had a new name created to tell the program to no longer continue while loop in main code.				#
#####################################################################################################################################################################################
def versionupdate(x):

	global accept				#Global so it can change it to False if there is an error which stops the rest of the program from running.
	global repeat				#Global so it can tell the program to stop the while loop once all files that need to be processed have been.
	global newstockname			#Hold new reorder stock name as a string.
	global newreordername		#Hold new re order file name as a string.
	vstart = None				#Used to find what comes after the - symbol.
	vend = None					#Used to find what comes before the .dat.
	version = 0					#Hold the version.
	filenamestart = None		#Used to hold the start of the file name before the version.
	filenameend = None			#Used to hold the end of the file name after the version
	newfilename = None			#Contains the new file name.



	#If the user has entered the name of file has a name that does not allow for versioning, this try will stop the program from crashing.
	try:
		#Finds what is 1 ahead of the - symbol and what is the . symbol.
		vstart = x.find("-") + 1
		vend = x.find(".")
		#If condition then checks to see if the vstart and vend are both the same. If they are that means the user has entered a - symbol but no number after it. if condition used because it should always run if condition is met.
		if (vstart == vend):
			#The program will set the version to 0 if this happens.
			version = 0
		#else used because if the if condition is not met then this should always run. Will run if the user has put a number after - and before .dat
		else:
			#Gets the file version as an integer
			version = int(filename[vstart:vend])
		
		#New file name is created by getting the start of the file name (anything beofore version number) and the end of the file name (anything after version number)
		#Updating the version number by 1 so it is the next version.
		#Adding all 3 together as and assigning it to a variable to be used to create a file in the main code.
		filenamestart = x[0:vstart]
		filenameend = x[vend:]
		version = version + 1
		newfilename = filenamestart + str(version) + filenameend
		
	#If there is an error with the naming format so that it does not allow for creating a new version with new number
	except Exception:
		#This will print an error message explaining the error to the user. Will cause a bell sound to play.
		#accept is set to False to stop the program from continuing. repeat is also set to False to allow it to stop the loop so the program can exit.
		print ("Error: File named in invalid format. (Must be in valid format to allow for versioning).\a")
		accept = False
		repeat = False
	
	
	#An if has been used because if the option = 0 then the it must be inputing a stock file name. accept must also = True as the program should not continue if there has been any previous errors.
	if ((option == 0) and (accept == True)):
		#Assigns the newfile name to the newstockname so that it can be used later to name the new file that is output.
		newstockname = newfilename
		
	#If it is not a 0 then it could be a 2 which is why an elif has been used. elif has been used rather than an else because it could still possibly be a 1 which is used for the sales file. accept must also = True as the program should not continue if there has been any previous errors.
	elif ((option == 2) and (accept == True)):
		
		#Assigns the new file name to the newreordername so that it can be used later to name the new file that is output. Also sets repeat to False to stop the while loop in main code.
		newreordername = newfilename
		repeat = False
			




#	This gets file names from the user and checks they exit. Also uses a function to check if they are in the correct format for versioning and also updates them.
###################
#This gets the data from the local directory and checks if they exist and can be opened.
while (repeat == True):
	

	#If used because it should always run this code if the condition are met. If option = 0 then it must be dealing with the stock file.
	if (option == 0):
		
		#Prints instuctions to the user about how to enter a file name and what is considered valid.
		print ("Enter file name. Name must include - symbol before number at end or .dat to allow for versioning. Example: stock-1.dat\nSales file does not require - symbol\n")	
		
		#Gets stock file name from the user and assigns it to variable as a string.
		stockname = str(input("\nEnter a valid file name for stock file: "))
		
		#This try is used to check if the stock file can be found and if it can be opened. If it can then it is opened and the code continues.
		try:
			#This opens to file the user has entered to read. It is only needed to be read because it is a different version that will be edited and output to the user.
			stockfile = open (stockname, "r")
			
		#If the file could not be found this code is used.
		except Exception:
			#Prints an error message explaining the issue to the user. Will also cause a sound. Also changes accept and repeat to False to stop the program from continuing. This allows the program to exit.
			print ("Error: File does not exist or could not be found.\a")
			accept = False
			repeat = False
		
		#else used because if the except was not used then it should always set the filename to the stockname so that it can be used in the function
		else:
			#Sets the file name to the same as the stock name to be used in the function.
			filename = stockname
	
	#elif used because it should not run if the previous one already has. If option = 1 then it must be dealing with the sales file.
	elif (option == 1):
	
		#Gets sales file name from the user and assigns it to variable as a string.
		salesname = str(input("\nEnter a valid file name for sales file: "))
		
		#This try is used to check if the sales file can be found and if it can be opened. If it can then it is opened and the code continues.
		try:
			#opens the file the user has entered to read. It only needs to be read as it does not need to be edited.
			salesfile = open (salesname, "r")
			
		#If the file could not be found then this code is used.
		except Exception:
			#Prints an error message explaining the issue to the user. Will also cause a sound. Also changes accept and repeat to False to stop the program from continuing. This allows the program to exit.
			print ("Error: File does not exist or has invalid naming format.\a")
			accept = False
			repeat = False
			
		#else used because if the except was not used then it should always set the filename to the salesname.
		else:
			#sets the file name to the same as the sales name.
			filename = salesname
		
	#elif used because it should not run if the previous one already has. If option = 2 then it must be dealing with the reorder file.
	elif (option == 2):
		
		#Get reorder file name from the user and assigns it to variable as a string.
		reordername = str(input("\nEnter a valid file name for reorder file: "))
		
		#This is used to check if the reorder file can be found and if it can be opened. If it can then it is opened and the code continues.
		try:
			#opens the file the user has entered to read. It only needs to be read as it does not need to be edited.
			reorderfile = open (reordername, "r")
			
		#If the file could not be found then this code is used.
		except Exception:
			#Prints an error message explaing the issue to the user. Will also cause a sound. Also changes accept and repeat to False to stop then program from continuing. This allows the program to exit.
			print ("Error: File does not exist or has invalid naming format.\a")
			accept = False
			repeat = False
			
		#else used because if the xcept was not used then it should always set the filename to the reordername.
		else:
			#sets the filename to the same as in reordername so it can be used in the function to get a new version number and name.
			filename = reordername
	
	#If non of the if and two elif statement condition are met then option must have reached 3 and the loop has completed what it needed to.
	else:
		#If there is an error these values are set to False. Repeat will stop the loop and accept will prevent the program continuing any further.
		accept = False
		repeat = False
		
		
	#Should always run if condition are met. If accept = True then files must have been able to load. option should not equal 1 because sales do not have to have a version update as their is no update file to create for them.	
	if (accept == True) and (option != 1):
		#Runs the function using the filename that the user has entered.
		versionupdate(filename)
	
	#1 is added to option to allow it to repeat and go onto the next option to get the next file name from the user and deal with it.
	option = (option + 1)

#This load the files with json once they have been checked to exist.
if (accept == True):

	#Checks to see if the file can be loaded with json
	try:
		#Will use json to load files and assign them to variables.
		loadedstock = json.load(stockfile)
		loadedsales = json.load(salesfile)
		loadedreorder = json.load(reorderfile)

	#If it cant then this will run
	except Exception:
		#prints an error message and sets accept to False to stop program from continuing.
		print("Error: Files entered could not be loaded. They may be in incorrect format.")
		accept = False

#if used because it should always check that there have been no issues with the code.
if (accept == True):

	#Checks if the files that have been loaded in can be used or if it will crash the system.
	try:
		
		#for loop causes the loop to repeat until everything is checked. Two for loops has been used here.
		for salesItemDict in loadedsales:
			#Another for loop has been used to get it to repeat until all items in loaded sales have been checked and processed.
			for item in salesItemDict:
				#Adds the item code to the sales report.
				salesreport = (salesreport + "Item code: " + item + "\n")
				
				#Assigns the number sold to a variable so it can be used to calculate the final stock
				numbersold = salesItemDict[item]
				
				#find the amount of stock that corrosponds with a key and reduces it by the number sold as this will now be moved to the warehouse.
				loadedstock[item] = (loadedstock[item] - numbersold)
				#if the storage is below 0 then that amount can not be moved to the shelves because it does not exist. If it is below 0 this code is used.
				if (loadedstock[item] < 0):
					#if this code is used then loadedstock must be a minus so adding it to number sold will result in the correct ammount.
					numbersold = (numbersold + loadedstock[item])
					#Also sets loadedstock corrosponding item to 0 because it can not be a minus number as the product would simply not exist to send to the shelves.
					loadedstock[item] = 0
					
				#Add the amount that need to be moved to the sheld onto the sales report.
				salesreport = (salesreport + "Items to be moved to shelf: " + str(numbersold) + "\n")
				
	
				#if because it should always run if the conditions are met. if the amount left is equal or lower than the reorder value and it has not already been reordered then this should pass.
				if ((loadedstock[item]) <= (loadedreorder[item][0])) and ((loadedreorder[item][1]) == False):
					#The item is added to the reorder report. Value is set to True to say that it has been reordered. noreorder set to False to prevent it printing no reorder message
					reorderreport = (reorderreport + "Item code: " + item + "\n")
					loadedreorder[item][1] = (true)
					noreorder = False
	
	#If an error was caused this should pass
	except Exception:
		#prints an error message to the user and sets accept to False to prevent the code from running any further.
		print ("Error: Data was not valid. Ensure correct files have been loaded to correct categories.\a")
		accept = False

#if there have been no errors up to this stage or accept has not been set to False then this should always pass. 
if (accept == True):

	#This will print the sales report and reorder report sequentially rather than having them printed combined. This was specified as the correct way to output the data.
	print (salesreport)
	print (reorderreport)
	
	#If there have been no reorderes then this should pass
	if (noreorder == True):
		#If there have been no reorder then this should print to tell the user that there have been no reorders.
		print ("No items were required to be reordered")


	#################################################################################################
	#This creates a new file with the new version name and opens it to be wrote to.					#
	#The code also changes the list to a string and then replaces any apostrophies with quotes.		#
	#This ensures it is output in correct format.													#
	#The new stock report is then wrote to the new file.											#
	#################################################################################################
	createstockreport = open ((newstockname), "w")
	loadedstock = str(loadedstock)
	loadedstock = loadedstock.replace("'", '"')
	createstockreport.write (loadedstock)
	
	#################################################################################################
	#This creates a new file with the new version anme and opens it to be wrote to.					#
	#The code also changes the list to a string and then replaces any apostrophies with quotes.		#
	#This ensure it is output in correct format and can be used again the next time.				#
	#Also replaces True and False so that part is also in the correct format.						#
	#The new reorder report i then wrote to the new file.											#
	#################################################################################################
	createreorderreport = open ((newreordername), "w")
	loadedreorder = str(loadedreorder)
	loadedreorder = loadedreorder.replace("'", '"')
	loadedreorder = loadedreorder.replace("True", "true")
	loadedreorder = loadedreorder.replace("False", "false")
	createreorderreport.write (loadedreorder)
	