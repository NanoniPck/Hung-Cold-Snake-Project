import argparse

def get_args() -> tuple[str]:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode")
    parser.add_argument("ip")
    parser.add_argument("port")
    parser.add_argument("--keysize")

    args = parser.parse_args()

    supported_modes = ['send', 'receive', 're-key']
    if args.mode not in supported_modes:
        raise Exception(f'Mode "{args.mode}" not allowed; only support {supported_modes}')
    
    try: args.port = int(args.port)
    except ValueError: raise Exception('Invalid port number')
    
    if args.keysize != None:
        try: args.keysize = int(args.keysize)
        except ValueError: raise Exception('Invalid keysize number')

    return args.mode, args.ip, args.port, args.keysize
