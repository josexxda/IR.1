salario= int(input("Ingrese tu salario: "))*12
print ("salario anual es :", salario)
inss=salario*0.0625 /12
print("su insss es :", inss )
if salario <=100000.00 :
  saldo_neto= ((salario-0.00)-0.00)
  print("salario luego de deducciones: ", saldo_neto)
  
elif salario>=100000.01 and salario<= 200000.00:
  deducciones_anuales=((salario-100000.00 )*0.15)+0.00
  deducciones_mensual=deducciones_anuales/12
  saldo_neto2=(salario-deducciones_anuales) / 12
  print("salario  mensual luego de deducciones: ", saldo_neto2)
  print("IR anual  : ", deducciones_anuales)
  print("IR mensual : " , deducciones_mensual)
  
elif salario>=200000.01 and salario <= 350000.00:
  deducciones_anuales3=((salario-200000.00 )*0.20)+15000.00
  deducciones_mensual_3=deducciones_anuales3/12
  saldo_neto3=(salario-deducciones_anuales3) / 12 
  print("salario  mensual luego de deducciones: ", saldo_neto3)
  print("IR anual  : ", deducciones_anuales3)
  print("IR mensual es: " , deducciones_mensual_3)
  
elif salario>=350000.01 and salario <= 500000.00:
  deducciones_anuales4=((salario-350000.00 )*0.25)+45000
  deducciones_mensual_4=deducciones_anuales4/12
  saldo_neto4=(salario-deducciones_anuales4) / 12 
  print("salario  mensual luego de deducciones: ", saldo_neto4)
  print("IR anual  : ", deducciones_anuales4)
  print("IR mensual es: " , deducciones_mensual_4)

elif salario>=500000.01 :
  deducciones_anuales5=((salario-500000.00 )*0.30)+82500
  deducciones_mensual_5=deducciones_anuales5/12
  saldo_neto5=(salario-deducciones_anuales5) / 12 
  print("salario  mensual luego de deducciones: ", saldo_neto5)
  print("IR anual  : ", deducciones_anuales5)
  print("IR mensual es: " , deducciones_mensual_5)
else:
  ("nel perrro")
  
  print("gracias")
