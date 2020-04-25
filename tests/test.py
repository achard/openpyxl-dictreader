import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import dictreader

reader = dictreader.DictReader("names.xlsx", worksheet="Sheet1")

for row in reader:
    print(row)

for row in reader:
    print(row["First Name"], row["Last Name"])