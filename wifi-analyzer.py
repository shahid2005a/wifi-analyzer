#!/usr/bin/env python3
"""
DGTL WiFi Profile & Password Analyzer
"""

import subprocess
import re
import sys
import json
import argparse
import os
from typing import List, Dict, Optional

# Enable ANSI escape sequences on Windows for color support
if sys.platform == "win32":
    os.system("")

# Color definitions (ANSI)
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Your custom ASCII graphic
CUSTOM_BANNER = f"""{CYAN}
         ,-.
        / \\  `.  __..-,O
       :   \\ --''_..-'.'
       |    . .-' `. '.
       :     .     .`.'
        \\     `.  /  ..
         \\      `.   ' .
          `,       `.   \\
         ,|,`.        `-.\\
        '.||  ``-...__..-`
         |  |
         |__|
         /||\\
        //||\\\\
       // || \\\\
    __//__||__\\\\__
   '--------------'{RESET}"""

def print_banner():
    """Displays your custom ASCII banner with contact info."""
    print(CUSTOM_BANNER)
    print(f"{BOLD}{BLUE}======================================================{RESET}")
    print(f"{BOLD}{GREEN}            AFRIDI NETWORK ANALYSIS TOOL{RESET}")
    print(f"{BOLD}{BLUE}======================================================{RESET}")
    print(f"{YELLOW} ⌲ Telegram Group: {RESET}https://t.me/dgtlcyber")
    print(f"{YELLOW} 🔴 YouTube:       {RESET}https://www.youtube.com/@aryanafridi00")
    print(f"{BLUE}------------------------------------------------------{RESET}\n")

def fetch_raw_data() -> str:
    """Retrieves raw profiles output from netsh."""
    try:
        res = subprocess.run(
            ["netsh", "wlan", "show", "profiles"],
            capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=20
        )
        if res.returncode != 0:
            print(f"{RED}[!] System Error: {res.stderr.strip()}{RESET}")
            sys.exit(1)
        return res.stdout
    except FileNotFoundError:
        print(f"{RED}[!] This tool requires a Windows environment (netsh not found).{RESET}")
        sys.exit(1)

def parse_profile_names(raw_text: str) -> List[str]:
    """Extracts profile names from the raw text (Locale-agnostic)."""
    names = []
    for line in raw_text.splitlines():
        if ":" in line:
            parts = line.split(":", 1)
            key = parts[0].strip().lower()
            val = parts[1].strip()
            if any(x in key for x in ["profile", "profil", "perfil"]):
                if val and val not in names:
                    names.append(val)
    return names

def fetch_profile_details(ssid: str) -> Optional[str]:
    """Retrieves specific profile details including the cleartext key."""
    try:
        res = subprocess.run(
            ["netsh", "wlan", "show", "profile", f"name={ssid}", "key=clear"],
            capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=10
        )
        return res.stdout if res.returncode == 0 else None
    except:
        return None

def extract_key_content(details: str) -> Optional[str]:
    """Extracts the password/key content from profile details."""
    for line in details.splitlines():
        line_str = line.strip()
        if line_str.lower().startswith("key content") or "περιεχόμενο κλειδιού" in line_str.lower():
            parts = line_str.split(":", 1)
            if len(parts) == 2:
                return parts[1].strip()
    
    match = re.search(r'(?:Key\s*Content|Περιεχόμενο\s*κλειδιού)\s*:\s*(.+)', details, re.IGNORECASE)
    return match.group(1).strip() if match else None

