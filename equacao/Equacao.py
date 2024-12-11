from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import os


#pasta dos gráficos

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
        a,b = self.coeficientes
        self.resultado = -b/a
        return self.resultado
        
    def plotar_grafico(self):
        a,b = self.coeficientes
        x = [i for i in range(-10,11)]
        y = [a*i + b for i in x]
        plt.plot(x,y, label=f'{a}x + {b}')
        plt.axhline(0, color='black', lw=0.5)
        plt.axvline(0, color='black', lw=0.5)
        plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
        plt.legend()
        plt.title('Gráfico da equação de primeiro grau')
        plt.xlabel("x")
        plt.ylabel("y")
        grafico_path = os.path.join(pastagraficos, 'grafico_primeiro_grau.png')
        plt.savefig(grafico_path)
        plt.close()
        return grafico_path

class EqSegundoGrau(Equacao):
    def calcular(self):
        a,b,c = self.coeficientes
        delta = b**2 - 4*a*c
        if delta < 0:
            return "Não possui raízes reais"
        elif delta == 0:
            self.resultado = -b/(2*a)
            return self.resultado
        else:
            x1 = (-b + delta**0.5)/(2*a)
            x2 = (-b - delta**0.5)/(2*a)
            self.resultado = (x1,x2)
            return self.resultado
            
    def plotar_grafico(self):
            a,b,c = self.coeficientes
            delta = b**2 - 4*a*c

            if delta < 0:
                self.resultado = "Não possui raízes reais"
            elif delta == 0:
                self.resultado = -b/(2*a)
            else:
                x1 = (-b + delta**0.5)/(2*a)
                x2 = (-b - delta**0.5)/(2*a)
                self.resultado = (x1,x2)
            return self.resultado

    def plotar_grafico(self):
        a,b,c = self.coeficientes
        x = [i for i in range(-10,11)]
        y = [a*i**2 + b*i + c for i in x]
        plt.plot(x,y, label=f'{a}x² + {b}x + {c}')
        plt.axhline(0, color='black', lw=0.5)
        plt.axvline(0, color='black', lw=0.5)
        plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
        plt.legend()
        plt.title('Gráfico da equação de segundo grau')
        plt.xlabel("x")
        plt.ylabel("y")
        grafico_path = os.path.join(pastagraficos, 'grafico_segundo_grau.png')
        plt.savefig(grafico_path)
        plt.close()
        return grafico_path


    
class EqTerceiroGrau(Equacao):
    def calcular(self):
        a,b,c,d = self.coeficientes
        return "Não implementado"
        
    def plotar_grafico(self):
        a,b,c,d = self.coeficientes
        x = [i for i in range(-10,11)]
        y = [a*i**3 + b*i**2 + c*i + d for i in x]
        plt.plot(x,y, label=f'{a}x³ + {b}x² + {c}x + {d}')
        plt.axhline(0, color='black', lw=0.5)
        plt.axvline(0, color='black', lw=0.5)
        plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
        plt.legend()
        plt.title('Gráfico da equação de terceiro grau')
        plt.xlabel("x")
        plt.ylabel("y")
        grafico_path = os.path.join(pastagraficos, 'grafico_terceiro_grau.png')
        plt.savefig(grafico_path)
        plt.close()
        return grafico_path



