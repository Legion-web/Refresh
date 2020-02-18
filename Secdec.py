#Sequence decoder
inp=""
print("Welcome to the sequence decoder")
inp=input("Enter your sequence :")
inpstr=inp.split()
a=inpstr[0]
b=inpstr[1]
c=int(b)-int(a)
seqno=int(input("Enter the position of the number which you want to find out :"))
seqno1=int(seqno)
seqnon=seqno1-1
seqno2=seqnon * c
seqno3=seqno2 + int(a)
print(seqno3)
