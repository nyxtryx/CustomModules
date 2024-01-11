''' 
 to call, place this file in the root, and run
    import cpCustMods
    <object> = cpCustMods.<function>

    for example:
        import cpCustMods
        PWD = cpCustMods.CPCWD(<your relative path here>)
'''

import os
import shutil as SH
herePWD = os.getcwd() + "\\customModules"
print("Your current root directory is: " +  herePWD + "\n \n Please remember to use relative paths for calling modules! \n \n ie if you have subfolders, you'll need to provide the path FROM the root dir to the sub-dir ie \\<your dir here> to be inserted for any def that has relativePath as a variable.")

# below copies the getCWD file to the PWD+relative path
def CPCWD(relativePath):
    SH.copy2(herePWD + "\\getCWD.py", (herePWD + relativePath + "\\getCWD.py"), follow_symlinks=True)
    print("Copied getCWD.py from source to: " + herePWD + relativePath + "\\getCWD.py \n \n You may now import getCWD into the current project and call using getCWD()")