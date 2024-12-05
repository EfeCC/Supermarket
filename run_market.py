from main import *
import time
print("""
************************

WELCOME TO THE SUPERMARKET APP

Products:
1-Show Products
2-Question Products
3-Add Product
4-Delete Product
5-Upgrade Consumption Date
6-Upgrade Size
7-Press 'q' to quit

************************
""")

marketLibrary = MarketLibrary()

while True:
    choice = input("Select your choice: ")
    if choice  == 'q':
        print("See you again...")
        time.sleep(2)
        break
    elif choice == '1':
        marketLibrary.show_products()
    elif choice == '2':
        name = input("Which product do you want to quest ? ")
        print("Product is questioning...")
        time.sleep(2)
        marketLibrary.question_products(name)

    elif choice == '3':
        name = input("Enter name: ")
        producer = input("Enter producer: ")
        price = int(input("Enter price: "))
        product_date = int(input("Enter product year: "))
        consumption_date = int(input("Enter consumption date: "))
        size = input("Enter size: ")
        new_product = Market(name,producer,price,product_date,consumption_date,size)
        print("Product adding...")
        time.sleep(2)
        marketLibrary.add_product(new_product)
        print("Product added.")
    elif choice == '4':
        name = input("Which product you want to delete ?")
        answer = input("Are you sure that you want to delete ?(Y/N)")

        if answer == 'Y':
            print("Product is deleting...")
            time.sleep(2)
            marketLibrary.delete_product(name)
            print("Deleted.")
        elif answer == 'N':
            print("Delete canceled.")
            continue

    elif choice == '5':
        name = input("Enter product name that you want to upgrade date: ")
        print("Upgrading...")
        time.sleep(2)
        marketLibrary.upgrade_year(name)
        print("Upgraded.")

    elif choice == '6':
        #market = Market(name,producer,price,product_date,consumption_date,size)
        name = input("Which product that you want to upgrade size? ")
        new_size = input("Enter new size of product: ")

        print("Upgrading...")
        time.sleep(2)
        marketLibrary.upgrade_size(new_size,name)
        print(f"The new size of product is: {new_size}")
