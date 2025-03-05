import pypandoc
import yaml
import os
import time

# Load the config file
with open('resume.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)

source_file = config['source']
pdf_output = config['output']['pdf']
docx_output = config['output']['word']
font_size = config['output']['format']['font-size']
margins = config['output']['format']['margins']

# Ensure we're working in the current directory
current_dir = os.getcwd()
pdf_path = os.path.join(current_dir, pdf_output)
docx_path = os.path.join(current_dir, docx_output)

# Pandoc arguments for PDF
pdf_args = [
    '--pdf-engine=pdflatex',
    f'-V geometry:margin={margins}in',
    f'-V fontsize={font_size}pt'
]
try:
    pypandoc.convert_file(source_file, 'pdf', outputfile=pdf_path, extra_args=pdf_args)
    if os.path.exists(pdf_path):
        print(f"PDF generated at: {pdf_path} (size: {os.path.getsize(pdf_path)} bytes)")
    else:
        print(f"PDF conversion succeeded but file not found at: {pdf_path}")
except Exception as e:
    print(f"PDF conversion failed: {e}")

# Pandoc arguments for DOCX
docx_args = [
    '--verbose',
]
docx_args = ['--verbose', '--reference-doc=custom-reference.docx']
try:
    output = pypandoc.convert_file(source_file, 'docx', outputfile=docx_path, extra_args=docx_args)
    print(f"DOCX conversion output: {output}")
    if os.path.exists(docx_path) and os.path.getsize(docx_path) > 0:
        print(f"DOCX generated at: {docx_path} (size: {os.path.getsize(docx_path)} bytes)")
    else:
        print(f"DOCX conversion succeeded but file empty or not found at: {docx_path}")
except Exception as e:
    print(f"DOCX conversion failed: {e}")

time.sleep(1)  # Ensure files are written

# List files
print("Files in current directory:")
for file in os.listdir(current_dir):
    file_path = os.path.join(current_dir, file)
    if os.path.isfile(file_path):
        print(f" - {file} (size: {os.path.getsize(file_path)} bytes)")
    else:
        print(f" - {file} (directory)")