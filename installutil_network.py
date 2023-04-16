import common
import sys
import os

MY_DOT_NET = common.get_path("bin", "mydotnet.exe")


@common.dependencies(MY_DOT_NET)
def main():
    server, ip, port = common.serve_web()
    common.clear_web_cache()

    target_app = "mydotnet.exe"
    common.patch_file(MY_DOT_NET, common.wchar(":8000"), common.wchar(":%d" % port), target_file=target_app)

    mono_path = "/usr/bin/mono"

    if not os.path.exists(mono_path):
        common.log("Mono is not installed. Please install Mono to proceed.")
        return

    common.clear_web_cache()
    common.execute([mono_path, target_app])

    common.remove_file(target_app)
    server.shutdown()


if __name__ == "__main__":
    exit(main())
