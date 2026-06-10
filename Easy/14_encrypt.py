
def encode_or_decode(msg: str, mode: str) -> str:
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    values = keys[-1] + keys[0:-1]
    dict_encode = dict(zip(keys,values))
    dict_decode = {value:key for key, value in dict_encode.items()}
    
    if mode.lower() == 'e':
        new_msg = ''.join([dict_encode[letter] for letter in msg.lower()])
    else:
        new_msg = ''.join([dict_decode[letter] for letter in msg.lower()])
    
    return new_msg.capitalize()

msg = input('Enter your secret message quietly: ')
mode = input('Crypto mode: encode (e) OR decrypt as default: ')
print(encode_or_decode(msg, mode))
