import os
import sys


os.system("echo "+ sys.argv[1])
os.system("git remote add upstream "+  sys.argv[1])
os.system("git fetch upstream")
os.system("git checkout master")
os.system("git merge upstream/master")
os.system("echo \"DONE WEY\"")