''' Test Script '''
import os

with open('./test/sample.txt', encoding="utf-8") as f:
    print(f.read())
    os.mkdir('./create/')
