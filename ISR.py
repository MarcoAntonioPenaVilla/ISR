import matplotlib.pyplot as plt
"""A=int(input("Ingresa el total de personas: "))
for X in range(A):"""
P=(input("Ingresa el Nombre de la persona: "))
I=float(input("ingresos de la persona a la quincena: ")) 
GM=I*2
IVA=I*0.16
Total0=GM-IVA
print("El IVA a pagar es: ",IVA)
print("Tus ingresos mensuales son de: ",Total0)

plt.figure(figsize=(8,6))
plt.scatter([P],[I],[IVA],marker="o",color="Blue")
plt.title("Servicios de administracion Tributaria")
plt.ylabel(I)
plt.xlabel(IVA)
plt.show()

print("Inversiones compuestas")
M=int(input("Ingresa el monto original: "))
TASA=int(input("Ingresa el porcentaje de crecimiento: "))
Cr=TASA*0.01
Ganancia=M*Cr
Total=M+Ganancia
Impuesto=Total*0.009
G=Ganancia-Impuesto
GAT=Total-Impuesto
print()
print("------------")
print()
print("El rendimiento neto es de: ",Ganancia)
print("El total mas ganancias es de: ",Total)
print("La retencion de impuestos ISR es de: ",Impuesto)
print("Menos ISR su Ganancia Neta Bruta es de: ",G)
print("Su total es de: ",GAT)
plt.figure(figsize=(8,6))
plt.scatter([M],[TASA],[GAT],marker="o",color="Blue")
plt.title("Interes Compuesto")
plt.ylabel(M)
plt.xlabel(TASA)
plt.show()
