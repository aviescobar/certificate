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







