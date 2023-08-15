# message = input("tell me something, and i will repeat it back to you: ")
# print(message)

prompt = "\ntell me something, and i will repeat it back to you: "
prompt += "\nenter 'quit' to end the program. "

message = ""

# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)

while active: 
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)