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
        print(phone_nums[num_query])
        global contact
        contact = True
    else:
        contact = False
        print(f"You don't have {num_query}'s number.")

num_query = input("Give me a first name and I'll give you their number: ")

phone_num(num_query)

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

# these are just to test the updates
# print(phone_nums[num_query])

# print(phone_nums)

