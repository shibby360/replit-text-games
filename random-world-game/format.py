def format(list2d, island=None, select=None):
  for i in list2d:
    for j in i:
      if type(j.value) == dict and select:
        #specializaiton
        if j['island'] == island:
          if island == 'none':
            print('\033[34m', end='')
          else:  
            print('\033[0;42m', end='')
        if j['island'] == 'none':
          print('\033[34m', end='')
        dis = ' ' + j[select]
        dis = '🌴' if j[select] == 't' else dis
        dis = '📦' if j[select] == 'c' else dis
        dis = '⚔' if j[select] == 's' else dis
        dis = '🏴' if j[select] == 'p' else dis
        dis = ' ~' if j['island'] == 'none' and j[select] == ' -' else dis
        #end specialization
        print(dis, end='')
        print(' \033[0m', end='')
      else:
        print(j, end=' ')
    print()