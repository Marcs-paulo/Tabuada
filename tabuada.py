def tabuada():


   print('------------------Tabuada------------------ \n *Escolha uma das operações abaixo: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n')


   escolha = -1


   while escolha >= 1 or escolha <= 5:
      escolha = int(input('\nDigite o número referente a operação a ser escolhida \n R='))
      escolha += 0
      if escolha < 1 or escolha > 4:
         print('\nErro, o número deve ser entre 1 a 4! Tente novamente!')
         continue
      else:
         break


   oper_nome = ''
   if escolha == 1:
      oper_nome = 'Soma'
   if escolha == 2:
      oper_nome = 'Subtração'
   if escolha == 3:
      oper_nome = 'Multiplicação'
   if escolha == 4:
      oper_nome = 'Divisão'


   oper_num = float(input('\nA operação escolhida foi {} \nDigite de qual número será a tabuada \n R='.format(oper_nome)))


   print('|A tabuada de {} do {:.0f}|'.format(oper_nome, oper_num))


   if escolha == 1:
      for i in range (1, 11):
         print('         {:.0f} + {:2} = {:.0f}'.format(oper_num, i, oper_num + i))
   if escolha == 2:
      for i in range (1, 9):
         print('         {:.0f} - {:2} = {:.0f}'.format(oper_num, i, oper_num - i))
      for i in range (9, 11):
         print('         {:.0f} - {:2} = {:.0f}'.format(oper_num, i, i - oper_num))
   if escolha == 3:
      for i in range (1, 11):
         print('         {:.0f} X {:2} = {:.0f}'.format(oper_num, i, oper_num * i))
   if escolha == 4:
      for i in range (1, 11):
         multiplos = oper_num * i
         print('         {:.0f} : {:.0f} = {:.0f}'.format(multiplos, oper_num, multiplos / oper_num))


   resposta = ''
   while resposta == 'S' or 'N':
      resposta = input('\nDeseja refazer? S/N \n R= ').upper().strip()
      if resposta == 'S':
         tabuada()
         break
      if resposta == 'N':
         break
      print('A resposta não corresponde a pergunta (a resposta deve ser S ou N)')




tabuada()