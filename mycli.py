import os
import sys

HERE = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(HERE, 'vendor'))

import baker

@baker.command
def list_user():
    print 'hello'

baker.run()
