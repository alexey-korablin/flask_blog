class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'   # root - имя пользователя, 1 - пароль,
    # localhost - адрес БД, test1 - имя БД ;;; mysqlconnector
