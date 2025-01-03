import io

from chainstream import ChainStream, TextChainStream

with open("README.md", 'rb') as f:
    with open("tox.ini", 'rb') as g:
        h = io.BufferedReader(ChainStream([f, g]))
        print(h.read())
        h.close()

with open("README.md", encoding='utf-8') as f:
    with open("tox.ini", encoding='utf-8') as g:
        h2 = TextChainStream([f, g])
        print(h2.read())
        h2.close()
