import fileinput

checkoftests=0
N=0
unregisteredcase=0
cookiedisc=list()
cookiedisc2=list()
cookieplate=list()
cookie_string=0
cookie_string2=0
flag = 0
flag2=0
trials = 0
f = open('outputcookies.txt','w')




for line in fileinput.input("happyinput.in"):
    if checkoftests == 0:
      checkoftests+=1
      print(line)
    else:
        N=line
        print("the line is ", N)
        disc_string = str(N)
        for cookie in str(disc_string):
            if cookie == "+":
                 cookiedisc.append(1)
                 flag +=1
            elif cookie == "-":
                cookiedisc.append(0)
    while sum(cookiedisc) < len(cookiedisc):
        flag2=0
        iterat=0
        for coin in cookiedisc:
            iterat+=1
            print(iterat)
            if coin==1: 
                if flag2!=0:
                    print("i have to take action")
                    trials += 1
                    for i in cookiedisc:
                        if i==0:
                            cookiedisc2.insert(i,1)
                        else:
                            cookiedisc2.insert(i,0)
                    flag2=0
                else: 
                    if iterat == len(cookiedisc2):
                        for i in cookiedisc:
                            if i==0:
                                cookiedisc2.insert(i,1)
                            else:
                                cookiedisc2.insert(i,0)
                            flag2=0
                    else:
                        flag2+=1
            print(cookiedisc)
            print(cookiedisc2)
            cookiedisc = cookiedisc2



            

    print("trials ",trials)
    flag=0






f.close()
print("That's all filks!")

