import os
import argparse

__authors__ = ["Elangovan", "Gajendhiran", "Hariharan", "Gokul"]
__description__ = "A Digital Key Signature Interdisciplinary Project"

parser = argparse.ArgumentParser(
    description=__description__,
    epilog="Developed by {}".format(", ".join(__authors__))
)

parser.add_argument("DIR_PATH", help="Path to directory")
args = parser.parse_args()
path_to_scan = args.DIR_PATH

print(path_to_scan)

for root,directories, files in os.walk(path_to_scan):
    for file_entry in files:
        # create the relative path to the file
        file_path = os.path.join(root, file_entry)
        print(file_path)