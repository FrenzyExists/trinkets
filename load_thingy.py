# Python Loading thingy

import time

def loading_screen(total=40):
    bar = " " * (total)
    for delta in range(total+1):
        percentage = int((delta/(total)) * 100)
        print("\033[0;33;40m  %s [{}]\033[0m".format(bar) % str(percentage), end="\r")
        bar = bar.replace(" ", "=", 1)
        time.sleep(0.1)
    print("\n")
