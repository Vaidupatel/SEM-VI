import random

def generate_large_prime():
    while True:
        prime_candidate = random.randint(100, 1000)
        if is_prime(prime_candidate):
            return prime_candidate

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_private_key(p):
    return random.randint(1, p - 1)

def calculate_public_key(g, private_key, p):
    return pow(g, private_key, p)

def calculate_shared_secret(public_key, private_key, p):
    return pow(public_key, private_key, p)

def diffie_hellman():
    p = generate_large_prime()
    print("Prime number:",p)
    g = 5 
    print("Primitive Root(g):",g)

    alice_private_key = generate_private_key(p)
    bob_private_key = generate_private_key(p)

    alice_public_key = calculate_public_key(g, alice_private_key, p)
    bob_public_key = calculate_public_key(g, bob_private_key, p)

    alice_shared_key = calculate_shared_secret(bob_public_key, alice_private_key, p)
    bob_shared_key = calculate_shared_secret(alice_public_key, bob_private_key, p)

    return alice_shared_key, bob_shared_key

alice_secret, bob_secret = diffie_hellman()
print("Alice's shared secret:", alice_secret)
print("Bob's shared secret:", bob_secret)
