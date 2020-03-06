import sys 
import os
import django

def test_config():
    assert django in sys.modules
