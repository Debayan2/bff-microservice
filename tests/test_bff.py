import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app  # Now pytest can find the 'app' module

def test_sample():
    assert 1 + 1 == 2  # Dummy test
