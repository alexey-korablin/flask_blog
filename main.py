from app import app # 1-й app - файл, 2-й app - экземпляр класса flask
import view # так сервер узнает о существовании views приложения
from app import db
from posts.blueprint import posts

app.register_blueprint(posts, url_prefix='/blog')

if __name__ == '__main__':
    app.run()

