print("====================================")                      
print("   SMART DISCOUNT CALCULATOR   ")
print("====================================")

print('\nwelcome to the discount calculator 😊')

print('\nPlease choose from one of the discount type:')
print("1. Percentage Discount")
print("2. Price-Based Discount")
print("3. Customer Discount")
print("4. Flat Discount")
print("5. Exit")
print("====================================")


choice = 0

while choice != 5:

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n----- Percentage Discount -----")

        price = float(input("Enter Product Price:"))
        discount = float(input("Enter Discount (%): "))

        discount_amount = (price * discount) / 100
        final_price = (price - discount_amount)
        print("Saved =", discount_amount)
        print("Final Price =", final_price)

    elif choice == 2:
        print("\n-----Price Based Discount-----")

        price = float(input("Enter Product Price:"))

        if price < 500:
            print("Sorry No Discount !! , buy products priced greater then 500")
            print("Saved = 0")
            print(f"final price = {price}")
        elif price > 500 :
            discount = float(input("Enter Discount (%): "))

            discount_amount = (price * discount) / 100
            final_price = (price - discount_amount)
            print("Saved =", discount_amount)
            print("Final Price =", final_price)


    elif choice == 3:
        print("\n-----Customer Discount-----")
        customer = ['student' , 'general' , 'premium']

        customer = str(input("Enter your customer type: a) student b) general c) premium"))

        if customer == "student" or "general" or "premium":
           price = float(input("Enter Product Price:"))
           discount = float(input("Enter  your customer discount (%): "))

           discount_amount = (price * discount) / 100
           final_price = (price - discount_amount)
           print("Saved =", discount_amount)
           print("Final Price =", final_price)
        
        elif customer != "student" or "general" or "premium" :
            print("Invalid input ! , please enter customer type")

    elif choice == 4:
        print("\n-----Flat Discount-----")
        price = float(input("Enter Product Price:"))
        discount = float(input("Enter Discount (price):"))

        discount_amount = (discount)
        final_price = (price-discount_amount)
        print("Saved =", discount_amount)
        print("Final Price =", final_price)


    elif choice == 5:
        print("\nThank you for using Smart Discount Calculator!")

    else:
        print("\nInvalid Choice!") 

