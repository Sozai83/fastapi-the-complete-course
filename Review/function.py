def user_dict(f_name, l_name, age):
    dict = {}
    dict["first_name"] = f_name
    dict["last_name"] = l_name
    dict["age"] = age
    ## dict = {"first_name": f_name, "last_name": l_name, "age": age} ## another way to create a dictionary

    return dict

print(user_dict("John", "Doe", 30))
print(user_dict("Jane", "Smith", 25))