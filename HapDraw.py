def print_sq(n):
    if (n == 0):
        return
    
    print("#", end="")
    print_sq(n - 1)

def staircase(space):
    if (space == 0):
        return
     
    print("_", end="")
    staircase(space - 1)
# กำหนดการวาดอันไหนก่อนหลัง ส่วนแพทเทินจะวาดแบบไหนกำหนด num n เอา
def pattern(num,n):
    if (n == 0):
        return

    staircase(n - 1) #ก่อน
    print_sq(num - n + 1) #หลัง
    print()
 
    pattern(num, n - 1)

def inversepattern(num,n):
    if (n == num):
        return

    staircase(n)
    print_sq(num - n)
    print()

    inversepattern(num, n + 1)


I = int(input("Enter Input : "))
if I == 0:
    print("Not Draw!")
elif I<0:
    inversepattern(I*-1,0)
else:
    pattern(I, I)