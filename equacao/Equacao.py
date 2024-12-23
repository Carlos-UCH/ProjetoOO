from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import os
import math
import cmath

# Pasta dos gráficos
pastagraficos = os.path.join(os.path.dirname(__file__), '..', 'graficos')
os.makedirs(pastagraficos, exist_ok=True)

class Equacao(ABC): 
    def __init__(self, *coeficientes):
        self.coeficientes = coeficientes
        self.resultado = None

    @abstractmethod
    def calcular(self):
        pass
    
    @abstractmethod
    def plotar_grafico(self):
        pass

class EqPrimeiroGrau(Equacao):
    def calcular(self):
        a, b = self.coeficientes

        if a == 0:
            return "O coeficiente 'a' não pode ser zero."

        self.resultado = -b / a

        if self.resultado < 0:
            return f"A raiz é negativa: {self.resultado}"
        else:
            return f"A raiz é positiva: {self.resultado}"
        
    def plotar_grafico(self):
        a, b = self.coeficientes
        x = [i for i in range(-10, 11)]
        y = [a * i + b for i in x]
        plt.plot(x, y, label=f'{a}x + {b}')
        plt.axhline(0, color='black', lw=0.5)
        plt.axvline(0, color='black', lw=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.title('Gráfico da equação de primeiro grau')
        plt.xlabel("x")
        plt.ylabel("y")

        nome_1grau = 'grafico_primeiro_grau'
        nome_1grau_arquivo = f'{nome_1grau}.png'

        grafico_path = os.path.join(pastagraficos, nome_1grau_arquivo)
        cont = 1
        while os.path.exists(grafico_path):
            nome_1grau_arquivo = f'{nome_1grau}_{cont}.png'
            grafico_path = os.path.join(pastagraficos, nome_1grau_arquivo)
            cont += 1
        plt.savefig(grafico_path)
        plt.close()
        return grafico_path

class EqSegundoGrau(Equacao):
    def calcular(self):
        a, b, c = self.coeficientes
        delta = b**2 - 4*a*c
        
        if delta < 0:
            x1 = (-b + cmath.sqrt(delta)) / (2*a)
            x2 = (-b - cmath.sqrt(delta)) / (2*a)
            self.resultado = (self.format_complex_result(x1), self.format_complex_result(x2))
            return f"Raízes complexas: resultado"
        elif delta == 0:
            self.resultado = -b / (2*a)
            return f"Raiz única: {self.resultado}"
        else:
            x1 = (-b + delta**0.5) / (2*a)
            x2 = (-b - delta**0.5) / (2*a)
            self.resultado = (x1, x2)
            return f"Raízes reais: {x1}, {x2}"
    def format_complex_result(self, x):
        if isinstance(x, complex):
            return f"{x.real:.2f} + {x.imag:.2f}i" if x.imag >= 0 else f"{x.real:.2f} - {abs(x.imag):.2f}i"
        return x
    def plotar_grafico(self):
        a, b, c = self.coeficientes
        x = [i for i in range(-10, 11)]
        y = [a * i**2 + b * i + c for i in x]
        plt.plot(x, y, label=f'{a:+}x² {b:+}x {c:+}')
        plt.axhline(0, color='black', lw=0.5)
        plt.axvline(0, color='black', lw=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.title('Gráfico da equação de segundo grau')
        plt.xlabel("x")
        plt.ylabel("y")

        nome_2grau = 'grafico_segundo_grau'
        nome_2grau_arquivo = f'{nome_2grau}.png'

        grafico_path = os.path.join(pastagraficos, nome_2grau_arquivo)
        cont = 1
        while os.path.exists(grafico_path):
            nome_2grau_arquivo = f'{nome_2grau}_{cont}.png'
            grafico_path = os.path.join(pastagraficos, nome_2grau_arquivo)
            cont += 1

        plt.savefig(grafico_path)
        plt.close()
        return grafico_path

class EqTerceiroGrau(Equacao):

    @staticmethod
    def format_complex_result(real_part, im_part):
        # Formatação do resultado de raízes complexas
        if real_part == 0 and im_part == 0:
            return "0"

        number = ""

        if real_part != 0:
            number += f"{real_part:.2f}"

        if im_part > 0:
            number += f"+{im_part:.2f}i"
        elif im_part < 0:
            number += f"{im_part:.2f}i"
        elif real_part == 0:
            number = f"{im_part:.2f}i"

        return number

    def calcular(self):
        a, b, c, d = self.coeficientes
        
        if a == 0:
            return "O coeficiente 'a' não pode ser zero."

        roots = []

        A = b / a
        B = c / a
        C = d / a

        p = B - A**2 / 3
        q = C + 2 * A**3 / 27 - A * B / 3

        # Discriminante
        delta = q**2 / 4 + p**3 / 27

        if delta >= 0:
            y1 = (-q / 2 + math.sqrt(delta))**(1/3) + (-q / 2 - math.sqrt(delta))**(1/3)
            roots.append(f"{(y1 - A / 3):.2f}")

            delta2 = -3 * y1**2 - 4 * p
            
            if delta2.imag == 0:
                if delta2.real > 0:
                    roots.append(f"{((-y1 + math.sqrt(delta2)) / 2 - A / 3):.2f}")
                    roots.append(f"{((-y1 - math.sqrt(delta2)) / 2 - A / 3):.2f}")
                else:
                    roots.append("Raízes complexas")
            else:
                # Raízes complexas
                real_part = -y1 / 2
                im_part = math.sqrt(abs(delta2)) / 2

                roots.append(self.format_complex_result(real_part - A / 3, im_part))
                roots.append(self.format_complex_result(real_part - A / 3, -im_part))
        else:
            # Euler
            rho = math.sqrt(q**2 / 4 + abs(delta))
            theta = math.acos(-q / (2 * rho))
            roots.append(str(f"{(2 * (rho**(1/3)) * math.cos((theta / 3) - A / 3)):.1f}"))
            roots.append(str(f"{(2 * (rho**(1/3)) * math.cos((theta + 2 * math.pi) / 3) - A / 3):.1f}"))
            roots.append(str(f"{(2 * (rho**(1/3)) * math.cos((theta + 4 * math.pi) / 3) - A / 3):.1f}"))
            
        self.resultado = roots

        if any("i" in root for root in roots):
            return f"Raízes complexas: {', '.join(roots)}"
        else:
            return f"Raízes reais: {', '.join(roots)}"

    def plotar_grafico(self):
        a, b, c, d = self.coeficientes
        x = [i for i in range(-10, 11)]
        y = [a * i**3 + b * i**2 + c * i + d for i in x]
        plt.plot(x, y, label=f'{a:+}x³ {b:+}x² {c:+}x {d:+}')
        plt.axhline(0, color='black', lw=0.5)
        plt.axvline(0, color='black', lw=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.title('Gráfico da equação de terceiro grau')
        plt.xlabel("x")
        plt.ylabel("y")

        nome_3grau = 'grafico_terceiro_grau'
        nome_3grau_arquivo = f'{nome_3grau}.png'

        grafico_path = os.path.join(pastagraficos, nome_3grau_arquivo)
        cont = 1
        while os.path.exists(grafico_path):
            nome_3grau_arquivo = f'{nome_3grau}_{cont}.png'
            grafico_path = os.path.join(pastagraficos, nome_3grau_arquivo)
            cont += 1

        plt.savefig(grafico_path)
        plt.close()
        return grafico_path
 
