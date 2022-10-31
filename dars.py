import threading as th
import time

from ism import *
from familiya import *
from ochistva import *


t1 = th.Thread(target=ism)
t2 = th.Thread(target=familiya)
t3 = th.Thread(target=ochistva)

t1.start()
t2.start()
t3.start()