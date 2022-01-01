secret_code="spooky"
entered_code=input("Please Enter Your Code \n")
count=1
flag=True

while secret_code!=entered_code and flag==True:
     if count<=3:
         entered_code=input("Please Enter Your Code || attempt : "+str(count)+" \n")
         count+=1
     else:
        flag=False

if flag:
    print("You Entered the correct code")
else:
    print("You lost")