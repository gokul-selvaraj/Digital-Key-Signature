import os
import sys
import argparse
from datetime import datetime as dt

__authors__ = ["Elangovan", "Gajendhiran", "Hariharan", "Gokul"]
__description__ = "A Digital Key Signature Interdisciplinary Project"

parser = argparse.ArgumentParser(
    description=__description__,
    epilog="Developed by {}".format(", ".join(__authors__))
)

parser.add_argument("DIR_PATH", help="Path to directory")
args = parser.parse_args()
path_to_meta = args.DIR_PATH

stat_info = os.stat(path_to_meta)
if "linux" in sys.platform or "darwin" in sys.platform:
    print("Change time: ", dt.fromtimestamp(stat_info.st_ctime))
elif "win" in sys.platform:
    print("Creation time: ", dt.fromtimestamp(stat_info.st_ctime))
else:
    print("[-] Unsupported platform {} detected. Cannot interpret ".format(sys.platform))

print(stat_info.st_size / 1024)