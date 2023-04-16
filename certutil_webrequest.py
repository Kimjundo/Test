import common

MY_DLL = common.get_path("bin", "mydll.so")

@common.dependencies(MY_DLL)
def main():
    # http server will terminate on main thread exit
    # if daemon is True
    server, ip, port = common.serve_web()

    uri = "bin/mydll.so"
    target_file = "mydll.so"
    common.clear_web_cache()
    url = "http://{ip}:{port}/{uri}".format(ip=ip, port=port, uri=uri)
    common.execute(["wget", "-q", url, "-O", target_file])

    server.shutdown()
    common.remove_file(target_file)

if __name__ == "__main__":
    exit(main())
