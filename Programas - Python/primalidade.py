
print("Este programa lhe informa se um número é primo.")
a=int(input("Informe um número inteiro positivo:"))


if a==2 or a==3 or a==5 or a==7 or a==11 or a==13 or a==17 or a==19 or a==23 or a==29 or a==31 or a==37 or a==41 or a==43 or a==47 or a==53 or a==59 or a==61 or a==67 or a==71 or a==73 or a==79 or a==83 or a==89 or a==97:
 print("primo")
elif a==1 or a%2==0 or a%3==0 or a%5==0 or a%7==0 or a%11==0 or a%13==0 or a%17==0 or a%19==0 or a%23==0 or a%29==0 or a%31==0 or a%37==0 or a%41==0 or a%43==0 or a%47==0 or a%53==0 or a%59==0 or a%61==0 or a%67==0 or a%71==0 or a%73==0 or a%79==0 or a%83==0 or a%89==0 or a%97==0:
 print("não primo")
else:
 print("primo")

 def primo(x):
    f=2
    if x==2:
        return True
    while x % f!=0 and f <= (x/2):
        f=f+1
    if x%f==0:
        return False
    else:
        return True
