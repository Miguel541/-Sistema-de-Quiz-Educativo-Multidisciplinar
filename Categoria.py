from Perguntas_Quiz import perguntas_qz

class Categoria:
    def __init__(self):
        self.categorias = self.carregar_categorias()

    def carregar_categorias(self):
        # Cria um conjunto para armazenar categorias únicas
        categorias = set()
        # Itera sobre todas as perguntas
        for pergunta in perguntas_qz:
            # Adiciona a categoria ao conjunto
            # Se a categoria já estiver no conjunto, ela não será adicionada novamente
            categorias.add(pergunta['categoria'])
        # Converte o conjunto em uma lista e retorna
        # Fazemos isso porque conjuntos não têm uma ordem específica, mas listas têm
        return list(categorias)

    def organizar_perguntas_por_categoria(self):
        # Cria um dicionário vazio para armazenar perguntas organizadas por categoria
        perguntas_por_categoria = {}
        
        # Itera sobre todas as perguntas na lista perguntas_qz
        for pergunta in perguntas_qz:
            # Obtém a categoria da pergunta atual
            categoria = pergunta["categoria"]
            
            # Se a categoria ainda não estiver no dicionário, adiciona uma nova entrada com uma lista vazia
            if categoria not in perguntas_por_categoria:
                perguntas_por_categoria[categoria] = []
            
            # Adiciona a pergunta atual à lista correspondente à sua categoria
            perguntas_por_categoria[categoria].append(pergunta)
        
        # Retorna o dicionário com perguntas organizadas por categoria
        return perguntas_por_categoria

    def organizar_perguntas_por_dificuldade(self):
        # Cria um dicionário com chaves para cada nível de dificuldade e listas vazias como valores
        perguntas_por_dificuldade = {"Fácil": [], "Média": [], "Difícil": []}
        
        # Itera sobre todas as perguntas na lista perguntas_qz
        for pergunta in perguntas_qz:
            # Obtém a dificuldade da pergunta atual
            dificuldade = pergunta["dificuldade"]
            
            # Verifica se a dificuldade da pergunta está no dicionário
            if dificuldade in perguntas_por_dificuldade:
                # Adiciona a pergunta atual à lista correspondente à sua dificuldade
                perguntas_por_dificuldade[dificuldade].append(pergunta)
        
        # Retorna o dicionário com perguntas organizadas por dificuldade
        return perguntas_por_dificuldade

    def atualizar_categorias(self):
        self.categorias = self.carregar_categorias()

# Inicializar a instância de Categoria
categoria_instance = Categoria()