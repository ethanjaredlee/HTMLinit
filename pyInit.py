import subprocess
import sys, os
import ipdb

def caller():
    fileName = sys.argv[1]
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

caller()
