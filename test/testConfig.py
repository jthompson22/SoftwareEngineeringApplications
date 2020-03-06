import sys 
import os
sys.path.append(os.path.abspath("./Code Library/venv/polls/apps"))

import apps

def test_config():
    a = PollsConfig()
    assert a.name == 'polls'
