def show_messages(message):
    for i in message:
        print(i.title())


def send_messages(messages,sent_messages):
    while messages:
        msg = messages.pop()
        print(f"{msg.title()}")
        sent_messages.append(msg)

messages = ['halo', 'hola', 'hallo', 'selamat']
sent_msg = []


show_messages(messages)
send_messages(messages[:],sent_msg)
