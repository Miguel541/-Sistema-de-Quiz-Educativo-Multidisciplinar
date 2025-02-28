class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0
        self.historico = []
        
    def atualizar_pontuacao(self, pontos):
        self.pontuacao += pontos
        
    def registar_resposta(self, pergunta, correta):
        self.historico.append((pergunta, correta))
        
    def exibir_historico(self):
        print(f"\nHistórico de {self.nome}:")
        for pergunta, correta in self.historico:
            resultado = "Certa" if correta else "Errada"
            print(f"- {pergunta}: {resultado}")