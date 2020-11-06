from translate import Translator

translator = Translator(to_lang='uk')
try:
    with open('test.txt', mode="r") as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('text_uk.txt',mode='w', encoding='utf8') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print("check your file path silly!")