import sys 
import os
import os.path.abspath("./Code Library/venv/polls/apps")

def test_config():
    a = PollsConfig()
    assert a.name == 'polls'
