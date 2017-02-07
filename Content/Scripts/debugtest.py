import redirect_print
import time
import imp
from threading import Thread

imp.reload(redirect_print)

def backspace(n):
    # print((b'\x08' * n).decode(), end='') # use \x08 char to go back
    print('\r' * n, end='')                 # use '\r' to go back

def testaction():
	for i in range(51):                        # for 0 to 100
	    s = str(i) + '%'                        # string for output
	    print(s, end='')                        # just print and flush
	    # sys.stdout.flush()                    # needed for flush when using \x08
	    backspace(len(s))                       # back for n chars

	    time.sleep(0.01)                         # sleep for 200ms

t = Thread(target=testaction)
t.start()