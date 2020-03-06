import sys 
import os


def test_config():
    check = True
    try:
        import django
    except ImportError:
        check = False

    assert check
