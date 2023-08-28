import random
import math
import rsa

print("Modes: 1 - generate RSA public and priv keys using default math function, 2 - generate priv and pub keys using RSA library, 3 - decode encrypted message with private key ")
a = int(input("Use mode [1/2/3]: "))

def check_prime(number):
	if number < 2:
		return False
	for i in range(2, number // 2 + 1):
		if number % i == 0:
			return False
	return True

def generate_prime(min_value, max_value):
	prime = random.randint(min_value, max_value)
	while not check_prime(prime):
		prime = random.randint(min_value, max_value)
	return prime



def mod_inverse(e, phi):
	for d in range(3, phi):
		if (d * e) % phi == 1:
			return d

	raise ValueError("mod_inverse does not exist")

if a == 1:
	print("Remember,the higher the max value and min value, the more they will be generated")
	minV = int(input("Input min generating value of your p and q: "))
	maxV = int(input("Input max generating value of your p and q: "))
	p, q = generate_prime(minV, maxV), generate_prime(minV, maxV)

	while p == q:
                q = generate_prime(minV, maxV)

	n = p * q

	phi_n = (p-1) * (q-1)

	e = random.randint(3, phi_n-1)
	while math.gcd(e, phi_n) != 1:
                e = random.randint(3, phi_n -1)


	d = mod_inverse(e, phi_n)


	print("Public Key:", e)
	print("Private Key:", d)
	print("n:", n)
	print("Phi of n:", phi_n)
	print("q:", q)
	print("p:", p)

	ask = input("Do you want also encrypt some message [y=1/n=any message]: ")
	if ask == "1":
		message = input("Input message: ")
		message_encoded = [ord(c) for c in message]
		ciphertext = [pow(c, e, n) for c in message_encoded]
		print(ciphertext)

if a == 2:
	print("Generating your private and public keys...")
	public_key, private_key = rsa.newkeys(1024)

	with open("public.pem", "wb") as f:
		f.write(public_key.save_pkcs1("PEM"))

	with open("private.pem", "wb") as f:
		f.write(private_key.save_pkcs1("PEM"))

	ask = input("Do you want also encrypt some message [y=1/n=any message]: ")
	if ask == "1":
		message = input("Input message: ")
		encrypted_message = rsa.encrypt(message.encode(), public_key)
		with open("encrypted.message", "wb") as f:
			f.write(encrypted_message)

if a == 3:
	print("Remember, if you want to decrypt an encrypted message, using the private key, you should have a message and a private key in directory with this file ")
	name_mes = input("Input the name of file with encrypted message: ")
	name_key = input("Input the name of your private key: ")
	with open(name_key, "rb") as f:
		private_key = rsa.PrivateKey.load_pkcs1(f.read())
	encrypted_message = open(name_mes, "rb").read()
	clear_message = rsa.decrypt(encrypted_message, private_key)
	print("Decrypted message: ", clear_message.decode())