def process_wifi_data(profiles: List[str]) -> List[Dict]:
    """Processes and consolidates WiFi configuration data."""
    dataset = []
    for ssid in profiles:
        details = fetch_profile_details(ssid)
        
        # Bugfix for KeyError: Ensuring all structure keys exist even on failure
        if not details:
            dataset.append({
                "name": ssid,
                "actual_ssid": ssid,
                "password": "[Error: Access Denied]",
                "security": "Unknown",
                "status": "error"
            })
            continue
            
        password = extract_key_content(details)
        
        sec_match = re.search(r'(?:Authentication|Έλεγχος\s*ταυτότητας)\s*:\s*(.+)', details, re.IGNORECASE)
        security = sec_match.group(1).strip() if sec_match else "Unknown"
        
        ssid_match = re.search(r'SSID name\s*:\s*"([^"]+)"', details)
        actual_ssid = ssid_match.group(1) if ssid_match else ssid

        dataset.append({
            "name": ssid,
            "actual_ssid": actual_ssid,
            "password": password if password else "[No Password Saved]",
            "security": security,
            "status": "ok"
        })
    return dataset

def get_active_connection() -> Optional[str]:
    """Returns the current connected network SSID."""
    try:
        res = subprocess.run(
            ["netsh", "wlan", "show", "interfaces"],
            capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=10
        )
        for line in res.stdout.splitlines():
            if "SSID" in line and "BSSID" not in line:
                parts = line.split(":", 1)
                if len(parts) == 2:
                    return parts[1].strip()
    except:
        pass
    return None

def show_interactive(results: List[Dict]):
    """Renders the interactive command-line selection menu."""
    current = get_active_connection()
    
    if current:
        print(f" {GREEN}[*] Currently Connected To:{RESET} {BOLD}{YELLOW}{current}{RESET}\n")
    
    print(f" Found {len(results)} network profile(s):\n")
    for i, item in enumerate(results, 1):
        status_tag = f" {GREEN}(CONNECTED){RESET}" if current and (item["name"] == current or item["actual_ssid"] == current) else ""
        print(f"  [{BLUE}{i}{RESET}] {item['name']}{status_tag}")
        
    try:
        choice = input(f"\n Select index (1-{len(results)}) or '{BOLD}a{RESET}' for all: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)
        
    if choice == 'a':
        show_all(results)
    else:
        try:
            idx = int(choice) - 1
            show_single(results[idx])
        except (ValueError, IndexError):
            print(f"\n{RED}[!] Invalid choice.{RESET}")

def show_single(item: Dict):
    """Displays data for a single specific network profile."""
    print(f"\n{BLUE}" + "-"*50 + f"{RESET}")
    print(f" {CYAN}SSID:{RESET}         {item['name']}")
    print(f" {CYAN}Security:{RESET}     {item['security']}")
    print(f" {GREEN}Password:{RESET}     {BOLD}{YELLOW}{item['password']}{RESET}")
    print(f"{BLUE}" + "-"*50 + f"{RESET}")

def show_all(results: List[Dict]):
    """Displays all profile records in a clean structured table."""
    print(f"\n{BLUE}" + "="*85 + f"{RESET}")
    print(f"{BOLD}{'SSID':<30} {'Security':<20} {'Password':<30}{RESET}")
    print(f"{BLUE}" + "="*85 + f"{RESET}")
    for item in results:
        pwd = item['password']
        if len(pwd) > 28:
            pwd = pwd[:25] + "..."
        print(f"{item['name']:<30} {item['security']:<20} {GREEN}{pwd:<30}{RESET}")

def main():
    parser = argparse.ArgumentParser(description="HexSec WiFi Analyzer")
    parser.add_argument('--all', action='store_true', help='Show all passwords directly')
    parser.add_argument('--json', action='store_true', help='Output data as raw JSON')
    args = parser.parse_args()
    
    print_banner()
    
    raw_data = fetch_raw_data()
    profiles = parse_profile_names(raw_data)
    
    if not profiles:
        print(f"{YELLOW}[!] No saved WiFi profiles discovered on this system.{RESET}")
        return

    info = process_wifi_data(profiles)
    
    if args.json:
        print(json.dumps(info, indent=2, ensure_ascii=False))
    elif args.all:
        show_all(info)
    else:
        show_interactive(info)

if __name__ == '__main__':
    main()
