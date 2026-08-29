print("2 odd occuring")
n = int(input("Enter a 6 or 9"))
if n&1:
    print(n , "Binary = ", bin(n)[2:], "BIT 0 on group A")
else:
    print(n , "Binary = ", bin(n)[2:],"BIT 0 off group B")