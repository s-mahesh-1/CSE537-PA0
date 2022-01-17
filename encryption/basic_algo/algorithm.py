

def simple_encrypt(plain_text):
	return "".join([chr(25 - ord(c) + 2*ord('a')) for c in plain_text])


def simple_decrypt(cipher_text):
	return simple_encrypt(cipher_text)