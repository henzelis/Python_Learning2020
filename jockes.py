import pyjokes
from translate import Translator

joke = pyjokes.get_joke('en', 'all')

print(joke)

print('\n','\t','*'*10,'Translating for you...','*'*10,'\n')

translator = Translator(to_lang='uk')

translation = translator.translate(joke)
print(translation)
