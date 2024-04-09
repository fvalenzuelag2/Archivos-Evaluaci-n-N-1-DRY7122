vlan = int(input("Cual es el numero de tu vlan? "))
if vlan >= 1 and vlan <= 99:
 print("Esta vlan es de rango normal.")
elif vlan >=100 and vlan <= 199:
 print("Esta es una vlan extendida")
else:
 print("Esta vlan no es extendida ni normal .")