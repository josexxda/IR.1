ingresos=int(input("ingresos: "))
egresos=int(input("egresos: "))
subsaldo= ingresos-egresos

if subsaldo>=15000:
        impuestos_altos=0.15
        saldo_alto=subsaldo*impuestos_altos
        saldo_neto=subsaldo-saldo_alto
        print("salario luego de deducciones: ", saldo_neto)
        print("Deducciones inss  : ", saldo_alto)

if subsaldo<=14999:
        impuestos_bajos=0.08
        saldo_bajo=subsaldo*impuestos_bajos
        saldo_neto=subsaldo-saldo_bajo
        print("salario luego de deducciones: ", saldo_neto)
        print("salrio bajo :", saldo_bajo)
