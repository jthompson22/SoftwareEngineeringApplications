import sys 
import os


def test_djangoImport():
    check = True
    try:
        import django
    except ImportError:
        check = False

    assert check
