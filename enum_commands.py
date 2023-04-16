import argparse
import common
import random

long_commands = [
    "ps aux",
    "systemctl list-unit-files",
]

commands = [
    "ifconfig -a",
    "getent group",
    "getent passwd",
    "ps -ef",
    "smbtree",
    "ss -tuln",
    "whoami",
    "hostname",
    "systemctl",
    "ps aux --forest",
    "date",
    "mount",
    "lsblk",
    "df -h",
    "free -h",
    "cat /etc/fstab",
] + long_commands

def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sample', dest="sample", default=len(commands), type=int,
                        help="Number of commands to run, chosen at random from the list of enumeration commands")
    args = parser.parse_args(args)
    sample = min(len(commands), args.sample)

    if sample < len(commands):
        random.shuffle(commands)

    common.log("Running {} out of {} enumeration commands\n".format(sample, len(commands)))
    for command in commands[0:sample]:
        common.log("About to call {}".format(command))
        if command in long_commands:
            common.execute(command, kill=True, timeout=15)
            common.log("[output suppressed]", log_type='-')
        else:
            common.execute(command)

if __name__ == "__main__":
    exit(main())
