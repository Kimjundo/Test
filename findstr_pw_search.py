import common

def main():
    path = "/"
    common.log("Searching for passwords on {}".format(path))
    common.execute(["grep", "-r", "-i", "password", path])

if __name__ == "__main__":
    exit(main())
