import time
from yahboom.ybUtils.YbKey import YbKey
key = YbKey()
abort_main = 0
if key.is_pressed():
    time.sleep_ms(10)
    if key.is_pressed():
        abort_main = 1


if not abort_main:
    from yahboom.ybMain.main import *
    start()
