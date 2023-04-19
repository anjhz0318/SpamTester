import subprocess
import config
import testbody
import time
from common.common import *
from common.mail_sender import MailSender
from exploits_builder import ExploitsBuilder
import testcases
test_cases = testcases.test_cases
config = config.config
def send_test_mail():
    while(1):
        try:
            mail_server = config["server_mode"]['recv_mail_server']
            if not mail_server:
	            mail_server = get_mail_server_from_email_address(config["victim_address"])
            if not mail_server:
	            print("Error: mail server can not be resolved, please set recv_mail_server manually in config.py.")
	            return -1
            mail_server_port = config["server_mode"]['recv_mail_server_port']
            starttls = config['server_mode']['starttls']

            exploits_builder = ExploitsBuilder(testcases.test_cases, config)
            smtp_seqs = exploits_builder.generate_smtp_seqs()
            msg_content = config["raw_email"] if config["raw_email"] else smtp_seqs["msg_content"]
            mail_sender = MailSender()
            mail_sender.set_param((mail_server, mail_server_port), helo=smtp_seqs["helo"], mail_from=smtp_seqs["mailfrom"], rcpt_to =smtp_seqs["rcptto"], email_data=msg_content, starttls=starttls)
            mail_sender.send_email()
            break
        except Exception as e:
            print(str(e))
            time.sleep(5)
def add_multipart_headers():
    test_cases["server_a3"]["data"]["other_headers"] = b"Date: " + get_date() + b"\r\n" + b"Content-Type: multipart/mixed;\r\n\tboundary=\"----=_Part_111217_462031992.1680524601073\"\r\nMIME-Version: 1.0\r\nMessage-ID: <1538085644648.096e3d4e-bc38-4027-b57e-" +\
            id_generator() + b"@message-ids.attack.com>\r\nX-Email-Client: https://github.com/chenjj/espoofer\r\n\r\n"
    test_cases["server_a4"]["data"]["other_headers"] = b"Date: " + get_date() + b"\r\n" + b"Content-Type: multipart/mixed;\r\n\tboundary=\"----=_Part_111217_462031992.1680524601073\"\r\nMIME-Version: 1.0\r\nMessage-ID: <1538085644648.096e3d4e-bc38-4027-b57e-" +\
            id_generator() + b"@message-ids.attack.com>\r\nX-Email-Client: https://github.com/chenjj/espoofer\r\n\r\n"
    test_cases["server_a1"]["data"]["other_headers"] = b"Date: " + get_date() + b"\r\n" + b"Content-Type: multipart/mixed;\r\n\tboundary=\"----=_Part_111217_462031992.1680524601073\"\r\nMIME-Version: 1.0\r\nMessage-ID: <1538085644648.096e3d4e-bc38-4027-b57e-" +\
            id_generator() + b"@message-ids.attack.com>\r\nX-Email-Client: https://github.com/chenjj/espoofer\r\n\r\n"
def add_plain_text_headers():
    test_cases["server_a3"]["data"]["other_headers"] = b"Date: " + get_date() + b"\r\n" + b"Content-Type: text/plain; charset=\"UTF-8\"\r\nMIME-Version: 1.0\r\nMessage-ID: <1538085644648.096e3d4e-bc38-4027-b57e-" +\
            id_generator() + b"@message-ids.attack.com>\r\nX-Email-Client: https://github.com/chenjj/espoofer\r\n\r\n"
    test_cases["server_a4"]["data"]["other_headers"] = b"Date: " + get_date() + b"\r\n" + b"Content-Type: text/plain; charset=\"UTF-8\"\r\nMIME-Version: 1.0\r\nMessage-ID: <1538085644648.096e3d4e-bc38-4027-b57e-" +\
            id_generator() + b"@message-ids.attack.com>\r\nX-Email-Client: https://github.com/chenjj/espoofer\r\n\r\n"
    test_cases["server_a1"]["data"]["other_headers"] = b"Date: " + get_date() + b"\r\n" + b"Content-Type: text/plain; charset=\"UTF-8\"\r\nMIME-Version: 1.0\r\nMessage-ID: <1538085644648.096e3d4e-bc38-4027-b57e-" +\
            id_generator() + b"@message-ids.attack.com>\r\nX-Email-Client: https://github.com/chenjj/espoofer\r\n\r\n"
