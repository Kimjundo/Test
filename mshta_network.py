import common
import requests

HTA_FILE = common.get_path("bin", "beacon.hta")


@common.dependencies(HTA_FILE)
def main():
    # http server will terminate on main thread exit
    # if daemon is True
    common.log("MsHta Beacon")
    server, ip, port = common.serve_web()
    common.clear_web_cache()

    new_callback = "http://%s:%d" % (ip, port)
    common.log("Updating the callback to %s" % new_callback)
    common.patch_regex(HTA_FILE, common.CALLBACK_REGEX, new_callback)

    # Use Python's requests library to generate a web request instead of mshta.exe
    try:
        response = requests.get(new_callback, timeout=10)
        common.log("Request to {} completed with status code {}".format(new_callback, response.status_code))
    except requests.exceptions.RequestException as e:
        common.log("Request to {} failed: {}".format(new_callback, str(e)))

    server.shutdown()


if __name__ == "__main__":
    exit(main())
