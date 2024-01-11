# set PWD to cwd
# to call: import getCWD as GD
# PWD = GD.setPWD
# will return the CWD as PWD in the parent file

import os

def setPWD():
    PWD = str(os.getcwd())
    print("PWD set to: " + PWD)
    return(PWD)
