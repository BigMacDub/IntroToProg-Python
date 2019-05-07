#-------------------------------------------------#
# Title: We Got the Func
# Dev:   MWilson
# Date:  May 06, 2019
# ChangeLog: (Who, When, What)
#   MWilson, 05/06/2019, Created Script
#-------------------------------------------------#


#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

objFileName = "ToDo.txt"
strData = ""
dicRow = {}
lstTable = []

#-- Processing --#

class IO(object): #This class contains the processing code/functions for the program

    @staticmethod
    def objFileLoad(objFile): #This loads the data from the 'ToDo.txt' file
        objFile = open(objFileName, "r")
        for line in objFile:
            strData = line.split(",")  # readline() reads a line of the data into 2 elements
            dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
            lstTable.append(dicRow)
        objFile.close()
        return objFile

    @staticmethod
    def objPrint(row): #This prints the data that current exists in the 'ToDo.txt' file
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        return lstTable

    @staticmethod
    def objNew(strTask,strPriority): #This adds a new row of data to the 'ToDo.txt' file
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print("Current Data in table:")
        for dicRow in lstTable:
            print(dicRow)
        return dicRow

    @staticmethod
    def objDel(intRowNumber): #This deletes a row of data from the 'ToDo.txt' file
        blnItemRemoved = False  # Creating a boolean Flag
        intRowNumber = 0
        while (intRowNumber < len(lstTable)):
            if (strKeyToRemove == str(
                    list(dict(lstTable[intRowNumber]).values())[0])):  # the values function creates a list!
                del lstTable[intRowNumber]
                blnItemRemoved = True
            # end if
            intRowNumber += 1
        # end for loop
        # 5b-Update user on the status
        if (blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")
        return blnItemRemoved

    @staticmethod
    def objSave(): #This saves the data as it exists to the save point in the 'ToDo.txt' file
        objFile = open(objFileName, "w")
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()
        return objFile

# Step 1
# When the program starts, load the any data you have
# in a text file called "ToDo.txt" into a python Dictionary

IO.objFileLoad("ToDo.txt")

# Step 2
# Display a menu of choices to the user
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()#adding a new line

    # Step 3
    # Show the current items in the table
    if (strChoice.strip() == '1'):
        print("******* The current items ToDo are: *******")
        IO.objPrint(lstTable)
        print("*******************************************")

    # Step 4
    # Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        strTask = str(input("What is the task? - ")).strip()
        strPriority = str(input("What is the priority? [high|low] - ")).strip()
        IO.objNew(strTask,strPriority)

        #4a Show the current items in the table
        print("******* The current items ToDo are: *******")
        IO.objPrint(lstTable)
        print("*******************************************")
        continue #to show the menu

    # Step 5
    # Remove a new item to the list/Table
    elif(strChoice == '3'):
        #5a-Allow user to indicate which row to delete
        strKeyToRemove = input("Which TASK would you like removed? - ")
        IO.objDel(strKeyToRemove)
        #See objDel function for 5b
        #5c Show the current items in the table
        print("******* The current items ToDo are: *******")
        IO.objPrint(lstTable)
        print("*******************************************")
        continue #to show the menu

    # Step 6
    # Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        #5a Show the current items in the table
        print("******* The current items ToDo are: *******")
        IO.objPrint(lstTable)
        print("*******************************************")
        #5b Ask if they want save that data
        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            IO.objSave()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue #to show the menu

    # Step 7
    # Exit program
    elif (strChoice == '5'):
        break