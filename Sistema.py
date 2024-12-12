from equacao import EqPrimeiroGrau, EqSegundoGrau, EqTerceiroGrau
from geradorpdf.geradorpdf import GeradorPDF
import os 
import json

class Sistema:
    def __init__(self):
        self.__equacoes = []
        if not os.path.exists("graficos"):
            os.makedirs("graficos")

    
    #Getter
    def get_equacoes(self):
        return self.__equacoes
    #Setter
    def set_equacoes(self, novas_equacoes):
        if ininstance(novas_equacoes, list):
            self.__equacoes = novas_equacoes
        else: 
            raise ValueError("O valor passado não é uma lista")

    def adicionar_equacao(self, tipo, coeficientes):
        if tipo == "primeiro":
            self.__equacoes.append(EqPrimeiroGrau(*coeficientes))
        elif tipo == "segundo":
            self.__equacoes.append(EqSegundoGrau(*coeficientes))
        elif tipo == "terceiro":
            self.__equacoes.append(EqTerceiroGrau(*coeficientes))
        else:
            raise ValueError("Tipo de equação inválido")

    def calcular_todas(self):
        for equacao in self.__equacoes:
            equacao.calcular()
    def gerar_pdf(self):
        gerador_pdf = GeradorPDF()
        gerador_pdf.gerar_pdf(self.__equacoes)
    
    #SERIALIZAÇÃO JSON
    def salvar_em_json(self, caminho="equacoes.json"):
        dados = []

        for equacao in self.__equacoes:
            dados.append({
                "tipo": equacao.__class__.__name__,
                "coeficientes": equacao.coeficientes,
                "resultado": equacao.resultado
                })

        with open(caminho, "w") as arquivo:
            json.dump(dados, arquivo, indent=4)
        print(f"Equações salvas em {caminho}")

    #Carregar equações de um arquivo JSON
    def carregar_de_json(self, caminho="equacoes.json"):
        
        if not os.path.exists(caminho):
            print(f"Arquivo {caminho} não encontrado")
            return

        with open(caminho, "r") as arquivo:
            dados = json.load(arquivo)

        self.__equacoes = []

        for item in dados:
            tipo = item["tipo"]
            coeficientes = item["coeficientes"]

            if tipo == "EqPrimeiroGrau":
                self.__equacoes.append(EqPrimeiroGrau(*coeficientes))
            elif tipo == "EqSegundoGrau":
                self.__equacoes.append(EqSegundoGrau(*coeficientes))
            elif tipo == "EqTerceiroGrau":
                self.__equacoes.append(EqTerceiroGrau(*coeficientes))
            
        print(f"Equações carregadas de {caminho}")
    def executar(self):
        while True:
            print("\nMenu Principal:")
            print("1. Adicionar Equações")
            print("2. Calcular Equações e Gerar PDF")
            print("3. Salvar Equações em JSON")
            print("4. Carregar Equações de JSON")
            print("5. Sair")
            
            opcao = input("Escolha uma opção (1-5): ")

            if opcao == "1":
                self.adicionar_equacao_via_terminal()
            elif opcao == "2":
                self.calcular_todas()
                self.gerar_pdf()
            elif opcao == "3":
                self.salvar_em_json()
            elif opcao == "4":
                self.carregar_de_json()
            elif opcao == "5":
                print("Saindo...")
                break
            else:
                print("Opção inválida")
    def adicionar_equacao_via_terminal(self):
        tipo = input("Digite o tipo de equação (primeiro, segundo, terceiro): ").strip().lower()
        coeficientes = input("Digite os coeficientes separados por espaço: ").strip().split()
        coeficientes = list(map(float, coeficientes))
        self.adicionar_equacao(tipo, coeficientes)



















