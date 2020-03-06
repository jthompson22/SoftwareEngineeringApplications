import sys 
import os
import django

def test_config():
    check = django in sys.modules
    assert check
