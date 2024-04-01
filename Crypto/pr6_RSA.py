import random
import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def base64_to_image(base64_data, image_path):
    with open(image_path, "wb") as img_file:
        img_file.write(base64.b64decode(base64_data))


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = y2 - temp1 * y1

        x2 = x1
        x1 = x
        y2 = y1
        y1 = y

    if temp_phi == 1:
        d = y2 + phi

    return d

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal")

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    gcd_value = gcd(e, phi)
    while gcd_value != 1:
        e = random.randrange(1, phi)
        gcd_value = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

p = 61
q = 53
public_key, private_key = generate_keypair(p, q)

print("Public Key:", public_key)
print("Private Key:", private_key)

message = "Ye Mera Text He Jiska Aaj Postmortem Bole To Encryption Decryption Hoga!!!"
print("Original message:", message)

encrypted_msg = encrypt(public_key, message)
print("Encrypted message:", encrypted_msg)

decrypted_msg = decrypt(private_key, encrypted_msg)
print("Decrypted message:", decrypted_msg)

image_path = "vaidik.jpg"
base64_data = image_to_base64(image_path)
print("Image converted to base64.")

encrypted_data = encrypt(public_key, base64_data)
print("Base64 data encrypted.")

decrypted_data = decrypt(private_key, encrypted_data)
print("Data decrypted.")

base64_to_image(decrypted_data, "decrypted_image.jpg")
print("Decrypted data converted back to image.")
