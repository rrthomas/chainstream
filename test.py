import io

from chainstream import ChainStream

with open("README.md", 'rb') as f:
    with open("tox.ini", 'rb') as g:
        h = io.BufferedReader(ChainStream([f, g]))
        print(h.read())
        h.close()
