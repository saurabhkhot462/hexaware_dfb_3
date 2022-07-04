name=input("Enter Name: ")
K=int(input("Enter kannada marks: "))
E=int(input("Enter English marks: "))
H=int(input("Enter hindi marks: "))
S=int(input("Enter Science marks: "))
SS=int(input("Enter Social Science marks: "))
M=int(input("Enter Maths marks: "))

total=K+E+H+S+SS+M
per=total/6

if(per>85):
    print("Hii ",name,"You got Disticntion")
    
elif (per >60 and per<85):
    print("Hii ",name,"You got First class")

elif(per < 60 and per>35):
    print("Hii ",name,"You are pass")
else:
    print("Hii ",name,"You are fail")
    



