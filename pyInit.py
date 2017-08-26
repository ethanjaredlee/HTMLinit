import subprocess
import sys, os
import ipdb

def initHTML():
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
    else:
        f = open(fileName, 'w+')
        initString = '''<!doctype html>
<html>
<head>
</head>

<body>
</body>

</html>
'''
        f.write(initString)
        f.flush()
        subprocess.call(['vim', fileName])
        f.seek(0)

initHTML()
