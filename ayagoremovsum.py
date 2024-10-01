ay=["Yanvar","Fevral","Mart","Aprel","May","Iyun","Iyul","Avqust","Sentyabr","Oktyabr","Noyabr","Dekabr"]
number=0
sorqu=str(input())
while number!=12:
    if sorqu==ay[number]:
        nomre=number+1
        number=12
    else:
        number+=1
if nomre <=2 or nomre==12:
    print("qish")
elif nomre <=5:
    print("yaz")
elif nomre <=8:
    print("yay")
elif nomre <=11:
    print("payiz")
else:
    print("duzgun nomre daxil edin")