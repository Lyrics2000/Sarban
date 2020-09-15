import string
import random
from datetime import datetime

def id_generator(size=6, chars=string.ascii_uppercase + string.digits + str(datetime.now())):
       return ''.join(random.choice(chars) for _ in range(size))
   