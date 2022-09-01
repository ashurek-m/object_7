from pdf2image import convert_from_path
import os
from pathlib import Path
import pathlib
import glob


outputDir = 'output/'


def convert(file, outputDir):
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    pages = convert_from_path(file, 500)
    counter = 1
    for page in pages:
        myfile = outputDir / (str(counter) + '.jpg')
        counter += 1
        page.save(myfile, 'JPEG')


input_dir = Path(__file__).parent.parent / 'input'
output_dir = Path(__file__).parent.parent / 'output'

file_list = glob.glob(f'{str(input_dir)}\\*.pdf')

for file in file_list:
    convert(file, output_dir)

print(type(output_dir))