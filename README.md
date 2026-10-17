
               ,-.
              / \  `.  __..-,O
             :   \ --''_..-'.'
             |    . .-' `. '.
             :      .     .`.'
              \      `.  /  ..
               \      `.   ' .
                `,        `.   \
               ,|,`.        `-.\
              '.||  ``-...__..-`
               |  |
               |__|
               /||\
              //||\\
             // || \\
          __//__||__\\__
         '--------------'

======================================================

   AFRIDI WIFI PROFILE & PASSWORD ANALYZER
   Complete Guide & Documentation
   By: Aryan Afridi (shahid2005a)
===========================================

GitHub : https://github.com/shahid2005a/wifi-analyzer.git
Telegram: https://t.me/dgtlcyber
YouTube : https://www.youtube.com/@aryanafridi00


ABOUT THIS TOOL
=========================================

AFRIDI WiFi Analyzer ek Python-based tool hai jo Windows
system ke saare saved WiFi profiles aur unke passwords
nikal ke dikhata hai. Ye Netsh command ka use karke
key=clear flag se plain text passwords extract karta hai.

Developer : Aryan Afridi
Platform  : Windows Only (netsh required)
Language  : Python 3.6+
License   : Educational Purpose

FEATURES
========================================================

[✅] Saare saved WiFi profiles detect karta hai
[✅] Plain text passwords nikalta hai (key=clear)
[✅] Security type detect (WPA2/WPA3/WEP)
[✅] Currently connected network highlight
[✅] Multi-language support (EN/FR/ES/GR)
[✅] Interactive menu system
[✅] JSON output support
[✅] Bulk export (--all flag)
[✅] Custom ASCII banner
[✅] Color-coded output


REQUIREMENTS
========================================================

- Windows 10 / 11
- Python 3.6+
- netsh (built-in Windows command)
- No admin rights needed (but same user profile)
- Terminal / CMD / PowerShell


INSTALLATION
========================================================

Step 1: Python Install Karo
----------------------------
https://www.python.org/downloads/
[NOTE] Install karte waqt "Add to PATH" check karo

Step 2: Repository Clone Karo
------------------------------
git clone https://github.com/shahid2005a/wifi-analyzer.git
cd wifi-analyzer

Step 3: Run Karo
-----------------
python wifi_analyzer.py

[NOTE] Agar git nahi hai to ZIP download karo:
       GitHub > Code > Download ZIP > Extract


USAGE - COMMANDS
========================================================

Basic Run (Interactive Menu)
-----------------------------
python wifi_analyzer.py

Saare Passwords Ek Saath Dikhao
--------------------------------
python wifi_analyzer.py --all

JSON Format Me Output
----------------------
python wifi_analyzer.py --json

Help Dekho
----------
python wifi_analyzer.py --help



HOW IT WORKS - STEP BY STEP
========================================================

Step 1: Banner Display
-----------------------
[✅] ASCII art + contact info show hota hai
[✅] Telegram + YouTube links dikhte hain

Step 2: Profiles Fetch
-----------------------
Command internally chalti hai:
netsh wlan show profiles
[✅] Saare saved WiFi names list hote hain

Step 3: Parse Profile Names
----------------------------
[✅] Line-by-line parse hota hai
[✅] Multi-language support (profile/profil/perfil)
[✅] Duplicate names remove hote hain

Step 4: Password Extraction (MAIN TRICK)
-----------------------------------------
Har profile ke liye:
netsh wlan show profile name="SSID" key=clear
[✅] key=clear flag = plain text password
[✅] Key Content field se password nikala jata hai
[✅] Greek language bhi supported
    (Περιεχόμενο κλειδιού)

Step 5: Security Info
----------------------
[✅] Authentication field extract hoti hai
[✅] WPA2-Personal / WPA3 / WEP detect hota hai

Step 6: Active Connection Check
--------------------------------
Command internally chalti hai:
netsh wlan show interfaces
[✅] Currently connected WiFi highlight hota hai
[✅] (CONNECTED) tag dikhta hai

Step 7: Display Options
------------------------
[✅] Interactive menu (number select)
[✅] All-at-once table (--all)
[✅] JSON dump (--json)


INTERACTIVE MODE - KAISE USE KARE
========================================================

Run: python wifi_analyzer.py

Screen pe kuch aisa dikhega:

  Found 5 network profile(s):

  [1] Home_WiFi (CONNECTED)
  [2] Office_Net
  [3] JioFiber
  [4] Airtel_5G
  [5] Cafe_Guest

 Select index (1-5) or 'a' for all: _

Options:
- Number daalo (1-5) → specific WiFi password dekho
- 'a' daalo → saare passwords ek saath table me
- Ctrl+C → exit


OUTPUT EXAMPLES
========================================================

SINGLE NETWORK OUTPUT:
-----------------------
--------------------------------------------------
 SSID:         Home_WiFi
 Security:     WPA2-Personal
 Password:     MySecret@123
--------------------------------------------------

ALL NETWORKS OUTPUT:
--------------------
=====================================================================================
SSID                           Security             Password
=====================================================================================
Home_WiFi                      WPA2-Personal        MySecret@123
Office_Net                     WPA2-Enterprise      [No Password Saved]
JioFiber                       WPA3-Personal        Jio@2024
Airtel_5G                      WPA2-Personal        Airtel#9876
Cafe_Guest                     Open                 [No Password Saved]
=====================================================================================

JSON OUTPUT:
------------
[
  {
    "name": "Home_WiFi",
    "actual_ssid": "Home_WiFi",
    "password": "MySecret@123",
    "security": "WPA2-Personal",
    "status": "ok"
  }
]


========================================================
ERROR MESSAGES & SOLUTIONS
========================================================

