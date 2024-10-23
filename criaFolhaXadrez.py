# Dimensões da folha A2 com sangria (reduzindo 0.5 cm para a margem de impressão)
import os
from reportlab.lib.pagesizes import A2
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas



width_A2, height_A2 = A2

margin = 0.5 * cm  # Sangria de 0.5 cm

square_size_5cm = 5 * cm  # Quadrados de 5 cm

script_dir = os.path.dirname(os.path.abspath(__file__))

# Criando o arquivo PDF para a folha A2

pdf_A2_path = os.path.join(script_dir, "chessboard_A2_5cm_squares.pdf")

c_A2 = canvas.Canvas(pdf_A2_path, pagesize=A2)



# Função para desenhar o padrão xadrez em uma folha A2

def draw_chessboard_A2(c):

    # Número de quadrados inteiros que cabem na folha A2 considerando a sangria

    num_rows = int((height_A2 - 2 * margin) // square_size_5cm)

    num_cols = int((width_A2 - 2 * margin) // square_size_5cm)



    # Desenhar o padrão xadrez

    for row in range(num_rows):

        for col in range(num_cols):

            if (row + col) % 2 == 0:

                x = col * square_size_5cm + margin

                y = row * square_size_5cm + margin

                c.rect(x, y, square_size_5cm, square_size_5cm, fill=1)



# Desenhar o padrão xadrez na folha A2

draw_chessboard_A2(c_A2)

c_A2.save()



pdf_A2_path