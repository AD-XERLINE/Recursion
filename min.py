def findmin(n,len,temp,lst):
    t = temp
    if len != 1:
        if n < t:
            t = n
            l = lst
            return findmin(l[len-1],len-1,t,lst)

        if t < n:
            l = lst
            return findmin(l[len-1],len-1,t,lst)

    elif len == 1:
        return temp
        

lst = list(input("Enter Input : ").split(' '))
L = len(lst)
lst = [int(item) for item in lst] #แปลงของใน lst จาก['1','2','3'] เป็น [1,2,3]
print("Min : " + str(findmin(lst[L-1],L-1,lst[0],lst)))
