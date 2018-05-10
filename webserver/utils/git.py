import os
import sys
import subprocess


def check_version():
    original = os.path.abspath(sys.path[0])
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    git_hash = get_git_revision_hash()
    os.chdir(original)
    return git_hash.strip()

def get_git_revision_hash():
    return subprocess.check_output(['git', 'rev-parse', 'HEAD'])

def get_git_revision_short_hash():
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])
