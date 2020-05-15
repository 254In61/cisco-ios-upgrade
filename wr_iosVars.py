#Makes my life easier by writing the iosVars.yml file for me.
#iosVars.yml has details like newOs name, md5 value, size of the file, the first 10 characters on name, and "bootflash"

#!/usr/tools/pyenv/shims/python3
#Python scrip to prepare iosVars.yml file for iosUpload module
import os

def wr_iosVars():
    open("modules/iosVars.yml","w").close #Clear earlier values
    xx = open("modules/iosVars.yml","a")

    newOS = input("New IOS Image .bin filename?:")
    xx.write("---\n")
    xx.write("newOS: "+ newOS + "\n")

    cmd1 = "md5sum images/"+ newOS + " > ff.txt"
    #print(cmd1)
    os.system(cmd1)
    md5 = open("ff.txt","r").read().split()[0] #Gets value of md5
    #print("Md5 value of image:" + md5)
    xx.write("md5: "+ md5 + "\n")

    zz = newOS[0:10]
    #print("1st 9 characters of new image:"+zz)
    xx.write("zz: " + zz + "\n")

    ff = "bootflash"
    xx.write("ff: " + ff + "\n")

    cmd2 = "ls -l images/"+ newOS + " > ff.txt"
    #print(cmd2)
    os.system(cmd2)
    #print(o)
    size = int(int(open("ff.txt","r").read().split()[4])/1000) #Gets the size value in kbps
    #print(size)
    xx.write("size: "+ str(size) + "\n")
    os.system("cat modules/iosVars.yml > ff.txt")
    #print(open("ff.txt","r").read())

wr_iosVars()
