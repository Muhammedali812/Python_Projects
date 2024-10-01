ceki=float(input("ceki:\t"))
uzunluq=float(input("boy(m):\t")) 
bmi=ceki/(uzunluq**2) 
if bmi <=16:
    print("Şiddətli İncəlik")
elif bmi <=17:
    print("Orta İncəlik")
elif bmi <=18.5:
    print("Yüngül İncəlik")
elif bmi <=25:
    print("Normal")
elif bmi <=30:
    print("Artıq çəki")
elif bmi <=35:
    print("Obez sinif I")
elif bmi <=40:
    print("Obez sinif II")
elif bmi >=40:
    print("Obez sinif III")
else:
    print("Allah rehmet elesin")