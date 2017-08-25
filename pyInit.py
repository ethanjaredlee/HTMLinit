import subprocess


try:
    open('test.html', 'r')
except:
    f = open('test.html', 'w+')
    initString = '''<!doctype html>
<html>
<head>
</head>

<body>
</body>

</html>
'''

    f.write(initString)

subprocess.call('pwd')

