# def add_without(a,b):
#     while b != 0:
#         data = a & b #data=12
#         a = a ^ b    #a=26
#         b = data << 1 #b=240
#     return  a
# print("25 + 10 = ",add_without(25 ,10))

def add(a,b):
    if a != b:
        return (a*a-b*b)/(a-b)
    else:
        return 2*a
def main():
    a=int(input("enter no1:"))
    b=int(input("enter no2:"))
    print("sum :", int(add(a,b)))
main()
 