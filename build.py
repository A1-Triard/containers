from collections import namedtuple
from itertools import chain, product, combinations, count
import os, sys, shutil
from datetime import datetime
from time import mktime
from os import path, chdir, utime, remove, mkdir
from sys import stdout, stderr
import yaml
import subprocess
from subprocess import PIPE
from shutil import copyfile, move, make_archive, rmtree, copytree

def assembly_plugin(path, year, month, day, hour, minute, second, keep=False):
    subprocess.run('espa -p ru -' + ('k' if keep else '') + 'v "' + path + '.yaml"', stdout=stdout, stderr=stderr, check=True)
    date = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    t = mktime(date.timetuple())
    utime(path, (t, t))

def check_espa_version():
  espa = subprocess.run('espa -V', stdout=PIPE, check=True, universal_newlines=True)
  if espa.stdout != '0.2.0\n':
    print('wrong espa version')
    sys.exit(1)

def prepare_text(path, d):
    with open(path.upper(), 'r', encoding='utf-8') as utf8:
        with open(d + path + '.txt', 'w', encoding='cp1251') as cp1251:
            cp1251.write(utf8.read())

def main():
    cd = path.dirname(path.realpath(__file__))
    chdir(cd)
    check_espa_version()
    if path.exists('ar'):
        rmtree('ar')
    mkdir('ar')
    copytree('Data Files', 'ar/Data Files')
    copyfile('A1_Containers_V7.esp.yaml', 'ar/Data Files/A1_Containers_V7.esp.yaml')
    prepare_text('Readme', 'ar/')
    copytree('Screenshots', 'ar/Screenshots')
    assembly_plugin('ar/Data Files/A1_Containers_V7.esp', 2014, 8, 15, 18, 53, 0)
    make_archive('A1_Containers_2.0', 'zip', 'ar')
    rmtree('ar')

if __name__ == "__main__":
    main()
