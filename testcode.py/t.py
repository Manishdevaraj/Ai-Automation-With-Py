# from translate import Translator
# translator= Translator(from_lang="English",to_lang="ta")
# translation = translator.translate("Good Morning!")
# print(translation)


from translate import Translator

translator = Translator(to_lang="ta")
english_text = "Hello"
tamil_translation = translator.translate(english_text)
print(tamil_translation)
