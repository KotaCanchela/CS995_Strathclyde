import csv



class Customer:
    """
    Contents the contents of a list of customers
    """

    def __init__(self, ID, firstName, surname):
        self.ID = ID
        self.firstName = firstName
        self.surname = surname
        self.purchaseObjects = []

    def addPurchaseObject(self, purchaseObj):
        self.purchaseObjects.append(purchaseObj)


class Purchase:
    """
    Contains the contents of purchases
    """

    def __init__(self, customerID, itemID, amountPaid):
        self.customerID = customerID
        self.itemID = itemID
        self.amountPaid = amountPaid
        self.dict = {}

    def createDict(self):
        testDict = {}
        customerList = []
        itemList = []
        amountList = []

        for i in self.customerID:
            customerList += i
        for i in self.itemID:
            itemList += i
        for i in self.amountPaid:
            amountList += i



        self.dict = testDict
        return self.dict


def loadCustomerCSV(file_name):
    with open(file_name) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get index number and value for each item in the header_row list

        for index, column_header in enumerate(header_row):
            print(index, column_header)

        # Get ID, first name, and surname from this file
        customer_id, first_name, surname = [], [], []


        for row in reader:
            try:
                customer_identification = row[0]
                first_names = row[1]
                surnames = row[2]
            except ValueError:
                print("Missing data")
            else:
                customer_id.append(customer_identification)
                first_name.append(first_names)
                surname.append(surnames)

    return customer_id, first_name, surname


def loadPurchaseCSV(file_name):
    with open(file_name) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get index number and value for each item in the header_row list

        for index, column_header in enumerate(header_row):
            print(index, column_header)

        # Get ID, first name, and surname from this file
        compareCustomerID, itemID, amountPaid = [], [], []
        # Create Purchase Dictionary
        purchaseDict = {}

        for row in reader:
            try:
                customer_identification = row[0]
                item_identification = row[1]
                paid_value = row[2]
            except ValueError:
                print("Missing data")
            else:
                compareCustomerID.append(customer_identification)
                itemID.append(item_identification)
                amountPaid.append(paid_value)
                purchaseDict[compareCustomerID] = item_identification

    return compareCustomerID, itemID, amountPaid


if __name__ == "__main__":
    purchaseDict = {}
    customer_file_name = "Customers.csv"
    purchase_file_name = "Purchases.csv"

    # Load the customer and purchase CSV files into lists
    customerList = loadCustomerCSV(customer_file_name)
    purchaseList = loadPurchaseCSV(purchase_file_name)

    newCustomer = Customer(customerList[0], customerList[1], customerList[2])
    newPurchase = Purchase(purchaseList[0], purchaseList[1], purchaseList[2])

    newCustomer.addPurchaseObject(newPurchase)

    print(purchaseDict)





