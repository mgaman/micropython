# This is your main script.
# uart1 tx on gpio2, no rx
# NOTE GPIO also builtin led so cannot use that here

from machine import UART,Pin
from time import sleep
u = UART(1)
u.init(115200)
count = 0
while True:
    u.write(str(count)+'\r\n')
    count = count + 1
    sleep(1)
