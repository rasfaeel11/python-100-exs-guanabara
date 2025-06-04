num = str(input("digite um numero de 0 a 9999: "))
num = "000" + num
print("tem {} unidades" .format(num[-1]))
print("tem {} dezenas".format(num[-2]))
print("tem {} centenas".format(num[-3]))
print("tem {} milhares ".format(num[-4]))