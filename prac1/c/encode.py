import base64

with open('passwd_encoded.txt', 'r') as encoded_file:
        encoded_content = encoded_file.read()

decoded_content = base64.b64decode(encoded_content)

with open('passwd_decoded.txt', 'wb') as decoded_file:
        decoded_file.write(decoded_content)

print('file passwd_encoded.txt decoded into file passwd_decoded.txt')
