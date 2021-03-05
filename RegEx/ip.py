import re

'''
IP:
from 0.0.0.0 to 255.255.255.255
    
'''

validIp = re.compile(r'''
    ^
    (?:
        (?:
            25[0-5]|
            2[0-4]\d|
            1\d\d|
            [1-9]\d|
            \d
        )
        \.?
    ){4}
    \b
    $
''', flags=re.VERBOSE)

#r'^(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.?){4}\b$'

for i in range(0, 301, 5):
    ip = f'{i}.{i}.{i}.{i}'
    print(validIp.findall(ip))
