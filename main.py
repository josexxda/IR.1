salario_bruto= float(input("Ingrese tu salario anual: "))*12
 

if salario_bruto <=100000.00 :
        Impuesto_base1= 0.00
        sobrexceso1=0.00
        saldo_neto= salario_bruto-Impuesto_base1-sobrexceso1
        print("salario luego de deducciones: ", saldo_neto)
else : 
  print("no se puede")
if salario_bruto>=100000.01 and salario_bruto <= 200000.00:
  Impuesto_base2 = 0.00
  sobrexceso2=100000.00
  porcentaje_aplicable=0.15
  saldo_neto2=((salario_bruto-Impuesto_base2)-sobrexceso2)*0.15
  print("salario luego de deducciones: ", saldo_neto2)
else: 
  print("no se puede wey")