def add_wrong_headers():
    test_cases["server_a3"]["data"]["other_headers"] = b"Date: " + get_date() + b"\r\n" + b"Content-Type: multipart/alternative; boundary=\"001a113db9c28077e7054ee99e9c\"\r\nMIME-Version: 1.0\r\nMessage-ID: <1538085644648.096e3d4e-bc38-4027-b57e-" +\
            id_generator() + b"@message-ids.attack.com>\r\nX-Email-Client: https://github.com/chenjj/espoofer\r\n\r\n"
    test_cases["server_a4"]["data"]["other_headers"] = b"Date: " + get_date() + b"\r\n" + b"Content-Type: multipart/alternative; boundary=\"001a113db9c28077e7054ee99e9c\"\r\nMIME-Version: 1.0\r\nMessage-ID: <1538085644648.096e3d4e-bc38-4027-b57e-" +\
            id_generator() + b"@message-ids.attack.com>\r\nX-Email-Client: https://github.com/chenjj/espoofer\r\n\r\n"
    test_cases["server_a1"]["data"]["other_headers"] = b"Date: " + get_date() + b"\r\n" + b"Content-Type: multipart/alternative; boundary=\"001a113db9c28077e7054ee99e9c\"\r\nMIME-Version: 1.0\r\nMessage-ID: <1538085644648.096e3d4e-bc38-4027-b57e-" +\
            id_generator() + b"@message-ids.attack.com>\r\nX-Email-Client: https://github.com/chenjj/espoofer\r\n\r\n"
