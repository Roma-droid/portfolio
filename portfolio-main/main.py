#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_telegram = request.form.get('button_telegram')
    return render_template('index.html', button_python=button_python, button_telegram=button_telegram)

@app.route('/form', methods=['POST'])
def form():
    email = request.form.get['email']
    text = request.form.get['text']
    with open('feedback.txt', 'a', encoding='UTF-8') as f:
        f.write(email+ '\n')
        f.write(text+ '\n')
        f.write('=========================================================================================================='+ '\n')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)