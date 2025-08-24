omonat = int(input("omonatingizni kiriting: "))

if omonat < 100_000:
    print (" foiz 5% ")

if 100_000 <= omonat and 500_000 >= omonat:
    print(" foiz 7% ")

if omonat > 500_000:
    print (" foiz 10% ")
    # bankka qo'yilgan omonat summasi qancha foiz oshishini topishimiz kk
    