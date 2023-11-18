from Table import tableDesign

table1 = tableDesign("Table 1")
table2 = tableDesign("Table 2")
table3 = tableDesign("Table 3")
table4 = tableDesign("Table 4")
table5 = tableDesign("Table 5")
table6 = tableDesign("Table 6")
tableList = [table1, table2, table3, table4, table5, table6]

def userLogin():
    global username
    username = input("\nPlease enter username: ")
    password = input("Please enter password: ")
    print()
    for names in loginList:
        if names == username:
            if password == loginList[names]:
                print(f"\nWelcome {username}!")
                landingPage()
                break
            else:
                print("Invalid Password")
                break
    else:
        print("Invalid Username")

def getLogins():
    lineList = {}
    with open("Resources\Login.txt") as f:
        for line in f:
            (key, val) = line.split(",")
            lineList[key] = val.strip("\n")
    return lineList

def getStock():
    lineList = []
    with open("Resources\Stock.txt") as f:
        for line in f:
            (key, val) = line.split(",")
            lineList.append([key, val.strip("\n")])
    return lineList


def landingPage():
    userInput = int(input("\nWhat would you like to do? \n\
                      \n1. Assign Table \
                      \n2. Change customers\
                      \n3. Add to Order\
                      \n4. Prepare Bill\
                      \n5. Complete Sale\
                      \n6. Cashup \
                      \n0. Log out \
                      \nPlease enter your choice: "))
    print()
    if userInput == 1:
        availableTables()
    elif userInput == 2:
        changeCustomers()
    elif userInput == 3:
        addToOrder()
    elif userInput == 4:
        prepareBill()
    elif userInput == 5:
        completeSale()
    elif userInput == 6:
        cashUp()
    elif userInput == 0:
        print("\nLogging Out!!!")
        pass 
    else:
        print("Invalid input!")
        landingPage()
    
def availableTables():
    print("These are the available tables: ")
    for i in tableList:
        if i.tableAssignment == "None":
            print(f"{i.tableName.strip('Table ')}. {i.tableName}")
    userInput = int(input("Please enter your choice, or 0 to cancel: "))
    if(userInput != 0):
        tableList[userInput - 1].tableAssignment = username

        print(f"\n{tableList[userInput - 1].tableName} successfully assigned to {username}")

        addCustomers = input("Do you want to add customers to the table? (y/n): ")
        if addCustomers == "y":
            changeCustomers()
        else:
            landingPage()
    else:
        print("\nCancelling and Returning!!")
        landingPage()

def changeCustomers(): 
    print(f"\nThese are the tables available to {username}")
    for i in tableList:
        if i.tableAssignment == username:
            print(f"{i.tableName.strip('Table ')}. {i.tableName}")


    userInput = int(input("Please select the table you would like to add customers to, or 0 to exit: "))
    while True:
        if tableList[userInput - 1].tableAssignment == username :
            print(f"\nThere are currently {tableList[userInput - 1].tableCustomers} customers assigned to {tableList[userInput-1].tableName}")
            customerNumber = int(input("What is the amount of customers: "))
            tableList[userInput-1].tableCustomers = customerNumber

            print(f"\n{customerNumber} Customers successfully added to {tableList[userInput - 1].tableName}")
            break
        elif (userInput == 0):
            print("\nCancelling and Returning!")
            break
        else:
            print("Invalid selection")
            userInput = int(input("Please select the table you would like to add customers to, 0 to exit: "))

    landingPage()

def addToOrder():
    print(f"\nThese are the tables available to {username}")
    for i in tableList:
        if i.tableAssignment == username:
            print(f"{i.tableName.strip('Table ')}. {i.tableName}")
    
    userInput = int(input("Please select the table you would like to add an order to, or 0 to exit: "))

    while True:
        if tableList[userInput - 1].tableAssignment == username :
            print("\nSelect an item: ")
            counter = 0
            for i in stockList:
                print(f"{counter + 1}. {i[0]} at R{i[1]}")
                counter += 1
            orderSelect = int(input("What item would you like to order: "))
            quantity = int(input(f"How many {stockList[orderSelect - 1][0]}/s would you like to add to the order: "))
            tableList[userInput - 1].tableOrders[stockList[orderSelect - 1][0]] = quantity

            print(f"\n{quantity} {stockList[orderSelect - 1][0]}/s successfully added to {tableList[userInput - 1].tableName}")

            another = input("Would you like to add another order? (y/n): ")
            if another == "n":
                print()
                break

        elif (userInput == 0):
            print("\nCancelling and Returning!")
            break
        else:
            print("Invalid selection")
            userInput = int(input("Please select the table you would like to add an order to, 0 to exit: "))
    landingPage()

