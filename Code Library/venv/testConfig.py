import sys 
import os
from django.apps import AppConfig

sys.path.append(os.path.abspath('/polls/'))

from polls import apps

def test_config():
    a = apps.PollsConfig('pollsTest', 'testModule')
    assert a.name == 'polls'
