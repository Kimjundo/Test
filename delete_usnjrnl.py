import common
import os
import time

def main():
    message = "Deleting the journal logs may have unintended consequences"
    common.log("WARNING: %s" % message, log_type="!")
    common.execute(["journalctl", "--vacuum-time=1s"])
    time.sleep(5)

if __name__ == "__main__":
    exit(main())

