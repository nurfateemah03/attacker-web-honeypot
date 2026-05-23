# Libraries
import argparse
from ssh_honeypot import *
from web_honeypot import *

# parse arguments

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--address', type=str, required=True)
    parser.add_argument('-p', '--port', type=int, required=True)
    parser.add_argument('-u', '--username', type=str)
    parser.add_argument('-pw', '--password', type=str)

    parser.add_argument('-s', '--ssh', action="store_true")
    parser.add_argument('-w', '--http', action="store_true")

    args = parser.parse_args()

    try:
        if args.ssh:
            print("[-] Running SSH honeypot...")
            username = args.username if args.username else None
            password = args.password if args.password else None
            honeypot(args.address, args.port, username, password)

        elif args.http:
            print("[-] Running HTTP wordpress honeypot...")

            if not args.username:
                args.username = "admin"
            if not args.password:
                args.password = "password"

            print(f"Port:{args.port} Username:{args.username} Password {args.password}")
            run_web_honeypot(args.port, args.username, args.password)
            pass

        else:
            print("[!] Choose a honeypot type (SSH --ssh) or (HTTP --http).")

    except KeyboardInterrupt:
        print("\nExiting HONEYPY...")