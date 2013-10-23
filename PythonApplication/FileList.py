# coding: utf-8

import os, os.path
import glob

path = "C:\\Python27\\"

print("+--------------------+")
print(u"ファイル＋ディレクトリ一覧")
print("+--------------------+")

files = os.listdir(path)

for file in files:
    print(file)

# ---------------------------------

print("+--------------------+")
print(u"指定パス＋ファイル一覧")
print("+--------------------+")

files = glob.glob(path)

for file in files:
    print(file)

# ---------------------------------

print("+--------------------+")
print(u"ファイルとサブディレクトリ一覧")
print("+--------------------+")

for r, ds, fs in os.walk(path):
    print(r, ds, fs)
