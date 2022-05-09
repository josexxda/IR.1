#CALCULADORA DE IR Y INSS ANUAL
salario =int(input("Ingrese tu salario: "))*12
inss =salario*0.0625
print("su insss es :", inss )
#SALARIO ANUAL DE 100000.00 
if salario <=100000.00 :
  saldo_neto = ((salario-0.00)-0.00)
  print("salario excento de IR: ", saldo_neto ,)
#SALRIO ANUAL DE 100000.01 A 200000.00
elif salario>=100000.01 and salario<= 200000.00:
     deducciones_anuales =((salario-100000.00 )*0.15)+0.00
     print("IR anual  : ", deducciones_anuales)
 #SALARIO DE 200000.01 A 350000.00
elif salario>=200000.01 and salario <= 350000.00:
     deducciones_anuales3 =((salario-200000.00 )*0.20)+15000.00
     print("IR anual : ", deducciones_anuales3)
#SALARIO ANUAL 350000.01 A 500000.00
elif salario>=350000.01 and salario <= 500000.00:
     deducciones_anuales4 =((salario-350000.00 )*0.25)+45000
     print("IR anual  : ", deducciones_anuales4)
#SALARIO ANUAL 500000.01 A MAS
elif salario>=500000.01 :
     deducciones_anuales5 =((salario-500000.00 )*0.30)+82500
     print("IR anual  : ", deducciones_anuales5)
else:
  ("nel perrro")
  
print("gracias")
