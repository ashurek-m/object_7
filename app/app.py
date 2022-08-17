from pdf2image import convert_from_path
import os


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
print(os.path.splitdrive(os.path.splitdrive(r"D:\Python's_project\object_7\app\output")))
