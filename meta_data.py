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

print("File Size: ",stat_info.st_size / 1024)
print("Last Access Time", dt.fromtimestamp(stat_info.st_atime))
print("Modification Time: ", dt.fromtimestamp(stat_info.st_mtime))
print("Inode: ", stat_info.st_ino)
print("Mode: ", stat_info.st_mode)
print("User Id: ", stat_info.st_uid)
print("Group Id: ", stat_info.st_gid)
print("Device Id: ", stat_info.st_dev)

major = os.major(stat_info.st_dev)
minor = os.minor(stat_info.st_dev)

print("Major: ", major)
print("Minor: ", minor)