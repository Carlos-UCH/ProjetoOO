from fpdf import FPDF
import os

#pasta resultado

pastaresultado = os.path.join(os.path.dirname(__file__), '..', 'graficos', 'resultados')
os.makedirs(pastaresultado, exist_ok=True)

class GeradorPDF:
    def gerar_pdf(self, equacoes):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(0, 10, "Resultado das equações", ln=True, align="C")
        pdf.ln(10)

        for i, equacao in enumerate(equacoes, start=1):
            pdf.cell(0, 10, f"Equação {i}: {equacao.coeficientes}", ln=True)
            pdf.cell(0, 10, f"Resultado: {equacao.resultado}", ln=True)
            grafico_path = equacao.plotar_grafico()
            pdf.image(grafico_path, x=10, w=100)
            pdf.ln(10)

        pdf.output(os.path.join(pastaresultado, "resultado.pdf"))

