from deep_translator import GoogleTranslator

translator = GoogleTranslator(source="en", target="pl")
text_to_translate = "Hello World!"

translated_text = translator.translate(text_to_translate).title()

print(f"Input text: {text_to_translate}")
print(f"Output text: {translated_text}")
