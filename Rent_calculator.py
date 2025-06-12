"""Input"""

# What we need as input from user
# Total rent
# Electricity units spend
# Charge per unit
# Total food ordered for snacking
# No. of Persons in hostel

"""Output"""

# Total payment of individual 

print(" WELCOME TO RENT CALCULATOR per head.")

flat_rent = float(input("Enter your Flat/Hostel rent : "))
food = int(input("Enter the amount of food ordered : "))
electricity_spend=int(input(" Enter the total of electricty spend : "))

# Remember

charge_per_unit = int(input("Enter the charge per unit : "))
no_of_persons = int(input("Enter the no. of people living in hostel/room : "))


total_bill = ((flat_rent + food + (electricity_spend*charge_per_unit))/no_of_persons)

print(f"The contribution of the total bill per head is = {total_bill} ")
print(" PAY SOON !!!")