Error: "netsh not found"
-------------------------
Fix: Ye tool SIRF Windows pe chalta hai
     Linux/Mac pe kaam nahi karega

Error: "[Error: Access Denied]"
-------------------------------
Fix: Same user profile se run karo
     Jis user ne WiFi connect kiya tha, usi se chalao

Error: "No saved WiFi profiles"
-------------------------------
Fix: System me koi saved WiFi nahi hai
     Pehle kisi WiFi se connect karo

Error: "python: command not found"
----------------------------------
Fix: Python install karo
     Windows: python.org se download
     "Add to PATH" check karo

Error: "invalid choice"
-----------------------
Fix: Sirf valid number (1 to N) ya 'a' daalo

Error: UnicodeEncodeError
-------------------------
Fix: CMD me chalao (PowerShell ki jagah)
     Ya: chcp 65001 chalao (UTF-8 enable)


========================================================
CODE STRUCTURE (DEVELOPERS KE LIYE)
========================================================

Functions:
----------
1. print_banner()         - ASCII art + contacts
2. fetch_raw_data()       - netsh wlan show profiles
3. parse_profile_names()  - Profile names extract
4. fetch_profile_details()- netsh ... key=clear
5. extract_key_content()  - Password parse
6. process_wifi_data()    - Data consolidate
7. get_active_connection()- Current WiFi detect
8. show_interactive()     - Menu render
9. show_single()          - Single network display
10. show_all()            - Table display
11. main()                - Entry point


========================================================
CUSTOMIZATION TIPS
========================================================

1. Banner Change Karna
-----------------------
CUSTOM_BANNER variable edit karo (line ~25)

2. Colors Change Karna
-----------------------
BLUE, GREEN, YELLOW, RED, CYAN constants
ko apne RGB codes se replace karo

3. Contact Info Update
-----------------------
print_banner() function me Telegram aur YouTube
links apne se replace karo

4. Naya Language Add Karna
---------------------------
parse_profile_names() me:
["profile", "profil", "perfil"] list me
apni language ka word add karo

5. JSON Output Enhance Karna
-----------------------------
process_wifi_data() me dataset dict me
naye fields add karo


========================================================
LEGAL WARNING
========================================================

+------------------------------------------------------+
|  [🚨] IMPORTANT LEGAL NOTICE                         |
+------------------------------------------------------+

Ye tool SIRF apne khud ke computer pe use karo.
Kisi aur ke computer pe WiFi passwords nikalna:

- IT Act 2000 Section 66 ke under CRIME hai
- 3 saal tak jail + heavy fine
- Privacy violation
- Unauthorized access

✅ LEGAL USE:
- Apne computer ke bhoolay hue WiFi passwords
- Apni family ke device pe
- Admin dashboard ke liye backup

❌ ILLEGAL USE:
- Kisi aur ke laptop/PC pe
- Office computer pe bina permission
- Public computer pe
- Kisi ke ghar me chupke se

Zimmedari aapki hai. Ye tool sirf educational
purpose ke liye banaya gaya hai.


========================================================
SUPPORT & COMMUNITY
========================================================

Developer    : Aryan Afridi
GitHub       : https://github.com/shahid2005a/wifi-analyzer.git
Telegram     : https://t.me/dgtlcyber
YouTube      : https://www.youtube.com/@aryanafridi00
Website      : dgtlcyber.netlify.app

DGTL CYBER Community:
- WhatsApp Group   : chat.whatsapp.com/JhSEMaGzYk4GbkvEr2i6WI
- WhatsApp Channel : whatsapp.com/channel/0029VbD1uw37T8bQVsv5gc2n
- Telegram Bot     : t.me/GsmhackerBot


========================================================
FREQUENTLY ASKED QUESTIONS
========================================================

Q: Kya ye Linux/Mac pe chalega?
A: Nahi. Sirf Windows pe kyunki netsh Windows-only hai.
   Kali Linux ke liye nmcli command use karo.

Q: Admin rights chahiye?
A: Nahi, but same user profile se run karo.

Q: Kya hidden networks dikhenge?
A: Haan, agar pehle connect kiye hain to.

Q: Kya ye internet se passwords fetch karta hai?
A: Nahi. Sab kuch local system se aata hai.

Q: Kya ye tool safe hai?
A: Haan, koi network activity nahi karta. Sirf local
   netsh commands run karta hai.

Q: Password nahi dikh raha?
A: WPA2-Enterprise networks ka password plain text
   nahi hota (server se authenticate hota hai).

Q: Multiple users ke passwords?
A: Sirf current user ke saved networks dikhte hain.
   Har user apna alag profile rakhta hai.

Q: Kya isko EXE me convert kar sakte hain?
A: Haan, pyinstaller se:
   pip install pyinstaller
   pyinstaller --onefile wifi_analyzer.py


========================================================
TROUBLESHOOTING QUICK REFERENCE
========================================================

Problem                    | Solution
---------------------------|---------------------------
netsh not found            | Windows only tool hai
Access Denied              | Same user se run karo
No profiles found          | Pehle WiFi connect karo
python not found           | Python install karo
Unicode error              | chcp 65001 chalao
Invalid choice             | Valid number ya 'a' daalo
Password hidden            | Enterprise network hai
JSON empty                 | Profiles nahi hain system me


========================================================
VERSION INFO
========================================================

Tool Name : AFRIDI WiFi Analyzer
Version   : 1.0.0
Language  : Python 3.6+
Platform  : Windows 10/11
Status    : Active
License   : Educational Use Only

Made with ❤️ by Aryan Afridi
© 2024 DGTL CYBER. All Rights Reserved.


========================================================
   "Learn to protect, not to attack"
========================================================

========================================================
   END OF DOCUMENTATION
========================================================
