import RSA, Interface, Chatroom

mode, ip, port, keysize, name = Interface.get_args()

match mode:
    case "re-key": 
        print("Generating keys...")
        if keysize == None: new_keys = RSA.re_key(name)
        else: new_keys = RSA.re_key(name, size=keysize)
        print("Done")
    
    case "receive": 
        print("Listening...")
        with Chatroom.Receiver(ip, port) as chat:
            while message := chat.get_message():
                print(message.decode())
        print("Connection terminated")

    case "send": 
        with Chatroom.Sender(ip, port, name) as chat:
            print(f"Connected to {chat.dest}, start chatting!")
            while message := input("> "):
                chat.send_message(message.encode())
        print("Connection terminated")
        

