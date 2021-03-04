invalid_method = True
invalid_num = True
method = input("Encode or Decode: ").lower()

while invalid_method == True:
    if (method[0] == "d" or method[0] == "e"):
        invalid_method = False
    else:
        method = input("Please enter a valid choice: ").lower()

message = input("Enter your message: ").lower()
key = int(input("Enter the key number (1-26): "))

while invalid_num == True:
    if (key <= 0 or key > 26):
        key = int(input('Please enter a valid number: '))
    else:
        invalid_num = False

if method[0] == "d":
    key = -key
coded = ""
for char in message:
    if char.isalpha():
        num = ord(char)
        num += key
        if num > ord("z"):
            num -= 26
        elif num < ord("a"):
            num += 26
        coded += chr(num)
    else:
        coded += char
print("Your encoded message: " + str(coded))