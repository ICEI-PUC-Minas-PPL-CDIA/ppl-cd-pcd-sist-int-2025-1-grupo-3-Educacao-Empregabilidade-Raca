# Reimportar bibliotecas após reset
from pdf2image import convert_from_path
import os

# Recriar diretório para imagens
img_dir = "/mnt/data/img"
os.makedirs(img_dir, exist_ok=True)

# Caminhos dos PDFs reenviados
pdf_paths = {
    "state": "/mnt/data/relatorio_state_data_raca.pdf",
    "panorama": "/mnt/data/relatorio_completo_raca_panorama_2023.pdf"
}

# Converter páginas dos PDFs em imagens
image_paths = []

for label, path in pdf_paths.items():
    pages = convert_from_path(path, dpi=200)
    for i, page in enumerate(pages):
        img_path = f"{img_dir}/{label}_grafico_{i+1}.png"
        page.save(img_path, "PNG")
        image_paths.append((label, i+1, img_path))

image_paths
