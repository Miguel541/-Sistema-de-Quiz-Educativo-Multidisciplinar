from Perguntas_Quiz import perguntas_qz
from Categoria import categoria_instance

class Pergunta:
    def __init__(self, pergunta, opcoes, resposta_certa, categoria, dificuldade, explicacao):
        self.pergunta = pergunta
        self.opcoes = opcoes
        self.resposta_certa = resposta_certa
        self.categoria = categoria
        self.dificuldade = dificuldade
        self.explicacao = explicacao

    def adicionar_pergunta(self):
        if self.categoria not in categoria_instance.categorias:
            categoria_instance.categorias.append(self.categoria)

        perguntas_qz.append({
            "pergunta": self.pergunta,
            "opcoes": self.opcoes,
            "resposta_certa": self.resposta_certa,
            "categoria": self.categoria,
            "dificuldade": self.dificuldade,
            "explicacao": self.explicacao
        })
        self.guardar_perguntas_no_arquivo()
        categoria_instance.atualizar_categorias()

    def remover_pergunta(self):
        for pergunta in perguntas_qz:
            if pergunta["pergunta"] == self.pergunta:
                perguntas_qz.remove(pergunta)
                self.guardar_perguntas_no_arquivo()
                categoria_instance.atualizar_categorias()
                break

    def editar_pergunta(self, pergunta, opcoes, resposta_certa, categoria, dificuldade, explicacao):
        for pergunta in perguntas_qz:
            if pergunta["pergunta"] == self.pergunta:
                pergunta["pergunta"] = pergunta
                pergunta["opcoes"] = opcoes
                pergunta["resposta_certa"] = resposta_certa
                pergunta["categoria"] = categoria
                pergunta["dificuldade"] = dificuldade
                pergunta["explicacao"] = explicacao
                self.guardar_perguntas_no_arquivo()
                categoria_instance.atualizar_categorias()
                break

    def exibir_pergunta(self):
        print(f"\n{self.pergunta}")
        for opcao in self.opcoes:
            print(f"- {opcao}") 

    def guardar_perguntas_no_arquivo(self):
        with open('Perguntas_Quiz.py', 'w', encoding='utf-8') as f:
            f.write("perguntas_qz = [\n")
            for pergunta in perguntas_qz:
                f.write("    {\n")
                f.write(f"        'pergunta': '{pergunta['pergunta']}',\n")
                f.write(f"        'opcoes': {pergunta['opcoes']},\n")
                f.write(f"        'resposta_certa': '{pergunta['resposta_certa']}',\n")
                f.write(f"        'categoria': '{pergunta['categoria']}',\n")
                f.write(f"        'dificuldade': '{pergunta['dificuldade']}',\n")
                f.write(f"        'explicacao': '{pergunta['explicacao']}'\n")
                f.write("    },\n")
            f.write("]\n")

    def encontrar_pergunta(texto_pergunta):
        for pergunta in perguntas_qz:
            if pergunta["pergunta"] == texto_pergunta:
                return Pergunta(
                    pergunta=pergunta["pergunta"],
                    opcoes=pergunta["opcoes"],
                    resposta_certa=pergunta["resposta_certa"],
                    categoria=pergunta["categoria"],
                    dificuldade=pergunta["dificuldade"],
                    explicacao=pergunta["explicacao"]
                )
        return None