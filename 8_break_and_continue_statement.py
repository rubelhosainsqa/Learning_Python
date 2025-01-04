
for a in range(10):
    if a == 5:
        break   # Basically by default value of a is o and maximum value will be 10, break used for postponed the statement based on when if condition will be true
    print(a)


i = 1
for i in range(10):
    if i == 5:
        continue
    print(i)
    i+=1