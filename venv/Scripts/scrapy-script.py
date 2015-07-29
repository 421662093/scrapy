#!D:\project\scrapy\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'scrapy==1.0.1','console_scripts','scrapy'
__requires__ = 'scrapy==1.0.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('scrapy==1.0.1', 'console_scripts', 'scrapy')()
    )
