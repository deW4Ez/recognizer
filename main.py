from flask import Flask, jsonify, request
import converter

app = Flask(__name__)

@app.route('/')
def index():    
    return "Hello"

@app.route('/messages', methods = ['POST','OPTIONS'])
def putAudio():
    text = "Текст не найден"
    try:
        file = request.files['file']
        file.save("./voice/"+file.filename)
        text = converter.recognise("./voice/"+file.filename) 
    except:
        print("Случилась ошибка")    

    finalText = text 
    print(finalText)
    return {"text": finalText}

@app.route('/text', methods = ['GET'])
def getText():
    return finalText


if __name__ == "__main__":
    finalText = "Файл не найден"
    app.run(debug = True)