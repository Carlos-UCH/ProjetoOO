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
        if isinstance(novas_equacoes, list):
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

        #Verificar se o arquivo já existe
        if os.path.exists(caminho):
            with open(caminho, "r") as arquivo:
                try:
                    dados_exs = json.load(arquivo)
                except json.JSONDecodeError:
                    dados_exs = []
        else:
            dados_exs = []
        
        #Adicionar equações
        dados = []

        for equacao in self.__equacoes:
            resultado = equacao.resultado

            if isinstance(resultado, complex):
                resultado = {"real": resultado.real, "imag": resultado.imag}
            elif isinstance(resultado, (list, tuple)):
                resultado = [
                    {"real": r.real, "imag": r.imag} if isinstance(r, complex) else r
                    for r in resultado
                        ]
            dados.append({
                "tipo": equacao.__class__.__name__,
                "coeficientes": equacao.coeficientes,
                "resultado": equacao.resultado
                })

        #combinar dados existentes com novos dados
        for novo in dados:
            if novo not in dados_exs:
                dados_exs.append(novo)

        with open(caminho, "w") as arquivo:
            json.dump(dados, arquivo, indent=4)
        print(f"Equações salvas em {caminho}")

    #Carregar equações de um arquivo JSON
    def carregar_de_json(self, caminho="equacoes.json"):
        
        if not os.path.exists(caminho):
            print(f"Arquivo {caminho} não encontrado")
            return

        with open(caminho, "r") as arquivo:
            try:
                dados = json.load(arquivo)
            except json.JSONDecodeError:
                return  

        self.__equacoes = []

        for item in dados:
            tipo = item["tipo"]
            coeficientes = item["coeficientes"]
            resultado = item["resultado"]
           
            #Para números complexos

            if isinstance(resultado, dict) and "real" in resultado and "imag" in resultado:
                resultado = complex(resultado["real"], resultado["imag"])
            elif isinstance(resultado, list):
                resultado = [
                    complex(r["real"], r["imag"]) if isinstance(r, dict) else r
                    for r in resultado
                ]

            print("")
            print(f"Tipo: {tipo}")
            print(f"Coeficiente(s): {coeficientes}")
            print(f"Resultado: {resultado}")
            if tipo == "EqPrimeiroGrau":
                self.__equacoes.append(EqPrimeiroGrau(*coeficientes))
            elif tipo == "EqSegundoGrau":
                self.__equacoes.append(EqSegundoGrau(*coeficientes))
            elif tipo == "EqTerceiroGrau":
                self.__equacoes.append(EqTerceiroGrau(*coeficientes))
           

    def carregar_de_json_f(self, caminho="equacoes.json"):
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
            print("0. *CASO FECHOU O PROGRAMA (CARREGAR)*")
            print("1. Adicionar Equações")
            print("2. Calcular Equações e Gerar PDF")
            print("3. Salvar Equações em JSON")
            print("4. Equações anteriores")
            print("5. Sair")
            
            opcao = input("Escolha uma opção (1-5): ")
            
            if opcao == "0":
                self.carregar_de_json_f()
            elif opcao == "1":
                self.adicionar_equacao_via_terminal()
            elif opcao == "2":
                self.calcular_todas()
                self.gerar_pdf()
                print("Relátorio dos resultados gerado")
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
        print("\nTipos de equação:")
        primeiro = print("1. Primeiro Grau(ax + b = 0)")
        segundo = print("2. Segundo Grau(ax^2 + bx + c = 0)")
        terceiro = print("3. Terceiro Grau(ax^3 + bx^2 + cx + d = 0)")
        
        grau = input("Digite o grau da equação (1, 2, 3): ").strip()
        
        if grau == "1":
            tipo = "primeiro"
        elif grau == "2":
            tipo = "segundo"
        elif grau == "3":
            tipo = "terceiro"
        else:
            print("Grau inválido")
            return
        
        #tipo = input("Digite o tipo de equação (primeiro, segundo, terceiro): ").strip().lower()
        coeficientes = input("Digite os coeficientes separados por espaço: ").strip().split()
        coeficientes = list(map(float, coeficientes))
        self.adicionar_equacao(tipo, coeficientes)


