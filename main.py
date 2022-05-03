salario_bruto= float(input("Ingrese tu salario: "))*12
print ("salario anual es :", salario_bruto)
#insss=salario_bruto*0.0625

if salario_bruto <=100000.00 :
    Impuesto_base1= 0.00
    sobrexceso1=0.00
    saldo_neto= salario_bruto-Impuesto_base1-sobrexceso1
    print("salario luego de deducciones: ", saldo_neto)
  
    if salario_bruto>=100000.01 and salario_bruto <= 200000.00:
      Impuesto_base2 = 0.00
      porcentaje_aplicable=0.15
      deducciones_anuales=((salario_bruto-100000.00 )-Impuesto_base2)*0.15
      deducciones_mensual=deducciones_anuales/12
      saldo_neto2=(salario_bruto-deducciones_anuales) / 12 
      print("salario  mensual luego de deducciones: ", saldo_neto2)
      print("las deducciones anuales son  : ", deducciones_anuales)
      print("IR mensual es: " , deducciones_mensual)
      
      if salario_bruto>=200000.01 and salario_bruto <= 350000.00:
        Impuesto_base3 = 15000.00
        porcentaje_aplicable=0.20
        deducciones_anuales3=((salario_bruto-200000.00 )*0.20)+Impuesto_base3
        deducciones_mensual_3=deducciones_anuales3/12
        saldo_neto3=(salario_bruto-deducciones_anuales3) / 12 
        print("salario  mensual luego de deducciones: ", saldo_neto3)
        print("las deducciones anuales son  : ", deducciones_anuales3)
        print("IR mensual es: " , deducciones_mensual_3)
        
        if salario_bruto>=350000.01 and salario_bruto <= 500000.00:
          Impuesto_base4 = 45000.00
          porcentaje_aplicable=0.25
          deducciones_anuales4=((salario_bruto-350000.00 )*0.25)+Impuesto_base4
          deducciones_mensual_4=deducciones_anuales4/12
          saldo_neto4=(salario_bruto-deducciones_anuales4) / 12 
          print("salario  mensual luego de deducciones: ", saldo_neto4)
          print("las deducciones anuales son  : ", deducciones_anuales4)
          print("IR mensual es: " , deducciones_mensual_4)
          
          if salario_bruto>=500000.01 :
            Impuesto_base5 = 82500.00
            porcentaje_aplicable=0.30
            deducciones_anuales5=((salario_bruto-500000.00 )*0.30)+Impuesto_base5
            deducciones_mensual_5=deducciones_anuales5/12
            saldo_neto5=(salario_bruto-deducciones_anuales5) / 12 
            print("salario  mensual luego de deducciones: ", saldo_neto5)
            print("las deducciones anuales son  : ", deducciones_anuales5)
            print("IR mensual es: " , deducciones_mensual_5)
else:
  ("hasta aqui llego")