def main():
    test_account = b"anjhz0318"
    test_domain = b"gmail.com"
    config["victim_address"]=test_account + b"@"+ test_domain
    config["to_header"]=b"To: <"+test_account+b"@"+ test_domain +b">\r\n"
    config['mode'] = "s"
    
    for tls_status in [True]:
        config["server_mode"]["starttls"] = tls_status
        if tls_status == False:
            prefix1 = b"Tls Off"
        else:
            prefix1 = b"Tls On"
        for dkim_status in [b"server_a3"]:
            config["case_id"] = dkim_status
            if dkim_status == b"server_a4":
                prefix2 = b"Dkim Invalid-"+prefix1
            elif dkim_status == b"server_a3":
                prefix2 = b"Dkim valid-"+prefix1
            else:
                prefix2 = b"No Dkim-"+prefix1
            for spf_status in [b"<admin@attack.com>"]:
                if dkim_status == b"server_a4":
                    test_cases["server_a4"]["mailfrom"] = spf_status
                elif dkim_status == b"server_a3":
                    test_cases["server_a3"]["mailfrom"] = spf_status
                else:
                    test_cases["server_a1"]["mailfrom"] = spf_status

                if spf_status == b"<admin@legitimate.com>":
                    prefix3 = b"Spf Invalid-" + prefix2
                else:
                    prefix3 = b"Spf Valid-" + prefix2

                #for dmarc_status in ["No Dmarc","None","Quarantine","Reject"]:
                for dmarc_status in ["No Dmarc"]:   
                    '''
                    if dmarc_status == "No Dmarc":
                        config["legitimate_site_address"] = b"admin@baidu.com"
                        test_cases["server_a3"]["data"]["from_header"] = b"From: <admin@baidu.com>\r\n"
                        test_cases["server_a4"]["data"]["from_header"] = b"From: <admin@baidu.com>\r\n"
                        test_cases["server_a1"]["data"]["from_header"] = b"From: <admin@baidu.com>\r\n"
                        prefix4 = b"No Dmarc-" + prefix3
                    elif dmarc_status == "None":
                        config["legitimate_site_address"] = b"admin@outlook.com"
                        test_cases["server_a3"]["data"]["from_header"] = b"From: <admin@outlook.com>\r\n"
                        test_cases["server_a4"]["data"]["from_header"] = b"From: <admin@outlook.com>\r\n"
                        test_cases["server_a1"]["data"]["from_header"] = b"From: <admin@outlook.com>\r\n"
                        prefix4 = b"Dmarc None-" + prefix3
                    elif dmarc_status == "Quarantine":
                        config["legitimate_site_address"] = b"admin@qq.com"
                        test_cases["server_a3"]["data"]["from_header"] = b"From: <admin@qq.com>\r\n"
                        test_cases["server_a4"]["data"]["from_header"] = b"From: <admin@qq.com>\r\n"
                        test_cases["server_a1"]["data"]["from_header"] = b"From: <admin@qq.com>\r\n"
                        prefix4 = b"Dmarc Quarantine-" + prefix3
                    else:
                        config["legitimate_site_address"] = b"admin@yahoo.com"
                        test_cases["server_a3"]["data"]["from_header"] = b"From: <admin@yahoo.com>\r\n"
                        test_cases["server_a4"]["data"]["from_header"] = b"From: <admin@yahoo.com>\r\n"
                        test_cases["server_a1"]["data"]["from_header"] = b"From: <admin@yahoo.com>\r\n"
                        prefix4 = b"Dmarc Reject-" + prefix3
                    '''
                    config["legitimate_site_address"] = b"admin@anjhz.com"
                    test_cases["server_a3"]["data"]["from_header"] = b"From: <admin@anjhz.com>\r\n"
                    prefix4 = b"Normal-" + prefix3
                    '''
                    for i in range(1):
                        config["subject_header"]=b"Subject: "+prefix4+b"-URL-"+str(i+1).encode()+b"\r\n"
                        config["body"]=testbody.url_body
                        add_multipart_headers()
                        send_test_mail()
                        time.sleep(3)
    
                    for i in range(1):
                        config["subject_header"]=b"Subject: "+prefix4+b"-Attachment-"+str(i+1).encode()+b"\r\n"
                        config["body"]=testbody.attachment_body
                        add_multipart_headers()
                        send_test_mail()
                        time.sleep(3)
    
                    for i in range(1):
                        config["subject_header"]=b"Subject: "+prefix4+b"-Attachment and URL-"+str(i+1).encode()+b"\r\n"
                        config["body"]=testbody.attachment_and_url_body
                        add_multipart_headers()
                        send_test_mail()
                        time.sleep(3)

                    for i in range(1):
                        config["subject_header"]=b"Subject: "+prefix4+b"-Text Only-"+str(i+1).encode()+b"\r\n"
                        config["body"]=testbody.text_only_body
                        add_multipart_headers()
                        send_test_mail()
                        time.sleep(3)

                    for i in range(1):
                        config["subject_header"]=b"Subject: "+prefix4+b"-Text and URL-"+str(i+1).encode()+b"\r\n"
                        config["body"]=testbody.text_and_url_body
                        add_multipart_headers()
                        send_test_mail()
                        time.sleep(3)

                    for i in range(1):
                        config["subject_header"]=b"Subject: "+prefix4+b"-Text and Attachment-"+str(i+1).encode()+b"\r\n"
                        config["body"]=testbody.text_and_attachment_body
                        add_multipart_headers()
                        send_test_mail()
                        time.sleep(3)

                    for i in range(1):
                        config["subject_header"]=b"Subject: "+prefix4+b"-Text and URL and Attachment-"+str(i+1).encode()+b"\r\n"
                        config["body"]=testbody.text_and_url_and_attachment_body
                        add_multipart_headers()
                        send_test_mail()
                        time.sleep(3)
                    '''
                    '''
                    for i in range(3):
                        config["subject_header"]=b"Subject: "+prefix4+b"-Plain Text-"+str(i+1).encode()+b"\r\n"
                        config["body"]=testbody.random_body
                        add_wrong_headers()
                        send_test_mail()
                        time.sleep(3)
                    '''
                    
                    '''
                    for i in range(3):
                        config["subject_header"]=b"Subject: "+prefix4+b"-Default body-"+str(i+1).encode()+b"\r\n"
                        config["body"]=testbody.default_body
                        add_plain_text_headers()
                        send_test_mail()
                        time.sleep(3)
                    '''
                    
                    for i in range(3):
                        config["subject_header"]=b"Subject: "+prefix4+b"-Random Plain Text-"+str(i+1).encode()+b"\r\n"
                        config["body"]=testbody.random_plain_text
                        add_plain_text_headers()
                        send_test_mail()
                        time.sleep(3)
                    
    
if __name__ == '__main__':
    main()