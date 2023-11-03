user_input=list(map(int,input().split(",")))
positive_no=[]
for i in user_input:
    if i>0:
        positive_no.append(i)


print(positive_no)  
