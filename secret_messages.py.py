#!/bin/python3

alphabet = "abcdefghijklmnopqrstuvwxyz"
newmessage = ""
key = input('Enter the key: ')
key = int(key)

message = input('Enter the secret message: ')

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newposition = (position + key)%26
    newcharacter = alphabet[newposition]
    newmessage += newcharacter 
  else:
    newmessage += character

print(newmessage)