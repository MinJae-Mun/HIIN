from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x15?\xee\xbb;]\x87\x14\xdbT\xd6\x0b>\xac\x1c\xa6'