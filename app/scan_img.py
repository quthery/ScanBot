from PIL import Image
import pytesseract


def scan(path:str, languages:str, write_txt:bool):
    img = Image.open(path)

    text = pytesseract.image_to_string(img, lang=languages)

    if bool:
        with open("txt.txt", 'w') as txt:
            txt.write(text)
    else:
        pass

scan('d.jpg', "eng+rus", 1)