from flask import Flask, render_template, request, redirect, url_for
import webbrowser
webbrowser.open("http://localhost:5000/") 
app = Flask(__name__)

@app.route('/')
def index():
    # 渲染 login.html 模板
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # 获取用户名和密码
    username = request.form.get('username')
    password = request.form.get('password')

    # 在这里可以添加验证逻辑，例如检查用户名和密码是否匹配

    # 假设验证通过，跳转到 wyb.html 页面
    return redirect(url_for('wyb'))

@app.route('/wyb')
def wyb():
    # 渲染 wyb.html 模板，可以在这里添加 wyb 页面的内容
    return render_template('wyb.html')

if __name__ == '__main__':
    # 运行 Flask 应用
    app.run(debug=False)
