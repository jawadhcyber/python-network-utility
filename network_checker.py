import platform
import subprocess


def check_connection(host):
    # Windows uses -n; Linux/macOS use -c
    parameter = "-n" if platform.system().lower() == "windows" else "-c"

    command = ["ping", parameter, "1", host]

    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if result.returncode == 0:
        print(f"[+] {host} is reachable.")
    else:
        print(f"[-] {host} is not reachable.")


host = input("Enter an IP address or hostname: ")
check_connection(host)8.8.8.8
