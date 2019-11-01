from app import app
from flask import render_template   # отрисовывает шаблоны

@app.route('/') # декоратор, оборачивает результат выполнения функции. Внутри flask создает примерно такую конструкцию
# @app.route('/blog') ## поведение для '/' и '/blog' будет одинаковым
def index():    # { '/': 'view.index' }
    name = 'Chubaka'
    # return 'Hello world!'   # в ответе может быть строка текста, строка с тегами или шаблон
    return render_template('index.html', name=name)    # шаблон не нужно как-то особо импортировать. Поиск шаблонов
    # автоматически осуществляется внутри папки templates. Второй аргумент - данные, передаваемые в шаблон.
