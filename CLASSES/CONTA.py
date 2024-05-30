
class Conta():
    def __init__(self):
        msg="""
           Bem vindo, ao sistema bancário *ITY*
           Antes de mais nada precisaremos do seu nome para continuarmos com o processo!
           Agradeciria se apenas fornecesse os seus dados, uma vez que são confidiciais, o sistema está protegido e treinado para guarda-lo essas mesmas informações.Informações discenssárias serão discartadas!
           Obrigado

        """
        print(msg)

        self.ID = None
        self.estado = True
        self.saldo=0

        self.NOME = str(input('Qual é o seu nome?\n:'))
        self.BI = str(input('Qual é o seu bilhete de identidade?\n:'))
        self.TELF = int(input('Qual é o seu numero de telefone?\n:'))
        self.MORADA = str(input('Qual é a sua morada?\n:'))

    def Consultar(self):
        return self.saldo

    def Creditar(self): #colocar
        self.deposito=float(input('Quanto quer depositar?\n:'))
        self.saldo=self.saldo+self.deposito
        return self.saldo

    def Debitar(self): #retirar
        if self.saldo==0:
            print("O seu saldo é negativo")
        if  self.saldo<=10:
            print("O seu saldo é negativo;"
                  f"OBS: Na sua conta apenas tem saldo de {self.saldo} é inferior ao minimo, incluido a taxa de debito e outros serviços !")
        else:
            self.debito=float(input('Quanto quer debitar?\n:'))
            # self.caixa=10*self.debito/100 #tirar os 10%
            # self.debitoc=self.debito-self.caixa # e devolve os outros 90%
            self.saldo = self.saldo - self.debito
            return self.saldo
        return self.saldo

    def Transferir(self, valor, destino):
        self.Debitar()
        destino.Creditar()

                                             

















            # self.contat=10*self.depositoc/100(10*1000/100)

