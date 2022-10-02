# วิธียูคลิก 
def GCD(m,l):
    c = m%l
    if c != 0:
        return GCD(l,c)
    elif c == 0:
        if l<0:
            l=l*-1
            return l
        else:
            return l
            
lst = list(input("Enter Input : ").split(' '))
a = int(lst[0])
b = int(lst[1])
if a == 0 and b != 0 and b > 0:
    print("The gcd of "+str(b)+" and "+str(a)+" is : "+ str(b))
elif a == 0 and b != 0 and b < 0:
    print("The gcd of "+str(a)+" and "+str(b)+" is : "+ str(b*-1))    
elif b == 0 and a != 0 and a>0:
    print("The gcd of "+str(a)+" and "+str(b)+" is : "+ str(a))
elif b == 0 and a != 0 and a<0:
    print("The gcd of "+str(b)+" and "+str(a)+" is : "+ str(a*-1))
elif a==0 and b==0:
    print("Error! must be not all zero.")
elif a > b:  #abs(a)<abs(b)
    print("The gcd of "+str(a)+" and "+str(b)+" is : "+ str(GCD(abs(a),abs(b))))
else:
    print("The gcd of "+str(b)+" and "+str(a)+" is : "+ str(GCD(abs(b),abs(a))))

# ถ้าเท่ากับ 0 ให้ตอบตัวหาร