import RSA, Interface, Chatroom

mode, ip, port, keysize, name = Interface.get_args()

match mode:
    case "receive": 
        print("Listening...")
        with open('TestCases\\receiving_image.jpg', 'wb') as f:
            with Chatroom.Receiver(ip, port) as chat:
                while data := chat.get_message():
                    f.write(data)
        print("Connection terminated")

    case "send": 
        with open('TestCases\\sending_image.jpg', 'rb') as f:
            with Chatroom.Sender(ip, port, name) as chat:
                print(f"Sending to {chat.dest}...")
                while data := f.read(100):
                    chat.send_message(data)
                chat.send_message(b'')
        print("Connection terminated")
        

