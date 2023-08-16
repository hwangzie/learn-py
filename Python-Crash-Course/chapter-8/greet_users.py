def greet_users(names):
    """print a simple greeting to each user in the list"""
    for name in names:
        msg = f"hello {name.title()}!"
        print(msg)

usernames = ['ana', 'budd', 'leo']
greet_users(usernames)
