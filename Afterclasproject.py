# part 1 whats xor
print("XOR with 0 keeps the number")
print("4 ^ 0 = ", 6 ^ 0)
print("6 ^ 0 = ", 6 ^ 0)
print("XOR with itself gives 0.")
print("7 ^ 7 = ", 7 ^ 7)
print("3 ^ 3 = ", 3 ^ 3)
n = int(input("Enter a number :"))
print("12 ^ ", n, " ^ 12", 12^n^12)
# part 2 numbers with xor
print("Our list is [8,3,0,5,4,]")
f = int(input("Enter a number : "))
y = [3,f, 5,3,5]
result = 0 
for x in y:
    result = result ^ x
print("The result is", result)
# part 3 sorting the BITS
print("2 odd occuring")
d = int(input("Enter a 6 or 9"))
if d&1:
    print(d , "Binary = ", bin(d)[2:], "BIT 0 on group A")
else:
    print(d , "Binary = ", bin(d)[2:],"BIT 0 off group B")