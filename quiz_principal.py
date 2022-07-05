class QuizPrincipal:
    def __init__(self, q_questao) :
        self.numero_questao = 0
        self.lista_questao = q_questao
        self.pontuacao = 0
    
    def final_quiz(self):
        if(self.numero_questao < len(self.lista_questao)):
            return True
        else:
            print("Finalizado")
            print(f"Pontuacão final: {self.pontuacao}/{self.numero_questao}")

    def proxQuestao(self):
        questao_atual = self.lista_questao[self.numero_questao]
        self.numero_questao += 1
        resposta_usuario = input(f"Q.{self.numero_questao}: {questao_atual.texto}(True/False): ")
        self.conferir_resposta(resposta_usuario, questao_atual.resposta)
    
    def conferir_resposta(self, resposta_usuario, resposta_correta):
        if resposta_usuario.lower() == resposta_correta.lower():
            print("Você ACERTOU!")
            self.pontuacao += 1
        else:
            print("Errou!!!")
            print(f"Resposta certa: {resposta_correta}")
        
        print(f"Pontuacao atual: {self.pontuacao}/{self.numero_questao}\n")
