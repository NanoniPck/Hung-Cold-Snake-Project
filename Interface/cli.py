import argparse

def get_args() -> tuple[str]:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", help="set mode either 'send', 'receive', 're-key'")
    parser.add_argument("--ip")
    parser.add_argument("--port")
    parser.add_argument("--keysize")
    parser.add_argument("--name")

    args = parser.parse_args()

    supported_modes = ['send', 'receive', 're-key']
    if args.mode not in supported_modes:
        raise Exception(f'Mode "{args.mode}" not allowed; only support {supported_modes}')
    
    communicate_modes = ['send', 'receive']
    if args.mode in communicate_modes:
        if args.ip == None or args.port == None:
            raise Exception(f'ip and port required for {communicate_modes} modes')
        try: args.port = int(args.port)
        except ValueError: raise Exception('Invalid port number')

    named_modes = ['send', 're-key']
    if args.mode in named_modes and args.name == None:
        raise Exception(f'recipient name is required for send and re-key mode')

    
    if args.keysize != None:
        try: args.keysize = int(args.keysize)
        except ValueError: raise Exception('Invalid keysize number')

    return args.mode, args.ip, args.port, args.keysize, args.name
