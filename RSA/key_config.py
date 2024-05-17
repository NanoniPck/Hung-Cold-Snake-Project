import json, configparser, pathlib
from RSA.generate_keys import generate_key

KEYS_FOLDER = pathlib.Path(__file__).parent.parent / 'Keys'
CONF_PATH = KEYS_FOLDER / 'private.cfg'

def re_key(name: str, size: int = 512, e: int = 65537):
    e, d, n = generate_key()
    config = configparser.ConfigParser()
    config['DEFAULT'] = { 'name': name, 'd': d, 'n': n }
    with open(CONF_PATH, 'w') as private:
        config.write(private)
    config['DEFAULT'] = { 'e': e, 'n': n }
    with open(KEYS_FOLDER / f'{name}.cfg', 'w') as public:
        config.write(public)

def get_private_config() -> tuple[str, int, int]:
    exc = Exception('private.cfg not found or corrupt; please re-key.')
    config = configparser.ConfigParser()
    if not config.read(CONF_PATH): raise exc
    name = config['DEFAULT'].get('name')
    try: 
        d = int(config['DEFAULT'].get('d'))
        n = int(config['DEFAULT'].get('n'))
    except ValueError: raise exc
    if None in [name, d, n]: raise exc
    return name, d, n

def get_public_key(name: str) -> tuple[int, int]:
    exc = Exception(f'{name}.cfg not found or corrupt; please re-obtain key.')
    config = configparser.ConfigParser()
    if not config.read(KEYS_FOLDER / f'{name}.cfg'): raise exc
    try: 
        e = int(config['DEFAULT'].get('e'))
        n = int(config['DEFAULT'].get('n'))
    except ValueError: raise exc
    if None in [e, n]: raise exc
    return e, n

    