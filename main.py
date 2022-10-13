from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
  for letter in text:
    if letter not in alphabet:
      print(letter, end = "")
    elif (alphabet.index(letter)+shift < len(alphabet)):     
      print(alphabet[alphabet.index(letter) + shift], end= "")
    else: 
      #cycles the alphabet again
      print(alphabet[(alphabet.index(letter) - len(alphabet)) + shift], end = "")

def decode(text, shift):
  for letter in text:
    if letter not in alphabet:
      print(letter, end = "")
    elif alphabet.index(letter)-shift >= 0:     
      print(alphabet[alphabet.index(letter) - shift], end= "")
    else: 
      #cycles the alphabet again
      print(alphabet[(alphabet.index(letter) + len(alphabet)) - shift], end = "")      

should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 25

  if (direction == "encode"):
    encrypt(text, shift)
  else:
    decode(text, shift)

  restart = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")