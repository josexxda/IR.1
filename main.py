salario_bruto= float(input("Ingrese tu salario: "))*12
print ("salalario anual es :", salario_bruto)

if salario_bruto <=100000.00 :
  Impuesto_base1= 0.00
  sobrexceso1=0.00
  saldo_neto= salario_bruto-Impuesto_base1-sobrexceso1
  print("salario luego de deducciones: ", saldo_neto)
else : 
  print("no se puede")
if salario_bruto>=100000.01 and salario_bruto <= 200000.00:
  Impuesto_base2 = 0.00
  porcentaje_aplicable=0.15
  deducciones_anuales=((salario_bruto-100000.00 )-Impuesto_base2)*0.15
  deducciones_mensual=deducciones_anuales/12
  saldo_neto2=(salario_bruto-deducciones_anuales) / 12 
  print("salario  mensual luego de deducciones: ", saldo_neto2)
  print("las deducciones anuales son  : ", deducciones_anuales)
  print("IR mensual es: " , deducciones_mensual)
else: 
  print("no se puede wey") 
if salario_bruto>=200000.01 and salario_bruto <= 350000.00:
  Impuesto_base3 = 15000.00
  porcentaje_aplicable=0.20
  deducciones_anuales=((salario_bruto-200000.00 )+Impuesto_base3)*0.20
  deducciones_mensual=deducciones_anuales/12
  saldo_neto2=(salario_bruto-deducciones_anuales) / 12 
  print("salario  mensual luego de deducciones: ", saldo_neto2)
  print("las deducciones anuales son  : ", deducciones_anuales)
  print("IR mensual es: " , deducciones_mensual)
else:
  print("nel perro")