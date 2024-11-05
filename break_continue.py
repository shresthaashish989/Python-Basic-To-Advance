# Write a program that calculates the total and average of the following list of numbers, stopping if
# a negative value is encountered (using break), and skipping any zero values (using continue).
values = [10, 0, 25, 0, 50, -1, 40]
total=0
for i in values:
    if i<0:
        break
    elif i==0:
        continue
    total+=i
    print(total)
    print(total/len(values))