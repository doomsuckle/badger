import subprocess
import shlex

def badger():
    print('setting volume')
    ret = subprocess.Popen(shlex.split('osascript -e "set Volume 5"'), stdout=subprocess.PIPE)
    print('talky talky')
    statement = 'say "ho-tel, mo-tel, holiday -- in"'
    ret = subprocess.Popen(shlex.split(statement), stdout=subprocess.PIPE)

if __name__ == '__main__':
    badger()
