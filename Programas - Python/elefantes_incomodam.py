def incomodam(n):
    '''Retorna 'incomodam ' n vezes'''
    if type(n) != int or n < 1:
        return ''
    elif n == 1:
        return 'incomodam '
    else:
        return 'incomodam ' + incomodam(n - 1)

def elefantes(n):
    if n < 1:
        return ''
    elif n == 1:
        return 'Um elefante incomoda muita gente'
    elif n == 2:
        return 'Um elefante incomoda muita gente\n2 elefantes incomodam incomodam muito mais'
    else:
        return elefantes(n - 1) + '\n' + str(n - 1) + ' elefantes incomodam muita gente\n' + str(n) + ' elefantes ' + incomodam(n) + 'muito mais'
    
# "Um elefante incomoda muita gente\n2 elefantes incomodam incomodam muito mais\n2 elefantes incomodam muita gente\n3 elefantes incomodam incomodam incomodam muito mais\n3 elefantes incomodam muita gente\n4 elefantes incomodam incomodam incomodam incomodam muito mais"

# print(elefantes(4))
# Um elefante incomoda muita gente
# 2 elefantes incomodam incomodam muito mais
# 2 elefantes incomodam muita gente
# 3 elefantes incomodam incomodam incomodam muito mais
# 3 elefantes incomodam muita gente
# 4 elefantes incomodam incomodam incomodam incomodam muito mais

if __name__ == '__main__':
    print(elefantes(3))
