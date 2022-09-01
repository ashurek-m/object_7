from pdf2image import convert_from_path
import os
from pathlib import Path


outputDir = 'output/'


def convert(file, outputDir):
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    pages = convert_from_path(file, 500)
    counter = 1
    for page in pages:
        myfile = outputDir + 'output' + str(counter) + '.jpg'
        counter += 1
        page.save(myfile, 'JPEG')


#file = 'план.pdf'
#convert(file, outputDir)
#print(Path(__file__).parent.parent / 'input')

current_dir = Path.cwd()
home_dir = Path.home()

print(current_dir)
print(home_dir)
