# This program gives the user a phone number from the phonebook, if the contact exists. 
# It also updates the number, if the user desires.

phone_nums = {
    "Anna": "525-454-5532",
    "Jessica": "638-333-3200",
    "Kairah": "510-334-9929",
    "Francine": "510-444-0008",
    "Farah": "+52-455-34590"
}

contact = False

def phone_num(num_query):
    if num_query in phone_nums:
        print(f"{num_query}'s number: {phone_nums[num_query]}")
        global contact
        contact = True
    else:
        contact = False
        print(f"You don't have {num_query}'s number.")

num_query = input("Give me a first name and I'll give you their number: ")

phone_num(num_query)

# Update the phone number?

def update_num(change_query):
    phone_nums[num_query] = change_query    

if contact == True:
    yn = input("Would you like to update their phone number? yes/no? ")
else:
    yn = "no"

if yn == "yes":
    change_query = input("What is their new number? ")
    update_num(change_query)
else:
    if contact == True:
        print("Ok, let's keep the current number.")

# add a contact:

def add_contact(new_name, new_number):
    phone_nums[new_name] = new_number    

yn = input("Would you like to add a new contact? yes/no? ")

if yn == "yes":
    global new_name
    global new_number
    new_name = input("What is their name? ")
    unique = False
    while unique == False:
        if new_name in phone_nums:
            print("You already have that contact.")
            new_name = input("Choose a unique name by adding other characters or choose a nick name: ")
        else:
            new_number = input("What's their number? ")
            add_contact(new_name, new_number)
            unique = True
else:
    print("Ok. Have a lovely day.")

# test:
# print(phone_nums)

