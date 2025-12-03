import socket
import subprocess
import platform
import time


# ------------------------------
# Utility: Ping Test
# ------------------------------
def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    result = subprocess.run(["ping", param, "1", host],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)
    return result.returncode == 0


# ------------------------------
# Utility: TCP Port Test
# ------------------------------
def tcp_test(host, port, timeout=3):
    try:
        sock = socket.create_connection((host, port), timeout)
        sock.close()
        return True
    except:
        return False


# ------------------------------
# Utility: HTTP GET Test (Raw Socket)
# ------------------------------
def http_test(host):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((host, 80))
        request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
        s.send(request.encode())
        response = s.recv(50)
        s.close()
        return True if response else False
    except:
        return False


# ------------------------------
# Detect Local IP
# ------------------------------
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "Unknown"


# ------------------------------
# Network Class (A / B / C)
# ------------------------------
def get_network_class(ip):
    try:
        first = int(ip.split(".")[0])
        if 1 <= first <= 126:
            return "Class A"
        elif 128 <= first <= 191:
            return "Class B"
        elif 192 <= first <= 223:
            return "Class C"
        else:
            return "Other"
    except:
        return "Unknown"


# ------------------------------
# MAIN PROGRAM
# ------------------------------
def main():
    print("\n🌐 UNIVERSAL NETWORK CHECKER PRO")
    print("────────────────────────────────────\n")

    # List of websites to test (FULLY CUSTOMIZABLE)
    websites = [
        "google.com",
        "youtube.com",
        "cloudflare.com",
        "microsoft.com",
        "hamrah.academy",   # You can add/remove any domain
    ]

    # Basic System Info
    local_ip = get_local_ip()
    print(f"📌 Local IP: {local_ip}")
    print(f"📌 Network Class: {get_network_class(local_ip)}\n")

    print("🔍 Checking Global Internet...\n")
    time.sleep(1)

    # Test Public Internet via pinging common DNS servers
    dns_servers = ["8.8.8.8", "1.1.1.1"]

    internet_status = False
    for dns in dns_servers:
        print(f"➡️  Pinging DNS {dns} ...")
        if ping(dns):
            print("   ✅ DNS reachable\n")
            internet_status = True
            break
        else:
            print("   ❌ Failed\n")

    if not internet_status:
        print("🚨 Internet seems DOWN or unstable.\n")

    print("🌍 Testing Websites...\n")
    for site in websites:
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"🌐 Testing: {site}")

        # Ping test
        if ping(site):
            print("   📡 Ping:        ✅ OK")
        else:
            print("   📡 Ping:        ❌ Fail")

        # TCP test (HTTPS)
        if tcp_test(site, 443):
            print("   🔐 TCP 443:     ✅ OK")
        else:
            print("   🔐 TCP 443:     ❌ Fail")

        # HTTP GET test
        if http_test(site):
            print("   🌍 HTTP GET:    ✅ OK")
        else:
            print("   🌍 HTTP GET:    ❌ Fail")

        print()

    print("────────────────────────────────────")
    print("✔ TEST FINISHED — Developed by Milad Hadad")
    print("────────────────────────────────────\n")


if __name__ == "__main__":
    main()
