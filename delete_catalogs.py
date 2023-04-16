import common
import time
import sys

def main():
    if sys.platform.startswith("win"):
        warning = "Deleting the backup catalog may have unexpected consequences. Operational issues are unknown."
        common.log("WARNING: %s" % warning, log_type="!")
        time.sleep(5)

        common.execute(["wbadmin", "delete", "catalog", "-quiet"])
    else:
        common.log("This script is not supported on Linux. Skipping the execution.", log_type="!")

if __name__ == "__main__":
    exit(main())
