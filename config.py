import os
import random
import string


class Config:
    # Secret key for Session
    # byte encoded random string of length 16
    # Notice: All sessions will be dropped on web server restart
    SECRET_KEY = os.environ.get('SECRET_KEY') or str.encode(''.join(
        random.choice(string.ascii_lowercase) for i in range(16)
    ))

