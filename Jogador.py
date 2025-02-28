class Jogador:

    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0
        self.historico = []
        self.modo_jogo = "Treino"  

    def atualizar_pontuacao(self, pontos):
        self.pontuacao += pontos
        print(f"{self.nome} ganhou {pontos} pontos! Total: {self.pontuacao}")

    def registar_resposta(self, pergunta, correta):
        """Regista uma resposta no histórico do jogador."""
        self.historico.append({"pergunta": pergunta, "correta": correta})
        resultado = "Certa" if correta else "Errada"
        print(f"Resposta registada: {resultado}")

    def exibir_historico(self):
        """Exibe o histórico de desempenho do jogador."""
        print(f"\nHistórico de {self.nome}:")
        for item in self.historico:
            resultado = "Certa" if item["correta"] else "Errada"
            print(f"- {item['pergunta']}: {resultado}")

    def definir_modo_jogo(self, modo):
        """Define o modo de jogo do jogador."""
        modos_validos = ["Treino", "Contra-relógio", "Eliminatórias"]
        if modo in modos_validos:
            self.modo_jogo = modo
            print(f"Modo de jogo definido para: {modo}")
        else:
            print("Modo inválido! Escolha entre: Treino, Contra-relógio ou Eliminatórias.")

    def obter_perfil(self):
        """Retorna um resumo do perfil do jogador."""
        return {
            "Nome": self.nome,
            "Pontuação": self.pontuacao,
            "Modo de Jogo": self.modo_jogo,
            "Total de Perguntas Respondidas": len(self.historico)
        }
