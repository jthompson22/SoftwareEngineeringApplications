import sys 
import os
sys.path.append(os.path.abspath("SoftwareEngineeringApplications/Code Library/venv/polls/apps"))

from apps import *

def test_config():
    a = new PollsConfig()
    assert a.name = 'polls'
