from ctypes import c_char
import random
import string
print("Password Generator!")
def generate_password(length):
  letters=string.ascii_letters
  symbols=string.punctuation
  numbers=string.digits

  n_letter=int(input("Number of letters to enter: "))
  n_symbol=int(input("Number of symbols to enter: "))
  n_number=int(input("Number of numbers to enter: "))

  password=""
  for i in range(1,n_letter+1):
    char=random.choice(letters)
    password=password+char
  for i in range(1,n_symbol+1):
    char=random.choice(symbols)
    password=password+char
  for i in range(1,n_number+1):
    char=random.choice(numbers)
    password=password+char
  while len(password)<length:
    char=random.choice(string.printable)
    password+=c_char
  password=password[:length]
  return password

length_req=int(input("enter the length of the password: "))
generated_password=generate_password(length_req)
print("Generated password: ", generated_password)
