from googletrans import Translator

import googletrans

translator = Translator()

result = translator.translate('viele danke', src='de', dest='ru')

print(result.text)

print(googletrans.LANGCODES)