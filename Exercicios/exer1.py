#Converter segundos em horas, minutos e segundos
#Desenvolva um programa que assuma uma entrada em segundos e a converta para horas, minutos e segundos

num = int(input("Insire um numero: "))
if num<60:
    seg = num
    print(seg, "segundo(s)")
elif num>=60 and num<3600:
    min=num//60
    seg=num%60
    print(min,"minuto(s) e ",seg,"segundo(s)")
else:
    hora=num/3600
    min=(num%3600)//60
    seg=(num%3600)%60
    print(hora,"hora(s)", min,"minuto(s) e ",seg,"segundo(s)")