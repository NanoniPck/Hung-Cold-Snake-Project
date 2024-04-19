import RSA, Interface, Chatroom

mode, ip, port, keysize = Interface.get_args()

match mode:
    case "re-key": 
        print("Generating keys...")
        if keysize == None: new_keys = RSA.generate_key()
        else: new_keys = RSA.generate_key(size=keysize)
        RSA.set_keys(new_keys)
        print("Done")
    
    case "receive": 
        key = RSA.get_keys()
        print("Awaiting connection...")
        with Chatroom.Receiver(ip, port, key) as chat:
            print(f"Connected from {chat.addr}, start chatting!")
            while message := chat.get_message():
                print(message)
        print("Connection terminated")

    case "send": 
        with Chatroom.Sender(ip, port) as chat:
            print(f"Connected to {chat.dest}, start chatting!")
            while message := input("> "):
                chat.send_message(message)
        print("Connection terminated")
        

