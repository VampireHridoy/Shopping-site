#Budget control
#This loop will go untill the budget is integer or float while true :
try :
             bg=float(input("Enter your budget : "))
             #if budget is integer or float it will be stored
             #temporary is variables's
             s=bg
except ValueError:
        print("PRINT A NUMBER AS AMOUNT") 
        
else:
       
#dictionary to store preoduct ("Name"),quality("qurant",
#price("Price") with empty list their values
 a={"name":[], "quant":[], "price":[]}
#converting dictionary to list for further updation
b=list(a.values())
na=b[0]
qu=b[1]
pr=b[2]

while True:
    try:
            ch=int(input("1.ADD\n2.EXIT\nEnter your choice :"))
    except ValueError:
     print("\nERROR: Choose only digits from the given option")
    continue
else:
        if ch == 1 and s>0:
#input product name
                pn=input("Enter product Name : ")
                q=input("Enter quantity : ")
                p=float(input("Enter price of the product : "))
                if p>s:
                 print("\nCAN, T BUT THE PRODUCT")
            
        else: 
               ind= na.index(pn)
               qu.remove(qu[ind])
               pr.remove(pr[ind])
               qu.insert(ind,q)
               pr.insert(ind,p)
               s=bg-sum(pr)
            
               print("\namount left", s)
        else:
        na.append(pn)
        qu.append(q)
        pr.append(p)
        s=bg-sum(pr)
        print("\namount left", s)
        elifs<=0:
print("\nNO BUDGET")

print("\nAmount left : Rs."s)
if s in pr : 
       print("n\Amount left can buy you a", na[pr.index(s)])
print("\n\n\nGROCERY LIST")
for i in range(len(na)):
       print(na[i], qu[i], pr[i])
      #CODE BY KM ROKONUZZAMAN

        
        
 
    