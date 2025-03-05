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

'''
# Testes
#   
# Encontrar e remover a pergunta
pergunta_a_remover = Pergunta.encontrar_pergunta("Isto é uma pergunta teste!")
if pergunta_a_remover:
    pergunta_a_remover.remover_pergunta()

########################################
# Criar uma nova pergunta
pergunta1 = Pergunta(
    pergunta="Isto é uma pergunta teste!",
    opcoes=["1", "2", "3", "4"],
    resposta_certa="2",
    categoria="Geografia",
    dificuldade="Fácil",
    explicacao="A resposta certa é a 1."
)

# Adicionar a pergunta ao banco de perguntas
pergunta1.adicionar_pergunta()

# Exibir todas as perguntas
print("Perguntas após adicionar:")
for pergunta in perguntas_qz:
    p = Pergunta(
        pergunta=pergunta["pergunta"],
        opcoes=pergunta["opcoes"],
        resposta_certa=pergunta["resposta_certa"],
        categoria=pergunta["categoria"],
        dificuldade=pergunta["dificuldade"],
        explicacao=pergunta["explicacao"]
    )
    p.exibir_pergunta()
    print()

# Editar a pergunta
pergunta1.editar_pergunta(
    nova_pergunta="Qual é a capital da Alemanha?",
    novas_opcoes=["Paris", "Londres", "Berlim", "Madri"],
    nova_resposta_certa="Berlim",
    nova_categoria="Geografia",
    nova_dificuldade="Médio",
    nova_explicacao="Berlim é a capital e maior cidade da Alemanha."
)

# Exibir todas as perguntas após edição
print("Perguntas após edição:")
for pergunta in perguntas_qz:
    p = Pergunta(
        pergunta=pergunta["pergunta"],
        opcoes=pergunta["opcoes"],
        resposta_certa=pergunta["resposta_certa"],
        categoria=pergunta["categoria"],
        dificuldade=pergunta["dificuldade"],
        explicacao=pergunta["explicacao"]
    )
    p.exibir_pergunta()
    print()

# Remover a pergunta
pergunta1.remover_pergunta()

# Exibir todas as perguntas após remoção
print("Perguntas após remoção:")
for pergunta in perguntas_qz:
    p = Pergunta(
        pergunta=pergunta["pergunta"],
        opcoes=pergunta["opcoes"],
        resposta_certa=pergunta["resposta_certa"],
        categoria=pergunta["categoria"],
        dificuldade=pergunta["dificuldade"],
        explicacao=pergunta["explicacao"]
    )
    p.exibir_pergunta()
    print()

# Exibir todas as perguntas organizadas por categoria
print("Perguntas organizadas por categoria:")
perguntas_por_categoria = categoria_instance.organizar_perguntas_por_categoria()
for categoria, perguntas in perguntas_por_categoria.items():
    print(f"\nCategoria: {categoria}")
    for pergunta in perguntas:
        p = Pergunta(
            pergunta=pergunta["pergunta"],
            opcoes=pergunta["opcoes"],
            resposta_certa=pergunta["resposta_certa"],
            categoria=pergunta["categoria"],
            dificuldade=pergunta["dificuldade"],
            explicacao=pergunta["explicacao"]
        )
        p.exibir_pergunta()

# Exibir todas as perguntas organizadas por dificuldade
print("\nPerguntas organizadas por dificuldade:")
perguntas_por_dificuldade = categoria_instance.organizar_perguntas_por_dificuldade()
for dificuldade, perguntas in perguntas_por_dificuldade.items():
    print(f"\nDificuldade: {dificuldade}")
    for pergunta in perguntas:
        p = Pergunta(
            pergunta=pergunta["pergunta"],
            opcoes=pergunta["opcoes"],
            resposta_certa=pergunta["resposta_certa"],
            categoria=pergunta["categoria"],
            dificuldade=pergunta["dificuldade"],
            explicacao=pergunta["explicacao"]
        )
        p.exibir_pergunta()
'''