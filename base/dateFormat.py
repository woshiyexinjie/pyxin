import os
import subprocess

text = '2018-07-30 11-00-00'
pl = list(text)
pl[10]=' '
pl[13]=':'
pl[16]=':'
print(pl)
text="".join(pl)
print(text)
userSudoPass = 'F0110wme,'
modifyDateInstruct = "echo  " + userSudoPass + "  |  sudo -S  date -s '"+text+"'"
print(modifyDateInstruct)
os.system(modifyDateInstruct)
os.system("date")

# subprocess.check_call(modifyDateInstruct, shell=True)
# subprocess.check_call(["date"])
