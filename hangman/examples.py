# this is a comment! It is marked as it begins with a hashtag
# comments are ignored by the computer
# so I can leave handy notes everywhere without affecting my program.

# This is a string. We have to use it when we want to input text directly
"hello"
print("hello world")  #this will output "hello world" in the console

# This is a variable, x. Here, I've gone ahead and set it to 5.
x = 5
print(x) # this will output "5" in the console. Not x!
x = 3
print(x) # now, this will print "3"
x = 3+1
print(x) # take a guess what this prints

# this is an array. it's a collection of items, which we can change in and out.
myArray = ["a", "b", "c", "d", "e"]
print(myArray[0])   # prints out "a" (indexes start from 0)
print(myArray[4])   # prints out "e"
print(len(myArray)) # prints out 5, as there are five items
print(len("python")) # prints out 6, as there are 6 letters


y = 1   #try changing this to another number.
if y == 1:
    print("hello")
else:
    print("world")


for i in range(5): # will repeat the following 5 times
    print("wow")
    print(i)    # will print out i... what values will this be?

# what if we combine this with length???
myArray = ["a", "b", "c", "d", "e"]
for i in range(len(myArray)):   # remember, len(myArray) is going to be equal to 5
    print(myArray[i])           # what does i equal again? See above.
