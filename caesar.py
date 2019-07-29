def caesar(process, message, key):
	if process[0] == 'd':
		key = -key
	translated = ''
	for symbol in message:
		if symbol.isalpha():
			num = ord(symbol)
			num += key
			if num > ord('z'):
				num -= 26
			elif num < ord('a'):
				num += 26
			translated += chr(num)
		else:
			translated += symbol
	return translated

def main():
	invalid = True
	# Choosing a process
	process = input("Would you like to encode or decode?\n").lower()
	print()
	if process in 'encode decode'.split():
		process = process
	else:
		process = input('Enter either "encode" or "decode":\n').lower()
		print()
	# Entering Message
	message = input('Enter your message:\n').lower()
	print()
	# Getting a valid key number
	key = 0
	key = int(input('Enter the key number (1-26):\n'))
	print()
	while invalid == True:
		if (key >= 1):
			invalid = False
			key = key
		else:
			invalid = True
			key = int(input('Please enter a key number greater than 0:\n'))
			print()
	# Printing the encoded / decoded message
	if process[0] == 'd':
		print('Your decoded message:')
	elif process[0] == 'e':
		print('Your encoded message:')
	print(caesar(process, message, key))

main()
