import common
import os

def main():
    common.log("Encoding target")
    encoded_file = os.path.abspath('encoded.txt')
    decoded_file = os.path.abspath('decoded.sh')

    # 인코딩
    common.execute("base64 /bin/bash -o \"%s\"" % encoded_file)

    common.log("Decoding target")
    # 디코딩
    common.execute("base64 -d \"%s\" -o \"%s\"" % (encoded_file, decoded_file))

    common.log("Cleaning up")
    common.remove_file(encoded_file)
    common.remove_file(decoded_file)

if __name__ == "__main__":
    exit(main())
