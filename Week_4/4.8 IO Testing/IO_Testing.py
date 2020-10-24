import csv


class Customer:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.purchases = []

    def __repr__(self):
        return f"Customer information:\n\tID: {self.id}\nFirst name: {self.first_name}\nLast_name: {self.last_name}"

    def amountPaid(self):
        total = 0

        for purchase in self.purchases:
            total += float(purchase.paidAmount)

        # Reduce to 2 decimal places
        return round(total, 2)

    def getPurchase(self):
        userPurchase = f"{self.first_name} {self.last_name} bought: "
        for purchase in self.purchases:
            userPurchase += f"\n\titem #{purchase.itemId} for £{purchase.paidAmount}"

        return userPurchase



class Purchase:
    def __init__(self, customerID, itemId, paidAmount):
        self.customerID = customerID
        self.itemId = itemId
        self.paidAmount = paidAmount

    def __repr__(self):
        return f"Customer #{self.customerID} bought item number {self.itemId} for £{float(self.paidAmount)}"


def loadCustomerCSV(fileNameCustomers, fileNamePurchases):
    customerList = []
    purchases = loadPurchaseCSV(fileNamePurchases)
    i = 0
    customerFile = open(fileNameCustomers, "r", newline='')
    readCustomers = csv.reader(customerFile, delimiter=',', quotechar='"')

    for row in readCustomers:
        if i != 0:
            customer = Customer(row[0], row[1], row[2])
            customerList.append(customer)

            for purchase in purchases:
                if purchase.customerID == customer.id:
                    customer.purchases.append(purchase)
        i = 1

    return customerList

def loadPurchaseCSV(file_name):
    purchaseList = []
    with open(file_name) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get index number and value for each item in the header_row list

        for index, column_header in enumerate(header_row):
            print(index, column_header)

        # Get ID, first name, and surname from this file
        compareCustomerID, itemID, amountPaid = [], [], []

        for row in reader:
            try:
                customer_identification = row[0]
                item_identification = row[1]
                paid_value = row[2]
            except ValueError:
                print("Missing data")
            else:
                purchaseList.append(Purchase(customer_identification, item_identification, paid_value))

    return purchaseList


if __name__ == "__main__":
    customers = loadCustomerCSV(
        "Customers.csv", "Purchases.csv")

    for customer in customers:
        print(customer.getPurchase())
        print("\tTotal: " + str(customer.amountPaid()))
        print("-")

