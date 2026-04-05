
import sys
import os
sys.path.append(os.getcwd())
try:
    import docs.gallery
    print("SUCCESS")
except Exception as e:
    import traceback
    traceback.print_exc()
    sys.exit(1)
