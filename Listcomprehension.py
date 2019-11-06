import pandas as pd

numbers = [1,2,5,7,9]
doubled = []
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
start_s = []

start_s_comprehension = [friend for friend in friends if friend.startswith("S")] # list comprehension
doubled_comprehension = [num * 2 for num in numbers] # list comprehension

# Traditional approach
for num in numbers:
    doubled.append(num*2)

# Traditional approach
for friend in friends:
    if friend.startswith("S"):
        start_s.append(friend)


print(doubled)
print(doubled_comprehension)
print(start_s)
print(start_s_comprehension)

# Convert a list in a dataframe 
df = pd.DataFrame({'col':friends})
print (df)