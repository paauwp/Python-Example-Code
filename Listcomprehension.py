numbers = [1,2,5,7,9]
doubled = []
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
start_s = []

# LIST COMPREHENSION
start_s_comprehension = [friend for friend in friends if friend.startswith("S")]
doubled_comprehension = [num * 2 for num in numbers] 

# Traditional approach
for num in numbers:
    doubled.append(num*2)

# Traditional approach
for friend in friends:
    if friend.startswith("S"):
        start_s.append(friend)

#CHECK OUTPUT
print(doubled)
print(doubled_comprehension)
print(start_s)
print(start_s_comprehension)
