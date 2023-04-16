import common
import sys

def main():
    if sys.platform.startswith("win"):
        common.log("Deleting volume shadow copies...")
        common.execute(["vssadmin.exe", "delete", "shadows", "/for=c:", "/oldest", "/quiet"])
        common.execute(["wmic.exe", "shadowcopy", "delete", "/nointeractive"])
    else:
        common.log("This script is not supported on Linux. Skipping the execution.", log_type="!")

if __name__ == "__main__":
    exit(main())
