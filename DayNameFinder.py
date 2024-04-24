d=int(input("Enter The Date : ")) 
if(d>0 and d<=31):
    m=int(input("Enter The Month : "))
    if(m>0 and m<12):
        if(((d<=31) and (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12)) or((d<=30) and(m==4 or m== 6 or m==9 or m==11)) or ((d<=29) and (m==2))):
            y=int(input("Enter The Year : "))
            if (y>1900 and y<9999):
                c=y//100
                D=y%100
                if m>2:
                    m-=2
                else:
                    m+=1

                f=d+((13*m-1)/5)+D+D/4+(c/4)-2*c
                fres=int(f%7)
                day={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
                print(day[fres])
            else:
                print("Incorrect Year")
        else:
            print("Invalid Date")
    else:
        print("Incorrect Month")
else:
    print("Incorrect Date")