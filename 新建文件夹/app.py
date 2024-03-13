from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read

@app.route('/submit', methods=['POST'])
def submit():
    input_text = request.form['inputText']
    output_text = process_input(input_text)
    return output_text

def process_input(input_text):
    # 在输入文本后面加上数字 6
    processed_text = input_text + '6'
    print("Processed Text:", processed_text)
    return processed_text

if __name__ == '__main__':
    app.run(debug=False)
