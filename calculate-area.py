ch='y'
while (ch=='y') or (ch=='Y'):
    l=int(input("Enter base of parallelogram:"))
    w=int(input("Enter width of parallelogram:"))
    h=int(input("Enter height of parallelogram:"))
    p=2*(l+w)
    a=l*w
    print("Area of parallelogram =",a)
    print("Perimeter of parallelogram =",p)
    ch=input("Do you want more y/n:")
while (ch!='y') or (ch!='Y'):
    if (ch=='n') or (ch=='N'):
        print("Goodbye")
        break
    else:
        while (ch!='y') or (ch!='Y') or (ch!='n') or (ch!='N'):
            print("Wrong input")
            ch=input("Do you want more y/n:")
print("thanks")
