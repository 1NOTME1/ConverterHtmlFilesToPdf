#KONWERSJA PLIKOW HTML NA PDF
import os
import subprocess

def convert_html_to_pdf(html_file, pdf_file):
    try:
        subprocess.run(['wkhtmltopdf', html_file, pdf_file])
        print(f"Plik PDF {pdf_file} został pomyślnie utworzony.")
    except Exception as e:
        print(f"Wystąpił błąd podczas konwersji: {str(e)}")

def convert_html_files_to_pdf(input_file_path, output_dir):
    with open(input_file_path, 'r') as file:
        html_files = file.readlines()

    for html_file in html_files:
        html_file = html_file.strip()
        pdf_file = os.path.join(output_dir, os.path.basename(html_file).replace('.html', '.pdf'))
        convert_html_to_pdf(html_file, pdf_file)

input_file_path = r"C:\Users\USER_NAME\Desktop\html2pdf\sciezki_do_plikow_html.txt"
output_dir = r"C:\Users\USER_NAME\Desktop\html2pdf\pdf_from_html"
convert_html_files_to_pdf(input_file_path, output_dir)
