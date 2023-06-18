itens = []
itensGet = []
quests = []
floresta = []

nome = ""
inputi = ""

winat1 = 0
passagemAberta = 0
area = 1

#controles
print("CONTROLES:")
print("s = sim e n = não")
print("digite o nome das opções com letra minuscula(no caso de espaço use - )")

#introdução
print("")
print("Olá, você deve ser o aventureiro de que me falaram...")
print("...então, qual é seu nome?")
nome = input("")
print("Ok {}, vamos lá!".format(nome))
print("Você quer começar a aventura?")
inputi = input("")

#aventura
if(inputi == "s"):
  print("")
  print('CABANA INICIAL')
  print("")

  #update
  while(winat1 == 0):

  #area1 CABANA INICIAL

    if(area == 1):
      #0 itens
      if(len(itensGet) == 0):
        print("Certo, você vai levar uma corda ou uma faca para a sua aventura?(corda/faca)")
        inputi = input("")

        if(inputi == "corda"):
          print("Você escolheu a corda")
          itens.append(inputi)
          itensGet.append(inputi)
          print("")
          print("ESTRADA")
          print("")
          area = 2

        elif(inputi == "faca"):
          print("Você escolheu a faca")
          itens.append(inputi)
          itensGet.append(inputi)
          print("")
          print("ESTRADA")
          print("")
          area = 2

        else:
          print("")
          print("escolha uma opção dentre as mencionadas entre parenteses")
          print("")
      
      #1 ou + itens

      else:
        corda = 0
        faca = 0
      
        for a in floresta:
        
          if(a == 'corda'):
            corda = 1  
      
          elif(a == 'faca'):
            faca = 1
      
        if(faca == 1 and corda == 1):
          print('mais nada para fazer aqui!')
          print("")
          print("ESTRADA")
          print("")
          area = 2
      
        elif(corda == 1):
          print("Você quer levar a faca?")
          inputi = input("")
      
          if(inputi == "s"):
            print("Você pegou a faca")
            itens.append("faca")
            itensGet.append("faca")
            print("")
            print("ESTRADA")
            print("")
            area = 2
      
          elif(inputi == "n"):
            print("Ok então...")
            print("")
            print("ESTRADA")
            print("")
            area = 2
      
        elif(faca == 1):
          print("Você quer levar a corda?")
          inputi = input('')
      
          if(inputi == "s"):
            print("Você pegou a corda")
            itens.append("corda")
            itensGet.append("corda")
            print("")
            print("ESTRADA")
            print("")
            area = 2
      
          elif(inputi == "n"):
            print("Ok então...")
            print("")
            print("ESTRADA")
            print("")
            area = 2

  #area2 ESTRADA 

    if(area == 2):
      print("Onde você vai esplorar?")
      print("Você quer ir para a montanha, para a vila ou para a floresta ou ver seus itens?(montanha/vila/floresta/itens)")
      inputi = input("")

      if(inputi == "montanha"):
        print("")
        print("MONTANHA ANCESTRAL")
        print("")
        area = 3
      
      elif(inputi == "vila"):
        print("")
        print("VILA VOLEIRO")
        print("")
        area = 4

      elif(inputi == "floresta"):
        print("")
        print("FLORESTA DOS CEM PASSOS")
        print("")
        area = 5

      elif(inputi == "itens"):
        print("itens:")
        for a in itens:
          print(a,",")
      
      else:
        print("escolha uma opção dentre as mencionadas entre parenteses")

  #area3 MONTANHA ANCESTRAL

    if(area == 3):
      print("Você caminha velozmente até a Montanha Ancestral, conhecida por seus mais valiosos tesouros...")
      print("Voce quer escalar ela, voltar para a estrada ou olhar ao redor dela?(escalar/voltar/olhar)")
      inputi = input("")
      
      if(inputi == "escalar"):
        corda = 0

        for a in range(0,len(itens)):
          if(itens[a] == 'corda'):
            corda = 1
        
        if(corda == 1):
          print("O terreno está íngrime")
          print("Você usa sua corda para escalar a montanha")
          print("")
          print("TOPO DA MONTANHA ANCESTRAL")
          print("")
          area = 6

        else:
          print("O terreno está íngrime")
          print("Você precisa de uma corda para escalar a montanha")
      
      elif(inputi == "voltar"):
        print("")
        print("ESTRADA")
        print("")
        area = 2

      elif(inputi == "olhar"):
        print("Você olha em volta de toda a montanha e finalmente acha alguma coisa:")
        print("Você achou a Caverna dos Medos Medonhos, a mais temida em todo o mundo!!!")
        print("Você quer entrar nela ou voltar?(entrar/voltar)")
        inputi = input("")
        
        if(inputi == "entrar"):
          print("")
          print("CAVERNA DOS MEDOS MEDONHOS")
          print("")
          area = 7

        elif(inputi != "voltar"):
          print("escolha uma opção dentre as mencionadas entre parenteses")

      else:
        print("escolha uma opção dentre as mencionadas entre parenteses")

  #area4 VILA VOLEIRO
    
    if(area == 4):
      print("Todos os aldeões dizem juntos:")
      print("Você chegou!!!")
      print("Você sente o aconchego e o afeto que eles o oferecem")
      print("Mas tem muito trabalho pela frente...")
      print("Você vê um açougueiro, um carpinteiro, um minerador e um cara misterioso.")
      print("Com quem você irá falar? Ou você vai voltar?(açougueiro/carpinteiro/minerador/misterioso/voltar)")
      inputi = input("")

      if(inputi == "açougueiro"):
        print("")
        print("AÇOUGUEIRO")
        print("")
        area = 8

      elif(inputi == "carpinteiro"):
        print("")
        print("CARPINTEIRO")
        print("")
        area = 9

      elif(inputi == "minerador"):
        print("")
        print("MINERADOR")
        print("")
        area = 10

      elif(inputi == "misterioso"):
        print("")
        print("CARA MISTERIOSO")
        print("")
        area = 11

      elif(inputi == "voltar"):
        print("")
        print("ESTRADA")
        print("")
        area = 2

      else:
        print("escolha uma opção dentre as mencionadas entre parenteses")

  #area5 FLORESTA DOS CEM PASSOS

    if(area == 5):
      print("Você vê como a vegetação nativa é linda, porém densa o suficiente para não deixar você passar")
      machado = 0
      faca = 0

      for a in itens:
        if(a == 'machado'):
          machado = 1
        elif(a == 'faca'):
          faca = 1

      if(faca == 1 and machado == 0):
        print("Você corta o mato para tentar atravessar a floresta")
        itens.remove('faca')
        floresta.append('faca')
        print("Você ganhou grama!")
        itens.append('grama')
        itensGet.append('grama')
        area = 17

      elif(faca == 1 and machado == 1):
        print("Você pode usar o machado ou a faca para passar")
        print("Qual você escolhe?(machado/faca)")
        inputi = input("")
        
        if(inputi == "machado"):
          print("Você corta as árvores para tentar passar")
          itens.remove('machado')
          floresta.append('madeira')
          itens.append('madeira')
          itensGet.append('madeira')
          print("Você ganhou madeira!")
          print("")
          print("GIGANTE GUARDIÃO")
          print("")
          area = 17

        elif(inputi == "faca"):
          print("Você corta o mato para tentar atravessar a floresta")
          itens.remove('faca')
          floresta.append('faca')
          print("Você ganhou grama!")
          itens.append('grama')
          itensGet.append('grama')
          print("")
          print("GIGANTE GUARDIÃO")
          print("")
          area = 17

        else:
          print("escolha uma opção dentre as mencionadas entre parenteses")

      elif(faca == 0 and machado == 1):
        print("Você corta as árvores para tentar passar")
        itens.remove('machado')
        itens.append('madeira')
        itensGet.append('madeira')
        floresta.append('madeira')
        print("Você ganhou madeira!")
        print("")
        print("GIGANTE GUARDIÃO")
        print("")
        area = 17

      elif(faca == 0 and machado == 0):
        print("Nada por aqui")
        print("")
        print("ESTRADA")
        area = 2

  #area6 TOPO DA MONTANHA ANCESTRAL

    if(area == 6):
      machadoGet = 0
      for(i) in itensGet:
        if(i == 'machado'):
            machadoGet = 1
      if(machadoGet == 0):
            print("Você vê um machado, você quer pegá-lo?")
            inputi = input("")
            
            if(inputi == "s"):
              itens.append("machado")
              itensGet.append("machado")
              print("Você ganhou um machado")
                
            elif(input == "n"):
              print("")
              print("MONTANHA ANCESTRAL")
              print("")
              area = 3

      elif(machadoGet == 1):
        print("nada aqui")
        print("")
        print("MONTANHA ANCESTRAL")
        print("")
        area = 3

  #area7 CAVERNA DOS MEDOS MEDONHOS

    if(area == 7):
      print("Você entra, vê uma pilha de rochas e uma pessoa que parece estar perdida")
      print("O que você quer ver?Ou quer voltar?(pedras/pessoa/voltar)")
      inputi = input("")

      if(inputi == "pessoa"):
        print("")
        print("ARQUEÓLOGA")
        print("")        
        area = 13
      
      elif(inputi == "pedras"):
        if(passagemAberta == 0):

          picareta = 0
          for a in itens:
            if(a == 'picareta'):
              picareta = 1
        
          if(picareta == 0):
            print("Elas estão bloqueando a passagem da caverna, se eu quiser cristais vou ter que quebrá-las primeiro")
            print("Você quer voltar?")
            inputi = input("")

            if(inputi == "s"):
              print("")
              print("MONTANHA ANCESTRAL")
              print("")
              area = 3
            
            elif(inputi != "n"):
              print("escolha uma opção dentre as mencionadas entre parenteses")

          elif(picareta == 1):
            print("Você quer quebrá-las?")
            inputi = input("")

            if(inputi == "s"):
              passagemAberta = 1
              itens.remove('picareta')
            
            elif(inputi != "n"):
              print("escolha uma opção dentre as mencionadas entre parenteses")
        
        elif(passagemAberta == 1):
          print("Está escuro lá")
          print("Você quer mesmo entrar?")
          inputi = input("")

          if(inputi == "s"):
            tocha = 0

            for a in itens:
              if(a == 'tocha'):
                tocha = 1
            
            if(tocha == 1):
              print("")
              print("FUNDO DA CAVERNA DOS MEDOS MEDONHOS")
              print("")
              area == 14
            
            elif(tocha == 0):
              area = 16
          
          elif(inputi != "n"):
            print("escolha uma opção dentre as mencionadas entre parenteses")
      
      elif(inputi == "voltar"):
        print("Você quer voltar?")
        inputi = input("")

        if(inputi == "s"):
          print("")
          print("MONTANHA ANCESTRAL")
          print("")
          area = 3
        
        elif(inputi != "n"):
          print("escolha uma opção dentre as mencionadas entre parenteses")

  #area8 AÇOUGUEIRO (parei aqui itensGet e areas) 

    if(area == 8):
      facao = 0
      acougueiro = 0

      for a in range(0,len(itens)):
        if(itens[a] == 'facão'):
          facao = 1

      for a in quests:
        if(a == 'açougueiro'):
          acougueiro = 1

      if(facao == 1):
        print("Você pode dar o facão ou voltar(facão/voltar)")
        inputi = input("")
        
        if(inputi == "facão"):
          print("Obrigado, você me ajudou muito!!!")
          print("Aqui está, pegue este osso que achei por aí, deve servir para alguma coisa...")
          itens.remove('facão')
          itens.append("osso")
          quests.append("açougueiro")

        elif(inputi == "voltar"):
          area = 4

        else:
          print("escolha uma opção dentre as mencionadas entre parenteses")

      elif(facao == 0 and acougueiro == 0):
        print("Ah, finalmente, perdi meu facão, preciso muito dele. Se você o encontrar você pode me devolver, porfavorzinho? Eu posso te recompensar!")
        print("Mais nada por aqui")
        print("Você quer voltar?")
        inputi = input("")
        
        if(inputi == "s"):
          area = 4
        
        elif(inputi != "n"):
          print("escolha uma opção dentre as mencionadas entre parenteses")

      elif(acougueiro == 1):
        print("Mais nada por aqui")
        print("Você quer voltar?")
        inputi = input("")
        
        if(inputi == "s"):
          area = 4
        
        elif(inputi != "n"):
          print("escolha uma opção dentre as mencionadas entre parenteses")

  #area9 CARPINTEIRO

    if(area == 9):
      print("")
      print("CARPINTEIRO")
      print("")
      print("Ah, você está aí, preciso de madeira e grama para um novo prejeto...")
      print("Poderia me ajudar?")

      madeira = 0
      grama = 0
      for a in range(0,len(itens)):
        if(itens[a] == 'madeira'):
          madeira = 1
        
        if(itens[a] == 'grama'):
          grama = 1

      if(madeira == 1 and grama == 1):
        print("Você vai dar a madeira e a grama ou voltar? (madeira/voltar)")
        inputi = input("")
        
        if(inputi == "madeira"):
          print("Obrigado, agora eu acabo essa escultura!!!")
          print("Aceite essa picareta como recompensa...")
          itens.remove('madeira')
          itens.remove('grama')
          itens.append('picareta')
          quests.append("carpinteiro")
          area = 4 

        elif(inputi == "voltar"):
          area = 4

        else:
          print("escolha uma opção dentre as mencionadas entre parenteses")  
      print("Mais nada por aqui")
      print("Você quer voltar?")
      inputi = input("")
      
      if(inputi == "s"):
        area = 4
      
      elif(inputi != "n"):
        print("escolha uma opção dentre as mencionadas entre parenteses")

  #area10 MINERADOR

    if(area == 10):
      print("")
      print("MINERADOR")
      print("")
      print("Sabe aquele cara que vigia o portal???")
      print("Se você quer passar por ele vai precisar de algo que eu tenho...")
      print("Se você pegar diamantes na caverna para mim pooso te dar essa raridade")
      
      diamantes = 0
      for a in range(0,len(itens)):
        if(itens[a] == 'diamantes'):
          diamantes = 1
      
      if(diamantes == 1):
        print("Você quer dar os diamantes?")
        inputi = input("")
        
        if(inputi == "s"):
          print("Obrigado, agora estou rico!!!")
          print("Pegue, esse é o sonífero mais forte de todos, é o unico jeito de fazer aquela coruja com olhos de águi dormir...")
          itens.remove('diamantes')
          itens.append('sonífero')
          quests.append('minerador')
        
        elif(inputi != "n"):
          print("escolha uma opção dentre as mencionadas entre parenteses")
      
      else:
        print("Você quer voltar?")
        inputi = input("")
        
        if(inputi == "s"):
          area = 4
        
        elif(inputi != "n"):
          print("escolha uma opção dentre as mencionadas entre parenteses")

  #area11 CARA MISTERIOSO
  
    if(area == 11):
      print("")
      print("CARA MISTERIOSO")
      print("")
      print("Oi, eu sou o guardião do portal, e daqui você não passa!!!")

      facao = 0
      sonifero = 0
      for (a) in itensGet:
        if(a == 'facão'):
          facao = 1
      
        if(a == 'sonífero'):
          sonifero = 1
      
      if(facao == 0):
        print("Ah, eu achei esse facão, pode ficar para você, eu não sei de quem é mesmo")
        print("Você ganhou um facão")
        area = 4
      
      elif(sonifero == 1):
        print("Você vai usar esse sonífero para fazer ele dormir")

        itens.remove('sonífero')
        print("Zzzzzzzzzzzzzzz...")
        print("Ele dormiu e muito, vamos passar pelo portal !!!")
        print("Você passa pelo portal...")
        winat1 = 1
      
      else:
        area = 4

  #area12 LAGOA CALMA DA PROPAGAÇÃO DA PAZ
    
    if(area == 12):  
      print("")
      print("LAGOA CALMA DA PROPAGAÇÃO DA PAZ")
      print("")
      print("Você vê um cara pescando")
      print("Você quer voltar ou falar com ele?(voltar/falar)")
      inputi = input("")

      if(inputi == "voltar"):
        area = 5

      elif(inputi == "falar"):
        area = 15
      else:
        print("escolha uma opção dentre as mencionadas entre parenteses")

  #area13 ARQUEÓLOGA

    if(area == 13):
      print("")
      print("ARQUEÓLOGA")
      print("")
      acougueiro = 0
      tocha = 0

      for a in itens:
        if(a == 'tocha'):
          tocha = 1

      for a in quests:
        if(a == "açougueiro"):
          acougueiro = 1

      if(acougueiro == 0):
        print("Oi, quem é você?")
        print("-O que você está fazendo aqui?")
        print("Vim procurar o último osso de dinossauro que falta para eu ter ele completo...")
        print("Já olhei por toda Antycot e não achei ainda, Acredita?")
        print("Você me ajuda a procurar?")
        print("Você quer voltar?")
        inputi = input("")
        
        if(inputi == "s"):
          area = 7
        
        elif(inputi != "n"):
          print("escolha uma opção dentre as mencionadas entre parenteses")

      elif(acougueiro == 1 and tocha == 0):
        print("Você quer dar o osso à ela?")
        inputi = input("")
        
        if(inputi == "s"):
          print("Obrigada, não sabe como isso é importante para mim")
          print("Aqui, leve esta tocha caso voc~e queira entrar na caverna, lá é realmente bem escuro")
          print("Agora que eu não preciso mais ir lá pode ficar para você")
          itens.remove('osso')
          itens.append("tocha")
          quests.append("arqueóloga")
        
        elif(inputi != "n"):
          print("escolha uma opção dentre as mencionadas entre parenteses")
      
      elif(acougueiro == 1 and tocha == 1):
        print("Mais nada para fazer aqui")
        print("Você quer voltar?")
        inputi = input("")
        
        if(inputi == "s"):
          area = 7
        
        elif(inputi != "n"):
          print("escolha uma opção dentre as mencionadas entre parenteses")

  #area14 FUNDO DA CAVERNA DOS MEDOS MEDONHOS

    if(area == 12):  
      print("")
      print("FUNDO DA CAVERNA DOS MEDOS MEDONHOS")
      print("")
      diamantes = 0
      for a in itens:
        if(a == 'diamantes'):
          diamantes = 1
      if(diamantes == 0):
        inputi = input("")
        print("Você vê diamantes, você quer pegá-los?")
        if(inputi == "s"):
          itens.append("diamantes")
          itens.remove("picareta")
      
      else:
        print("Mais nada aqui")

  #area15 PESCADOR

    if(area == 15):  
      print("")
      print("PESCADOR")
      print("")
      print("OI, VoC^e VaI pArA a CaBanA In1c1aL m3SmO QUe n40 qU31R4 H4H4H4")
      area = 1

  #area16 MORCEGOS
  
    if(area == 16):
      print("Um novo morcego selvagem apareceu")
      print("Você quer atacá-lo?")
      inputi = input("")

      if(inputi == "s"):
        print("O morcego é mais forte do que você pensa...")
        print("tchau, {}".format(nome))
        looseat1 = 1

      elif(inputi == "n"):
        print("Ele te ataca e você morre")
        print("tchau, {}".format(nome))
        looseat1 = 1
      
      else:
        print("escreve direito poxa")

  #area 17 GIGANTE GUARDIÃO

    if(area == 17):
      print("Por favor espere, não seja tão afobado, apenas respire fundo, sinta essa paz vindo...")
      print("Se você quiser passar vai ter que responder um enígma milenar")
      print("O que é, o que é, de dia tem 4 pernas, de tarde tem 2 e de noite tem 3?")
      inputi = input("")

      if(inputi == "humano"):
        print("Como és esperto, pode passar adiante, vá para a lagoa, mas cuidado...!")
        area = 12
      else:
        print("errou, tente novamente")
else:
  print("tchau, {}".format(nome))
if(winat1 == 1):
  print("PARABÉNS {}, VOCÊ GANHOU".format(nome))