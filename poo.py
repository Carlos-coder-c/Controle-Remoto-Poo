class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
         self.cor = cor
         self.altura = altura
         self.profundidade = profundidade
         self.largura = largura
    def mexer_canal(self, botao): 
         if botao == "+":
           print("Passou mais um canal")
         elif botao == "-":
           print("Voltou mais um canal")
    def mexer_volume(self, botao2):
         
         if botao2 == "+":
            print("Som aumentado por 1+")
          
         elif botao2 == "-":
             print("1- menos um de volume")

    def desligar_tv(self, botao_desligar):
        
         if botao_desligar == ".":
             print("Você desligou sua tv")

      

  
controle_remoto =  ControleRemoto("preto", "10cm", "2cm", "2cm")
print("Meu controle remoto tem as seguintes caracteristicas: ")
print(controle_remoto.cor)
print(controle_remoto.altura)
print(controle_remoto.profundidade)
print(controle_remoto.largura)


print("+ passar e aumentar volume, - diminuir volume e voltar canal")
controle_remoto.mexer_canal("+")
controle_remoto.mexer_volume("+")
controle_remoto.desligar_tv(".")

print("Controle remoto 2")
controle_remoto =  ControleRemoto("cinza", "12cm", "5cm", "5cm")
print("Caracteristicas: ")
print(controle_remoto.cor)
print(controle_remoto.altura)
print(controle_remoto.profundidade)
print(controle_remoto.largura)

print("+ passar e aumentar volume, - diminuir volume e voltar canal")

controle_remoto.mexer_canal("-")
controle_remoto.mexer_volume("-")
controle_remoto.desligar_tv("")
