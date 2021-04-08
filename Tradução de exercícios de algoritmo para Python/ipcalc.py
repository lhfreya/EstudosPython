def calcip():


     ip = input('Digite o IP:')
     prefixo = int(input('Digite o Prefixo:'))




     if prefixo == 8:
        print("O endereço IP:", ip, " pertence a classe A")
        print("A mascara padrão é 255.0.0.0")

     if prefixo == 16:
        print("O endereço IP:", ip, " pertence a classe B")
        print("A mascara padrão é 255.255.0.0")

     while prefixo >= 24 and prefixo <= 30:

         print("O endereço IP:", ip, " pertence a classe C")
         print("Mascara de rede padrão: 255.255.255.0")

         if prefixo == 25:
            print("Quantidade de sub-redes: 2 ")
            print("Hosts válidos: 126")
            print("Mascara de sub-rede: 255.255.255.128 /25")

         if prefixo == 26:
            print("Quantidade de sub-redes: 4 ")
            print("Hosts válidos: 62")
            print("Mascara de sub-rede: 255.255.255.192 /26")

         if prefixo == 27:
            print("Quantidade de sub-redes: 8 ")
            print("Hosts válidos: 30")
            print("Mascara de sub-rede: 255.255.255.224 /27")

         if prefixo == 28:
            print("Quantidade de sub-redes: 16 ")
            print("Hosts válidos: 14")
            print("Mascara de sub-rede: 255.255.255.240 /28")

         if prefixo == 29:
            print("Quantidade de sub-redes: 32 ")
            print("Hosts válidos: 6")
            print("Mascara de sub-rede: 255.255.255.248 /29")

         if prefixo == 30:
            print("Quantidade de sub-redes: 64 ")
            print("Hosts válidos: 2")
            print("Mascara de sub-rede: 255.255.255.252 /30")


         break


calcip()