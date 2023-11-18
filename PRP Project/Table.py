class tableDesign:
    def __init__(self, tableName = "DefaultName", tableAssignment = "None", tableOrders = {}, tableCustomers = 0, preparedBill = False, printedBill = ""):
        self.tableName = tableName
        self.tableAssignment = tableAssignment
        self.tableCustomers = tableCustomers
        self.tableOrders = tableOrders
        self.preparedBill = preparedBill
        self.printedBill = printedBill
tableDesign()