def prepareBill():
    global profits
    print(f"\nThese are the tables available to {username}")
    for i in tableList:
        if i.tableAssignment == username:
            print(f"{i.tableName.strip('Table ')}. {i.tableName}")
    
    userInput = int(input("Please select the table you would like to prepare bill for, or 0 to exit: "))

    convertedTableList = list((tableList[userInput - 1].tableOrders).items())
    print (convertedTableList)
    while True:
        if tableList[userInput - 1].tableAssignment == username :
            tableList[userInput - 1].printedBill = f"- - - - - - - - - - - - - - - - - - - - - - - - \
                  \nThe bill for {tableList[userInput - 1].tableName}\n\
                  \n\tItem\tQuantity\tPrice"
            counter = 0
            total = 0
            for i in convertedTableList:
                for x in stockList:
                    if (i[0]) == x[0]:
                        tableList[userInput - 1].printedBill += (f"\n\t{i[0]}\t{i[1]}\tR\t{(int(x[1]) * i[1])}")
                        total += (int(x[1]) * i[1])
                counter+=1    
            tableList[userInput - 1].printedBill += f"\nThe total of you bill was R{total}\
                  \nRecommended Tip is R{round(total*0.1, 2)}\
                  \nGrand Total would be R{total + total*0.1}"
            if (tableList[userInput - 1].tableCustomers > 1):
                  tableList[userInput - 1].printedBill += f"\nYour bill split evenly amongst {tableList[userInput - 1].tableCustomers} would be R{(total + total*0.1)/tableList[userInput - 1].tableCustomers} each"
            tableList[userInput - 1].printedBill += f"\nYou were helped by {username}\
                  \n- - - - - - - - - - - - - - - - - - - - - - - -"
            tableList[userInput - 1].preparedBill = True

            print(tableList[userInput - 1].printedBill)

            profits += total
            break
            
        elif (userInput == 0):
            print("\nCancelling and Returning!")
            break
        else:
            print("Invalid selection")
            userInput = int(input("Please select the table you would like to prepare bill for, 0 to exit: ")) 
    landingPage()

def completeSale():
    print(f"\nThese are the tables available to {username}")
    for i in tableList:
        if i.tableAssignment == username:
            print(f"{i.tableName.strip('Table ')}. {i.tableName}")
    
    userInput = int(input("Please select the table you would like to complete sale for, or 0 to exit: "))

    while True:
        if tableList[userInput - 1].tableAssignment == username :
            if tableList[userInput - 1].preparedBill == True:
                fileName = input("Please enter a file name: ")
                f = open(f"CompletedOrders\{fileName}.txt", "x")
                f.write(tableList[userInput - 1].printedBill)

                print("\nSale was successfully completed")
                tableList[userInput - 1] = tableDesign(f"Table {userInput}")
                break
            else:
                print("\nBill is NOT prepared!")
                break
            
        elif (userInput == 0):
            print("\nCancelling and Returning!")
            break
        else:
            print("Invalid selection")
            userInput = int(input("Please select the table you would like to complete sale for, 0 to exit: "))
    landingPage()

def cashUp():
    global profits
    print(f"\nToday we made R{profits}")
    clearProfits = input("Do you wish to clear todays profit?(y/n): ")
    if clearProfits == "y":
        profits = 0
    landingPage()

#cant add items to order, only in order...
loginList = getLogins()
stockList = getStock()

profits = 0
while True: #main loop for continuous selection until exit is chosen
    
    print("_________________________________________")
    print("Welcome to Highlands Cafe Service!\n" )
    userInput = int(input("1.Login\n2.Exit\nPlease enter your choice: "))
    if (userInput == 1):
        
        userLogin()
    else:
        print("\nThank you for using Highlands Cafe Service!")
        break
    print()
