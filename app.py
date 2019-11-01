from flask import Flask # импорт конструктора Flask из модуля flask
from config import Configuration    # Импорт конигурационного файла
from flask_sqlalchemy import SQLAlchemy # реляционная база данных или ORM. SQLAlchemy позволяет работать с самыми
# разными БД (postgresql, mongodb и т.д.) для этого нужно изменить только БД и драйвер
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)   # вызов конструктора со значениями __name__, где __name__ - название текущего файла (app.py)
app.config.from_object(Configuration)   # Запись конфигурации из custom конфигурационного файла

db = SQLAlchemy(app)

migrate = Migrate(app, db)  # корелляция между приложением и БД
manager = Manager(app)
manager.add_command('db', MigrateCommand) # регистрация команды для миграций в консоли