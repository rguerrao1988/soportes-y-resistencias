
print("welcome")
# API ES: 4P7IRO8UHNJMBM1X
maximo = input("valor maximo")
minimo = input("valor minimo")
cierre = input("vaqlor cierre")
mx=int(maximo)
mn=int(maximo)
cl=int(minimo)
pp=mx+mn+cl/3
pivot=f"pivot: {pp}"
S2=f"Soporte 2: {pp-(mx-mn)}"
S1=f"Soporte 1: {(pp*2)-mx}"
R1=f"Resistencia 1: {(pp*2)-mn}"
R2=f"Resistencia 2: {pp+(mx-mn)}"
print(pivot) # punto pivot
print(S1)# soporte 1
print(S2)# soporte 2
print(R1)# resistencia 1
print(R2)# resistencia 2 
