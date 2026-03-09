#!/usr/bin/env python3
"""
TLS/SSL Vulnerability Scanner
M542 Cryptology — Individual Project
Author: [Rahul]
"""

from sslyze import *
from sslyze.plugins.scan_commands import ScanCommand
from colorama import Fore, Style, init

init(autoreset=True)

def print_banner():
    print(Fore.CYAN + """
╔══════════════════════════════════════╗
║       TLS/SSL Vulnerability Scanner  ║
║       M542 Cryptology Project        ║
╚══════════════════════════════════════╝
    """)

def scan_target(hostname, port=443):
    print(Fore.YELLOW + f"\n[*] Scanning {hostname}:{port} ...")
    print("-" * 50)

    try:
        # Updated API for newer SSLyze versions
        server_location = ServerNetworkLocation(hostname, port)
        
        scanner = Scanner()
        scan_request = ServerScanRequest(
            server_location=server_location,
            scan_commands={
                ScanCommand.SSL_2_0_CIPHER_SUITES,
                ScanCommand.SSL_3_0_CIPHER_SUITES,
                ScanCommand.TLS_1_0_CIPHER_SUITES,
                ScanCommand.TLS_1_1_CIPHER_SUITES,
                ScanCommand.TLS_1_2_CIPHER_SUITES,
                ScanCommand.TLS_1_3_CIPHER_SUITES,
                ScanCommand.HEARTBLEED,
                ScanCommand.SESSION_RENEGOTIATION,
            }
        )

        scanner.queue_scans([scan_request])
        vulnerabilities_found = []

        for result in scanner.get_results():

            # Check for connectivity error first
            if result.connectivity_error_trace:
                print(Fore.RED + f"[ERROR] Could not connect to {hostname}:{port}")
                return

            print(Fore.CYAN + f"\n[+] Results for {hostname}\n")

            # ---- SSLv2 ----
            ssl2 = result.scan_result.ssl_2_0_cipher_suites
            if ssl2.result.accepted_cipher_suites:
                print(Fore.RED + "  [CRITICAL] SSLv2 ENABLED — Extremely dangerous!")
                vulnerabilities_found.append("SSLv2 Enabled")
            else:
                print(Fore.GREEN + "  [OK] SSLv2 Disabled")

            # ---- SSLv3 (POODLE) ----
            ssl3 = result.scan_result.ssl_3_0_cipher_suites
            if ssl3.result.accepted_cipher_suites:
                print(Fore.RED + "  [CRITICAL] SSLv3 ENABLED — Vulnerable to POODLE!")
                vulnerabilities_found.append("SSLv3 / POODLE")
            else:
                print(Fore.GREEN + "  [OK] SSLv3 Disabled — POODLE safe")

            # ---- TLS 1.0 (BEAST) ----
            tls10 = result.scan_result.tls_1_0_cipher_suites
            if tls10.result.accepted_cipher_suites:
                print(Fore.YELLOW + "  [HIGH] TLS 1.0 ENABLED — Vulnerable to BEAST!")
                vulnerabilities_found.append("TLS 1.0 / BEAST")
            else:
                print(Fore.GREEN + "  [OK] TLS 1.0 Disabled — BEAST safe")

            # ---- TLS 1.1 ----
            tls11 = result.scan_result.tls_1_1_cipher_suites
            if tls11.result.accepted_cipher_suites:
                print(Fore.YELLOW + "  [MEDIUM] TLS 1.1 ENABLED — Deprecated!")
                vulnerabilities_found.append("TLS 1.1 Deprecated")
            else:
                print(Fore.GREEN + "  [OK] TLS 1.1 Disabled")

            # ---- TLS 1.2 ----
            tls12 = result.scan_result.tls_1_2_cipher_suites
            if tls12.result.accepted_cipher_suites:
                print(Fore.GREEN + "  [OK] TLS 1.2 Supported")
            else:
                print(Fore.YELLOW + "  [INFO] TLS 1.2 Not supported")

            # ---- TLS 1.3 ----
            tls13 = result.scan_result.tls_1_3_cipher_suites
            if tls13.result.accepted_cipher_suites:
                print(Fore.GREEN + "  [OK] TLS 1.3 Supported — Most secure")
            else:
                print(Fore.YELLOW + "  [INFO] TLS 1.3 Not supported")

            # ---- Heartbleed ----
            heartbleed = result.scan_result.heartbleed
            if heartbleed.result.is_vulnerable_to_heartbleed:
                print(Fore.RED + "  [CRITICAL] HEARTBLEED VULNERABLE!")
                vulnerabilities_found.append("Heartbleed")
            else:
                print(Fore.GREEN + "  [OK] Not vulnerable to Heartbleed")

            # ---- Summary ----
            print("\n" + "=" * 50)
            if vulnerabilities_found:
                print(Fore.RED + f"  ⚠️  {len(vulnerabilities_found)} vulnerabilities found:")
                for v in vulnerabilities_found:
                    print(Fore.RED + f"     → {v}")
            else:
                print(Fore.GREEN + "  ✅ No major vulnerabilities found!")
            print("=" * 50)

    except Exception as e:
        print(Fore.RED + f"[ERROR] Could not scan target: {e}")

if __name__ == "__main__":
    print_banner()
    scan_target("localhost", 443)
                                   
