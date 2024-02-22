from flask import Flask, render_template, abort
import os 

import hiragana
import katakana


app = Flask(__name__)
app.template_folder = os.path.abspath('Kantaka')


@app.route("/", methods=["GET"])
def main():
    return render_template("index.html")



@app.route("/hiragana/<ideogram>", methods=["GET"])
def showHiragana(ideogram):
    hiraganaReturn = hiragana.showHiragana(ideogram)

    if hiraganaReturn == 1:
        return render_template("error.html", message="Probabily you type something wrong, revise your request please.")
    
    else:
        return render_template("api.html", pronunciation=hiraganaReturn[1], writerJapaneseVariation=hiraganaReturn[2])



@app.route("/katakana/<ideogram>", methods=["GET"])
def showKatakana(ideogram):
    katakanaReturn = katakana.showKatakana(ideogram)

    if katakanaReturn == 1:
        return render_template("error.html", message="Probabily you type something wrong, revise your request please.")
    
    else:
        return render_template("api.html", pronunciation=katakanaReturn[1], writerJapaneseVariation=katakanaReturn[2])


@app.errorhandler(500)
def error(error):
    return render_template("error.html", message="Use the routes below.")

@app.errorhandler(404)
def error2(error):
    return render_template("error.html", message="Use the routes below.")


if __name__ == "__main__":
    app.run()