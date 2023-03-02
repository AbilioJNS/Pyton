deuda = float(input("Introduce el coste de la hipotea o tu deuda\n"))
euribor  = float(input("introduce '%' de euribor\n"))
tin = float(input("introduce el '%' del banco\n"))
tiempo = int(input("introduce los años de hipoteca\n"))
cuotaSin = 0
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio"
         ,"Agosto","Septiembre","Octubre","Noviembre","Diciembre"]


def calcularInteres(deudaActual, tin, euribor):
    print(f"Porcentaje de interes total = {tin+euribor}%")
    interes = (tin+euribor)/100
    return (deudaActual * interes)/12

for i in range(0,12):
    if cuotaSin == 0:
        cuotaSin = (deuda/tiempo)/12
        print("cuota sin interés: "+ str(cuotaSin))
    interesCuota = calcularInteres(deuda, tin, euribor)
    print(f"{interesCuota}: Interes de la cuota")
    deuda -= cuotaSin
    print(f"{meses[i]}: {cuotaSin + interesCuota:.3f} deuda restante {deuda:.3f}")

    

