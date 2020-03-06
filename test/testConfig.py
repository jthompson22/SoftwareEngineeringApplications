import sys 
import os
sys.path.append(os.path.abspath("/Code Library/venv/polls/apps.py"))

from polls.apps import PollsConfig

def test_config():
    a = PollsConfig()
    assert a.name == 'polls'
