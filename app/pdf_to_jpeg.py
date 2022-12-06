from pdf2image import convert_from_path
import os
from pathlib import Path
import glob
import PIL

PIL.Image.MAX_IMAGE_PIXELS = None


def convert(name_file, outputDir):
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    pages = convert_from_path(file, 250)
    counter = 1
    for page in pages:
        myfile = outputDir / (name_file.split('\\')[-1][0:-4] + f'_{str(counter)}' + '.jpg')
        counter += 1
        page.save(myfile, 'JPEG')


if __name__ in "__main__":
    input_dir = Path(__file__).parent.parent / 'input'
    output_dir = Path(__file__).parent.parent / 'output'

    file_list = glob.glob(f'{str(input_dir)}\\*.pdf')
    target_list = []

    for file in file_list:
        convert(file, output_dir)
        target_list.append(file.split('\\')[-1].rsplit('.', 1)[0])
        # print(file.split('\\')[-1].rsplit('.', 1)[0])
