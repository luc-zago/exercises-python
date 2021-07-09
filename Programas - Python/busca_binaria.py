def busca_binaria(seq, x):
   ''' (list, int) -> bool
        retorna a posicao em que x ocorre na lista ordenada,
        ou None caso contrario, usando o algoritmo de busca binaria.
        '''
   #if seq[len(seq)//2] == x:
   #    return len(seq)//2
   #elif len(seq) == 1 and seq[0] != x:
   #    return None
   #elif seq[len(seq)//2] > x:
   #    return busca_binaria(seq[0:len(seq)//2], x)
   #else:
   #    return busca_binaria(seq[len(seq)//2:], x)
   # meu algoritmo encontra o elemento mas não retorna o index correto

   primeiro = 0
   ultimo = len(seq) - 1

   while primeiro <= ultimo:
      meio = (primeiro + ultimo) // 2
      if seq[meio] == x:
         return meio
      else:
         if x < seq[meio]:
            ultimo = meio - 1
         else:
            primeiro = meio + 1

   return False

if __name__ == '__main__':
    seq = range(1024)
    testes = [80, 50, 103, 1033]

    for t in testes:
        pos = busca_binaria(seq, t)
        if pos is None:
            print("Nao achei ", t)
        else:
            print("Achei ", t)
            print(pos)
