phone_nums = {
    "Anna": "525-454-5532",
    "Jessica": "638-333-3200",
    "Kairah": "510-334-9929",
    "Francine": "510-444-0008",
    "Farah": "+52-455-34590"
}

def phone_num(num_query):
    if num_query in phone_nums:
        print(phone_nums[num_query])
    else:
        print(f"You don't have {num_query}'s number.")

num_query = input("Give me a first name and I'll give you their number: ")

phone_num(num_query)




# turned these two if statements into the phone_num function above:

# if "Kairah" in phone_nums:
#     print(phone_nums["Kairah"])

# else:
#     print("You don't have Kairah's number.")

# if "Jenny" in phone_nums:
#     print(phone_nums["Jenny"])
    
# else:
#     print("You don't have Jenny's number.")