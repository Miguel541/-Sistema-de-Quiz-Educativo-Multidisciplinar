import random

class SessaoQuiz:
 
 def __init__(self, jogador ):
  self.jogador = jogador 
  self.pontos = 0  
  self.perguntas_respondidas = [ ]
  self.corretas = 0
  self.erros = 0   
  
 def escolher_pergunta (self , perguntas , categoria = None) : 
  dificuldade = self.definir_dificuldade ( ) 
  perguntas_disponiveis = [ ]
  for p in perguntas :
   if (not categoria or p.categoria == categoria ) :
    if p.dificuldade == dificuldade :
     perguntas_disponiveis.append (p)
  if len ( perguntas_disponiveis ) > 0 :
   escolha = random.choice (perguntas_disponiveis )
   return escolha 
  else :
   return None  
  
 def responder ( self , pergunta , resposta ) : 
  if resposta == pergunta.resposta : 
   self.pontos += 10 * pergunta.dificuldade 
   self.corretas += 1  
   return " Acertou! " 
  else : 
   self.erros += 1  
   return " Errou! "  +  pergunta.explicacao 
  
 def definir_dificuldade ( self ) : 
  if self.corretas > self.erros :  
   return 2   
  else :   
   return 1  
 
 def mostrar_pontos (self) :  
  resultado = " Pontos: "  +  str ( self.pontos )  
  resultado += " , Corretas: "  +  str ( self.corretas )  
  resultado += " , Erros: "  +  str ( self.erros )  
  return resultado  
  
 def estatisticas (self) :  
  total = self.corretas + self.erros   
  if total == 0:   
   return " Nenhuma pergunta respondida ainda. "   
  return " Taxa de acertos: "  +  str ( self.corretas / total * 100 )  +  "%"   
