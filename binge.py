def binge(order):
    k=sorted(order)
    max_con=[]
    temp=[k[0]]
    for i in range(len(k)-1):
        if k[i]+1==k[i+1]: 
            temp.append(k[i+1])
        else:                     
            if temp:             
                max_con.append(temp)
            temp=[k[i+1]]    
    if temp:                     
        max_con.append(temp)
    res=sorted(max_con,key=lambda x:len(x),reverse=True)
    if len(res[0])==1:
        return "No consecutive watch order."
    else:
        return f"Longest proper binge {res[0]}"
List=eval(input("Watched episodes: "))
print(binge(List))
