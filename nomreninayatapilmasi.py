ay=["Yanvar","Fevral","Mart","Aprel","May","Iyun","Iyul","Avqust","Sentyabr","Oktyabr","Noyabr","Dekabr"]
number=0
sorqu=str(input())
while number!=11:
    if sorqu==ay[number]:
        print(number+1)
        sorqu=11
    else:
        number+=1