#!"C:\Users\Roman\PycharmProjects\facebook api marketing\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'worksheet==0.0.1a0','console_scripts','worksheet'
__requires__ = 'worksheet==0.0.1a0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('worksheet==0.0.1a0', 'console_scripts', 'worksheet')()
    )
