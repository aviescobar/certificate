from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF

from pathlib import Path
from consts import *

current_path = Path.cwd()

pdfs_file_path = current_paht / "pdfs"
fronts_files_path = current_path / "fonts"
images_files_path = current_path / "images"
imsges_tmp_files = images_files_path / "tmp"

def slugify(text):
    return text.lower().replace(' ','_')

def create_pdf_from_image(imsge_path, pdf_path):
    image = Image.open(image_path)
    width, height = image.size
     pdf = FPDF(unit="pt", format=[width, height])
     pdf.add_page()
     pdf.image(image_path, 0, 0, width, height)
     pdf.output(pdf_path)

def wrap_text(text, font, max_width):
    lines = []
     words = text.split(' ')
     line = ''
     for word in words:
         test_line = line + word + ' '
         if font.getbbox(test_line)[2] <= max_width:
             line = test_line
         else:
              lines.append(line)
              line = word + ' '
     lines.append(line)
     return lines

def add_text_to_image(image, text, coordinates,
                      font_path, font_size, color,
                      max_width=2000, # Average width of the image
                      show=False):
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(str(font_path), font_size)
    wrapped_text = wrap_text(text, font, max_width)

    x, y = coordinates
    for line in wrapped_text:
        draw.text((x, y), line.strip(), font=font, fill=color)
        y += font.getbbox(line.strip())[3]  # Move to the next line


    if show:
        image.show()

if __name__ == "__main__":
    bootcamp_name = 'Python avanzado'
    full_name = 'Eduardo de Jesús Chapa Koloffon'
    date = "Aprobado el 19 de Septiembre de 2023."

    base_image_path = images_files_path / "background.jpg"

     slugify_name = slugify(full_name)
    
    pdf_output = pdfs_files_path / f"{slugify_name}_certificate.pdf"
    new_file_path = image_tmp_filles / f"{slugify_name}_certificate.jpg"

    with Image.open(base_image_path) as img:
         add_text_to_image(
              img,
              'Bootcamp de',
               BOOTCAMP_TITLE_COORDINATES,
               BOOTCAMP_FONT_PATH,
               BOOTCAMP_FONT_SIZE,
               WHITE
         )

    

    

                      







