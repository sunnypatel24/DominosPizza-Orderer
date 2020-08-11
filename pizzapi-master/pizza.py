from pizzapi import *

def main():
    intro()
    customer = get_customer_info()
    address = get_address()
    order = get_order(address, customer)
    card = get_card()
    place_order(order, card)


def intro():
    print("Welcome! This is a program that allows you to order from your nearest Dominos Pizza store. You will be asked to enter in personal information, such as name, address, and phone number, as well as credit card information for when you pay for the order.\n")
    print("You can search the menu and add or remove items as you desire. When you are done, you can move on to payment when you are ready.\n")


def get_customer_info():
    valid_info = True
    while valid_info:
        try:
            enter_info = input("Please enter your full information, seperated by commas (first name, last name, email, phone number): ")
            full_info = enter_info.split(",")
            fname = full_info[0]
            lname = full_info[1]
            email = full_info[2]
            phone = full_info[3]
            customer = Customer(fname, lname, email, phone)
            break
        except IndexError:
            print()
            print("Invalid input. Please type all information in the required format.\n")
    print("\n")
    return customer


def get_address():
    valid_address = True
    while valid_address:
        try:
            enter_address = input("Please enter your full address (street, city, state, zip code): ")
            full_address = enter_address.split(",")
            street = full_address[0]
            city = full_address[1]
            state = full_address[2]
            zip_code = full_address[3]
            address = Address(street, city, state, zip_code)
            break
        except IndexError:
            print("Invalid input. Please type all information in the required format.\n")
    print("\n")
    return address


def get_order(address, customer):
    store = address.closest_store()
    menu = store.get_menu()
    order = Order(store, customer, address)
    search_menu = input("Would you like to search the menu for an item? Enter 'y' for yes or 'n' for no: ")
    current_order = []
    print("\n")
    while (search_menu == 'y'):
        item = input("Enter the name of the item you wish to look at: ")
        item = item.title()
        print("\n")
        menu.search(Name=item)
        code = input("Please enter the product code of the item you wish to add to your order. Press enter if you do not wish to add anything or if no products appeared (meaning that the searched product is not on the menu): ")
        if (code != ""):
            order.add_item(code)
            current_order.append(code)
        print("Your current order is the following: ")
        for item in current_order:
            print(item)
        print("\n")
        search_menu = input("Would you like to search the menu for an item? Enter 'y' for yes or 'n' for no: ")
    print("\n")
    remove = input("Would you like to remove anything from your order? Enter 'y' for yes or 'n' for no: ")
    while (remove == 'y'):
        print("\n")
        delete_code = input("Please enter the product code of the item you want to remove from your order: ")
        order.remove_item(delete_code)
        print("\n")
        remove = input("Would you like to remove anything from your order? Enter 'y' for yes or 'n' for no: ")
        print("\n")
    return order


def get_card():
    valid_card = True
    while valid_card:
        try:
            get_payment_info = input("Please enter the required credit card information (card number, expiration date w/o backslash, cvv, zip code): ")
            full_card = get_payment_info.split(",")
            number = full_card[0]
            expiration = full_card[1]
            cvv = full_card[2]
            zip_code = full_card[3]
            card = PaymentObject(number, expiration, cvv, zip_code)
            break
        except IndexError:
            print("Invalid input. Please type all information in the required format.\n")
    print("\n")
    return card


def place_order(order, card):
    confirm = input("Confirm order placement? Enter 'y' to place your order: ")
    if (confirm == 'y'):
        order.place(card)
        print("\n")
        print("Order has been placed!")
    else:
        print("\n")
        print("Order has been cancelled.")


main()