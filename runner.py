import sys
import os


os.system(f'javac ./{sys.argv[1]}.java')
os.system(f'java {sys.argv[1]}')
