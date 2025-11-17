#Display numbers from 1 to 10 range
for i in range(1, 11):
    print(i)

#Display elements of the list:
colors = ["red", "green", "blue"]
for i in colors:
    print(i)

#Display all the letters of the word:
word = "Python"

for letter in word:
    print(letter)

#Using while loop count down from 10 to 0
x = 10
while x > -1:
    print(x)
    x -= 1

#Use break to stop the count at 5
x = 10
while x > -1:
    print(x)
    if x == 5:
        break
    x -= 1
