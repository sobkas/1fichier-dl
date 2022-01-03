import sys
import os
from core.download import cli_download_aria2

# Pyinstaller
excludedhooks=['PyQt5']

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('''Usage: {os.path.basename(__file__)} link (password)''')
    elif len(sys.argv) == 2:
        cli_download_aria2.download(sys.argv[1])
    elif len(sys.argv) == 3:
        cli_download_aria2.download(sys.argv[1], sys.argv[2])
