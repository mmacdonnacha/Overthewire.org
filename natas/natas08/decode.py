from base64 import b64decode
from binascii import unhexlify


encoded_secret = '3d3d516343746d4d6d6c315669563362'

# Convert from hexadecimal to ascii
unhexed_secret = unhexlify(encoded_secret)

# Reverse string
reverse_secret = unhexed_secret[::-1]

# Decode the Base64 string
decoded_base64 = b64decode(reverse_secret).decode()

print(decoded_base64)

# One Liner
password = b64decode(unhexlify(encoded_secret)[::-1]).decode()
print(password)