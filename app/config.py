class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://vlad:vlad@localhost/blog_db'
    SECRET_KEY = '4h124go12u4g13084y1v2041y240'

    """Flask-security"""
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    SECURITY_REGISTERABLE = True

    """Mail"""
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'zvladsz@gmail.com'
    MAIL_PASSWORD = '#################'
