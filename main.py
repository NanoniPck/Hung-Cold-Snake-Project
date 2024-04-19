import argparse, RSA, Interface

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
        

