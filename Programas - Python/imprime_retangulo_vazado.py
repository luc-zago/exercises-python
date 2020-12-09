
l=int(input("Digite a largura:"))
a=int(input("Digite a altura:"))

x=1
y=1

while x<=a:
    if x>=2 and x!=a:
        print(end="#")
        y=2
        while y<l:
            print(end =" ")
            y=y+1
    elif x==a:
        while y<l:
            print(end ="#")
            y=y+1
    else:
        while y<l:
            print(end ="#")
            y=y+1
    x=x+1
    y=1
    print("#")
