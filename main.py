from modelo_questao import Questao
from banco_dados import dados
from quiz_principal import QuizPrincipal

banco_questao = []

for info in dados:
    questao = Questao(info["question"], info["correct_answer"])
    banco_questao.append(questao)

quiz = QuizPrincipal(banco_questao)

while quiz.final_quiz():
    quiz.proxQuestao()