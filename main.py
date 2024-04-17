class AutomatoFinitoDeterministico:
    def __init__(self, alfabeto, estados, estado_inicial, estados_finais, regras_transicao):
        self.alfabeto = alfabeto
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.regras_transicao = regras_transicao
        self.verifica_automato()
    
    def verifica_automato(self):
        
        assert self.estado_inicial in self.estados, \
            "O estado inicial DEVE fazer parte do conjunto de estados"
        
        assert all(estado_inicial in self.estados and prox_estado in self.estados 
                   for estado_inicial, _, prox_estado in self.regras_transicao), \
                   "Regra de transição possui algum estado inválido"
        
        assert all(simbolo in self.alfabeto for _, simbolo, _ in self.regras_transicao), \
                    "Regra de transição possui algum símbolo inválido"
    

    def faz_transicao(self, estado, simbolo):

        for inicial, s, prox_estado in self.regras_transicao:
            if inicial == estado and s == simbolo:
                return prox_estado
        return None
    
    def verifica_palavras(self, palavras):

        estado_atual = self.estado_inicial

        for simbolo in palavras:

            if simbolo not in self.alfabeto:
                return "INVALIDA"
            
            prox_estado = self.faz_transicao(estado_atual, simbolo)
            if prox_estado == None:
                return "REJEITA"
            
            estado_atual = prox_estado

        if prox_estado in self.estados_finais:
            return "ACEITA"
        else:
            return "REJEITA"
    
    def resultados(self, palavras):
        
        resultados = []

        for palavra in palavras:
            resposta = self.verifica_palavras(palavra)
            resultados.append((palavra, resposta))
        return resultados        
            


# Definição automato finito deterministico
alfabeto = {'a', 'b'}
estados =  {'q0', 'q1', 'q2', 'q3'}
estado_inicial = 'q0'
estados_finais = {'q3'}
regras_transicao = [
    ('q0', 'a', 'q1'),
    ('q0', 'b', 'q2'),
    ('q1', 'a', 'q3'),
    ('q1', 'b', 'q2'),
    ('q2', 'a', 'q1'),
    ('q2', 'b', 'q3'),
    ('q3', 'a', 'q3'),
    ('q3', 'b', 'q3')
]

# Minhas Palavras
palavras = ['aaa', 'ab', 'babb', 'abc', 'abababa']

# Meu autômato
automato = AutomatoFinitoDeterministico(alfabeto, estados, estado_inicial, estados_finais, regras_transicao)

# Verificando as palavras no autômato
verificando = automato.resultados(palavras)

for palavra, resultado in verificando:
    print(f"A palavra {palavra} = {resultado}")