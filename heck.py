import sys
import os

# TODO this hacking is because aa path is behind dist-package which
# tests module may be overrided by dist-package's tests module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../../../../"))
