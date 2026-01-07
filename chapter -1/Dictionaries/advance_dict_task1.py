'''
Docstring for chapter -1.Dictionaries.advance_dict_task1

We have following dictionary containing details

user={
    "user_name":"my_user",
    "password":"test@123",
    "email":"my_user@example.com",
    "address":"123, Main Street, City, Country",
    "country":"Wonderland",
    }

Perform following tasks:
Delete the sensitive information from the dictionary present in a list
sensitive_info = ["password", "email", "address"]
'''

user={
    "user_name":"my_user",
    "password":"test@123",
    "email":"my_user@example.com",
    "address":"123, Main Street, City, Country",
    "country":"Wonderland",
}

sensitive_info = ["password", "email", "address"]

for key in sensitive_info:
    if key in user:
        print(f"Deleting sensitive information: key: {key}, value: {user[key]}")
        user.pop(key)
    else:
        print(f"Key {key} not found in user dictionary.")

print("Updated user dictionary:", user)