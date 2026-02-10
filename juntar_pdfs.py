import PyPDF2 as pyf
from pathlib import Path

num_paginas = list(range(2, 35))
# Cria um novo arquivo PDF

novo_arquivo = pyf.PdfWriter()
for num in num_paginas:
    pagina_pdf = pyf.PdfReader(f"Manipular_pdf/paginas/Sumario/Arquivo Pagina {num}.pdf")
    novo_arquivo.add_page(pagina_pdf.pages[0])

    
with Path(f"C:/Ramiro/Cursos/TI/Desenvolvimento de Software/Python/Apostila Python/Separada/Modulo 1 ao 20/Sumario.pdf").open(mode="wb") as arquivo:
    novo_arquivo.write(arquivo)