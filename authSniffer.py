#Script written for finding unauthenticated endpoints.

import requests
import argparse

def test_endpoint(endpoint):
    try:
        response = requests.get(endpoint, timeout=10)
        if response.status_code == 200:
            print(f"[UNAUTHENTICATED] {endpoint} is accessible without authentication.")
            return True
        elif response.status_code in {401, 403}:
            print(f"[SECURED] {endpoint} requires authentication (Status: {response.status_code}).")
        else:
            print(f"[UNKNOWN] {endpoint} returned status {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Could not reach {endpoint}: {e}")
    return False

def main(file):
    unauthenticated_endpoints = []
    with open(file, 'r') as f:
        endpoints = [line.strip() for line in f if line.strip()]
    
    for endpoint in endpoints:
        print(f"Testing: {endpoint}")
        if test_endpoint(endpoint):
            unauthenticated_endpoints.append(endpoint)
    
    if unauthenticated_endpoints:
        with open("authSniffer_endpoints.txt", "w") as output:
            output.write("\n".join(unauthenticated_endpoints))
        print("\n[RESULT] Unauthenticated endpoints saved in 'authSniffer_endpoints.txt'")
    else:
        print("\n[RESULT] No unauthenticated endpoints found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test endpoints for unauthenticated access.")
    parser.add_argument("file", help="Path to the file containing the list of endpoints (one per line).")
    args = parser.parse_args()
    main(args.file)

