from Perguntas_Quiz import perguntas_qz

class Categoria:
    def __init__(self):
        self.categorias = self.carregar_categorias()

    def carregar_categorias(self):
        categorias = set()
        for pergunta in perguntas_qz:
            categorias.add(pergunta['categoria'])
        return list(categorias)

    def organizar_perguntas_por_categoria(self):
        perguntas_por_categoria = {}
        for pergunta in perguntas_qz:
            categoria = pergunta["categoria"]
            if categoria not in perguntas_por_categoria:
                perguntas_por_categoria[categoria] = []
            perguntas_por_categoria[categoria].append(pergunta)
        return perguntas_por_categoria

    def organizar_perguntas_por_dificuldade(self):
        perguntas_por_dificuldade = {"Fácil": [], "Média": [], "Difícil": []}
        for pergunta in perguntas_qz:
            dificuldade = pergunta["dificuldade"]
            if dificuldade in perguntas_por_dificuldade:
                perguntas_por_dificuldade[dificuldade].append(pergunta)
        return perguntas_por_dificuldade

    def atualizar_categorias(self):
        self.categorias = self.carregar_categorias()

# Inicializar a instância de Categoria
categoria_instance = Categoria()