from flask import Flask, render_template, request,make_response
import googletrans
from googletrans import Translator
import gtts
from gtts import gTTS
import time
from IPython.display import Audio

app = Flask(__name__)
language_codes = googletrans.LANGUAGES
languages = [{"code": code, "name": name} for code, name in language_codes.items()]

def translate_text(text, target_lang):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    return translation.text

@app.route("/", methods=["GET", "POST"])
def translate():
    if request.method == "POST":
        input_text = request.form.get("input_text")
        target_language = request.form.get("target_language")
        translated_text = translate_text(input_text, target_language)
        timestamp = int(time.time())
        filename = f"static/op_{timestamp}.mp3"  
        tts = gTTS(translated_text, lang=target_language)
        tts.save(filename)  
        return render_template("index.html", languages=languages, input_text=input_text, translated_text=translated_text, audio_filename=filename)
    return render_template("index.html", languages=languages)



if __name__ == "__main__":
    app.run(debug=True)
