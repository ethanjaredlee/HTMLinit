import subprocess
import sys, os
from shutil import copyfile

# can replace with editor of choice
EDITOR = 'vim'

# checks
if len(sys.argv) > 2:
    print 'too many args, exiting ...'
    sys.exit()

fileName = sys.argv[1]

if fileName[-5:] != '.html':
    print 'can only init .html file, exiting ...'
    sys.exit()

filePath = './{}'.format(fileName)
exists = os.path.isfile(filePath)

if exists:
    print 'file already exists, exiting ...'
    sys.exit()

# copying file over
repoPath = os.path.dirname(os.path.realpath(__file__))
copyfile(repoPath + '/template.html', fileName)
subprocess.call([EDITOR, fileName])

