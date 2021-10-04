import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..")))

extensions = ["sphinx.ext.autodoc"]
autodoc_type_aliases = dict(X="mycode.X")
nitpicky = True
autodoc_member_order = "bysource"