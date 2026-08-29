print("Our list is [2,7,6,6,2,]")
n = int(input("Enter a number : "))
y = [3,n, 5,3,5]
result = 0 
for x in y:
    result = result ^ x
print("The result is", result)