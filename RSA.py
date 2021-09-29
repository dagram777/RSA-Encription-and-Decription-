import random

primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
          79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
          167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
          257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
          353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
          449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557,
          563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647,
          653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 793, 751, 757,
          761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
          877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


def primeGenerator():
    prime = random.randint(2 ** 20, (2 ** 22) - 1)
    if prime % 2 == 0:
        return primeGenerator()
    for i in primes:
        if prime % i == 0:
            return primeGenerator()
    return prime


p = primeGenerator()
# p = 1554073
# q = 3243397
q = primeGenerator()
n = p * q
totient = (p - 1) * (q - 1)
print(p, q)


def GCD(e, t=totient):
    while t != 0:
        e, t = t, e % t
    return e


for i in range(5000, 10000):
    if (GCD(i, totient) == 1):
        e = i
        break


def Pulverizer(a, b):
    if (a % b == 0):
        return (b, 0, 1)
    else:
        gcd, s, t = Pulverizer(b, a % b)
        s = s - ((a // b) * t)
        return (gcd, t, s)


def inverse(e, t=totient):
    gcd, s, _ = Pulverizer(e, t)


    if (gcd != 1):
        return None
    else:
        return s % t

publicKey = (e, n)
d = inverse(e, totient)
privateKey = (d, n)


def encrypt(message, publicKey):
    e, n = publicKey
    word = ""
    message.upper()
    for i in message:
        m = ord(i)
        encrypted = pow(m, e, n)
        word += str(encrypted)
        word += "o"
    return word


def decrypt(privateKey, encrypted_message):
    d, n = privateKey
    x = ""
    new = encrypted_message.split("o")
  
    for i in new:
        if i == "":
            continue
        else:
            m = pow(int(i), d, n)
            
            c = chr(m)
            x += c
    return x


message = input("Enter a message: ")
val = input("Type A for encryption and B for Decryption.")
value = val.upper()
if value == "A":
    print(f"Your message after encryption is: {encrypt(message, publicKey)} ")
    print(f"The original message was:{decrypt(privateKey, encrypt(message, publicKey))}")
#Inorder to decrypt a given message you should use specific p and q on line 26 and 27.
elif value == "B":
    print(f" Your message is :{decrypt(privateKey, message)}")

