def busca(seq, x):

   primeiro = 0
   ultimo = len(seq) - 1

   while primeiro <= ultimo:
      meio = (primeiro + ultimo) // 2
      print(meio)
      if seq[meio] == x:
         return meio
      else:
         if x < seq[meio]:
            ultimo = meio - 1
         else:
            primeiro = meio + 1

   return False
