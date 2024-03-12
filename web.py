from flask import Flask
import webbrowser
webbrowser.open("http://localhost:5000/") 
app = Flask(__name__)
@app.route('/')
def index():
    return('第一次尝试')
if __name__ == '__main__':
    app.run(host='0.0.0.0')
