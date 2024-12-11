from equacao import EqPrimeiroGrau, EqSegundoGrau, EqTerceiroGrau
from geradorpdf.geradorpdf import GeradorPDF

if __name__ == "__main__":
    eq1 = EqPrimeiroGrau(2, -4)
    eq2 = EqSegundoGrau(1, -3, 2)
    eq3 = EqTerceiroGrau(1, -6, 11, -6)
    
    eq1.calcular()
    eq2.calcular()
    eq3.calcular()

    geradorpdf = GeradorPDF()
    geradorpdf.gerar_pdf([eq1, eq2, eq3])
