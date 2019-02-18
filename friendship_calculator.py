#!/bin/python3

first = input("Enter the first name: ")
second = input("Enter the second name: ")
names = first+second
points = 0

for character in names:
  if character in 'aeiou':
    points += 5 
  if character in 'friends':
    points += 5
    
for character in first:
  if character in second:
    points += 10

print(points)
if(points >= 90):
  print('BEST FRIEND\'S FOREVER')
elif(points>=70):
  print('FRIENDS')
elif(points>=40):
  print('NAAH')
else:
  print('ENEMIES')