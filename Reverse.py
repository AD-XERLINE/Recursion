def ReverseList(Olst,len,Nlst):
    if len >= 0:
        # print(len-1)
        Nlst.append(Olst[len])
        return ReverseList(Olst,len-1,Nlst)

    if len < 0:
        return Nlst

lst = list(input("Enter your List : ").split(','))
lst = [int(item) for item in lst]
lst.sort()
L = len(lst)
Nlst = []

print("List after Sorted : "+ str(ReverseList(lst,L-1,Nlst)))