import json
def set_keys(key: tuple[int, int]):
    d, n = key
    keys_json = {"decrypt": d, "modulus": n}
    with open("RSA\\keys.json", "w") as config:
        json.dump(keys_json, config, indent=4)


def get_keys() -> tuple[int, int]:
    with open("RSA\\keys.json", "r") as config:
        keys = json.load(config)
        return keys["decrypt"], keys["modulus"]
