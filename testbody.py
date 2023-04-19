url_body=b"------=_Part_111217_462031992.1680524601073\r\n"+\
            b"Content-Type: multipart/alternative;\r\n"+\
            b"\tboundary=\"----=_Part_111219_2139611906.1680524601073\"\r\n"+\
            b"\r\n"+\
            b"------=_Part_111219_2139611906.1680524601073\r\n"+\
            b"Content-Type: text/plain; charset=GBK\r\n"+\
            b"Content-Transfer-Encoding: 7bit\r\n"+\
            b"\r\n"+\
            b"https://www.tsinghua.edu.cn/\r\n"+\
            b"------=_Part_111219_2139611906.1680524601073\r\n"+\
            b"Content-Type: text/html; charset=GBK\r\n"+\
            b"Content-Transfer-Encoding: 7bit\r\n"+\
            b"\r\n"+\
            b"<div style=\"line-height:1.7;color:#000000;font-size:14px;font-family:Arial\"><div style=\"line-height: 1.7;\"><p style=\"margin: 0px;\"><a href=\"https://www.tsinghua.edu.cn/\" _src=\"https://www.tsinghua.edu.cn/\">https://www.tsinghua.edu.cn/</a> </p></div></div>\r\n"+\
            b"------=_Part_111219_2139611906.1680524601073--\r\n"+\
            b"\r\n"+\
            b"------=_Part_111217_462031992.1680524601073--\r\n"

attachment_body=b"------=_Part_111217_462031992.1680524601073\r\n"+\
            b"Content-Type: application/zip; name=whatever.zip\r\n"+\
            b"Content-Transfer-Encoding: base64\r\n"+\
            b"Content-Disposition: attachment; filename=\"whatever.zip\"\r\n"+\
            b"\r\n"+\
            b"UEsDBBQAAAAIACule1azQxFOCgAAAAgAAAAMAAAAd2hhdGV2ZXIudHh0K89ILEktSy0CAFBLAQIU\r\n"+\
            b"ABQAAAAIACule1azQxFOCgAAAAgAAAAMACQAAAAAAAAAIAAAAAAAAAB3aGF0ZXZlci50eHQKACAA\r\n"+\
            b"AAAAAAEAGAB14rFuqWDZAXK5MW+pYNkBGBwcaKlg2QFQSwUGAAAAAAEAAQBeAAAANAAAAAAA\r\n"+\
            b"------=_Part_111217_462031992.1680524601073--\r\n"

attachment_and_url_body=b"------=_Part_111217_462031992.1680524601073\r\n"+\
            b"Content-Type: multipart/alternative;\r\n"+\
            b"\tboundary=\"----=_Part_111219_2139611906.1680524601073\"\r\n"+\
            b"\r\n"+\
            b"------=_Part_111219_2139611906.1680524601073\r\n"+\
            b"Content-Type: text/plain; charset=GBK\r\n"+\
            b"Content-Transfer-Encoding: 7bit\r\n"+\
            b"\r\n"+\
            b"https://www.tsinghua.edu.cn/\r\n"+\
            b"------=_Part_111219_2139611906.1680524601073\r\n"+\
            b"Content-Type: text/html; charset=GBK\r\n"+\
            b"Content-Transfer-Encoding: 7bit\r\n"+\
            b"\r\n"+\
            b"<div style=\"line-height:1.7;color:#000000;font-size:14px;font-family:Arial\"><div style=\"line-height: 1.7;\"><p style=\"margin: 0px;\"><a href=\"https://www.tsinghua.edu.cn/\" _src=\"https://www.tsinghua.edu.cn/\">https://www.tsinghua.edu.cn/</a> </p></div></div>\r\n"+\
            b"------=_Part_111219_2139611906.1680524601073--\r\n"+\
            b"\r\n"+\
            b"------=_Part_111217_462031992.1680524601073\r\n"+\
            b"Content-Type: application/zip; name=whatever.zip\r\n"+\
            b"Content-Transfer-Encoding: base64\r\n"+\
            b"Content-Disposition: attachment; filename=\"whatever.zip\"\r\n"+\
            b"\r\n"+\
            b"UEsDBBQAAAAIACule1azQxFOCgAAAAgAAAAMAAAAd2hhdGV2ZXIudHh0K89ILEktSy0CAFBLAQIU\r\n"+\
            b"ABQAAAAIACule1azQxFOCgAAAAgAAAAMACQAAAAAAAAAIAAAAAAAAAB3aGF0ZXZlci50eHQKACAA\r\n"+\
            b"AAAAAAEAGAB14rFuqWDZAXK5MW+pYNkBGBwcaKlg2QFQSwUGAAAAAAEAAQBeAAAANAAAAAAA\r\n"+\
            b"------=_Part_111217_462031992.1680524601073--\r\n"

text_only_body=b"------=_Part_111217_462031992.1680524601073\r\n"+\
            b"Content-Type: multipart/alternative;\r\n"+\
            b"\tboundary=\"----=_Part_111219_2139611906.1680524601073\"\r\n"+\
            b"\r\n"+\
            b"------=_Part_111219_2139611906.1680524601073\r\n"+\
            b"Content-Type: text/plain; charset=GBK\r\n"+\
            b"Content-Transfer-Encoding: base64\r\n"+\
            b"\r\n"+\
            b"RG8gbm90IGdvIGdlbnRsZSBpbnRvIHRoYXQgZ29vZCBuaWdodCwKCk9sZCBhZ2Ugc2hvdWxkIGJ1\r\n"+\
            b"cm4gYW5kIHJhdmUgYXQgY2xvc2Ugb2YgZGF5OwoKUmFnZSwgcmFnZSBhZ2FpbnN0IHRoZSBkeWlu\r\n"+\
            b"ZyBvZiB0aGUgbGlnaHQuCgpUaG91Z2ggd2lzZSBtZW4gYXQgdGhlaXIgZW5kIGtub3cgZGFyayBp\r\n"+\
            b"cyByaWdodCwKCkJlY2F1c2UgdGhlaXIgd29yZHMgaGFkIGZvcmtlZCBubyBsaWdodG5pbmcgdGhl\r\n"+\
            b"eQoKRG8gbm90IGdvIGdlbnRsZSBpbnRvIHRoYXQgZ29vZCBuaWdodC4KCkdvb2QgbWVuLCB0aGUg\r\n"+\
            b"bGFzdCB3YXZlIGJ5LCBjcnlpbmcgaG93IGJyaWdodAoKVGhlaXIgZnJhaWwgZGVlZHMgbWlnaHQg\r\n"+\
            b"aGF2ZSBkYW5jZWQgaW4gYSBncmVlbiBiYXksCgpSYWdlLCByYWdlIGFnYWluc3QgdGhlIGR5aW5n\r\n"+\
            b"IG9mIHRoZSBsaWdodC4KCldpbGQgbWVuIHdobyBjYXVnaHQgYW5kIHNhbmcgdGhlIHN1biBpbiBm\r\n"+\
            b"bGlnaHQsCgpBbmQgbGVhcm4sIHRvbyBsYXRlLCB0aGV5IGdyaWV2ZWQgaXQgb24gaXRzIHdheSwK\r\n"+\
            b"CkRvIG5vdCBnbyBnZW50bGUgaW50byB0aGF0IGdvb2QgbmlnaHQuCgpHcmF2ZSBtZW4sIG5lYXIg\r\n"+\
            b"ZGVhdGgsIHdobyBzZWUgd2l0aCBibGluZGluZyBzaWdodAoKQmxpbmQgZXllcyBjb3VsZCBibGF6\r\n"+\
            b"ZSBsaWtlIG1ldGVvcnMgYW5kIGJlIGdheSwKClJhZ2UsIHJhZ2UgYWdhaW5zdCB0aGUgZHlpbmcg\r\n"+\
            b"b2YgdGhlIGxpZ2h0LgoKQW5kIHlvdSwgbXkgZmF0aGVyLCB0aGVyZSBvbiB0aGUgc2FkIGhlaWdo\r\n"+\
            b"dCwKCkN1cnNlLCBibGVzcyBtZSBub3cgd2l0aCB5b3VyIGZpZXJjZSB0ZWFycywgSSBwcmF5LgoK\r\n"+\
            b"RG8gbm90IGdvIGdlbnRsZSBpbnRvIHRoYXQgZ29vZCBuaWdodC4KClJhZ2UsIHJhZ2UgYWdhaW5z\r\n"+\
            b"dCB0aGUgZHlpbmcgb2YgdGhlIGxpZ2h0LiAKCgoK\r\n"+\
            b"------=_Part_111219_2139611906.1680524601073\r\n"+\
            b"Content-Type: text/html; charset=GBK\r\n"+\
            b"Content-Transfer-Encoding: base64\r\n"+\
            b"\r\n"+\
            b"PGRpdiBzdHlsZT0ibGluZS1oZWlnaHQ6MS43O2NvbG9yOiMwMDAwMDA7Zm9udC1zaXplOjE0cHg7\r\n"+\
            b"Zm9udC1mYW1pbHk6QXJpYWwiPjxwIHN0eWxlPSJtYXJnaW46MDsiPkRvIG5vdCBnbyBnZW50bGUg\r\n"+\
            b"aW50byB0aGF0IGdvb2QgbmlnaHQsPC9wPjxwIHN0eWxlPSJtYXJnaW46MDsiPk9sZCBhZ2Ugc2hv\r\n"+\
            b"dWxkIGJ1cm4gYW5kIHJhdmUgYXQgY2xvc2Ugb2YgZGF5OzwvcD48cCBzdHlsZT0ibWFyZ2luOjA7\r\n"+\
            b"Ij5SYWdlLCByYWdlIGFnYWluc3QgdGhlIGR5aW5nIG9mIHRoZSBsaWdodC48L3A+PHAgc3R5bGU9\r\n"+\
            b"Im1hcmdpbjowOyI+VGhvdWdoIHdpc2UgbWVuIGF0IHRoZWlyIGVuZCBrbm93IGRhcmsgaXMgcmln\r\n"+\
            b"aHQsPC9wPjxwIHN0eWxlPSJtYXJnaW46MDsiPkJlY2F1c2UgdGhlaXIgd29yZHMgaGFkIGZvcmtl\r\n"+\
            b"ZCBubyBsaWdodG5pbmcgdGhleTwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5EbyBub3QgZ28gZ2Vu\r\n"+\
            b"dGxlIGludG8gdGhhdCBnb29kIG5pZ2h0LjwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5Hb29kIG1l\r\n"+\
            b"biwgdGhlIGxhc3Qgd2F2ZSBieSwgY3J5aW5nIGhvdyBicmlnaHQ8L3A+PHAgc3R5bGU9Im1hcmdp\r\n"+\
            b"bjowOyI+VGhlaXIgZnJhaWwgZGVlZHMgbWlnaHQgaGF2ZSBkYW5jZWQgaW4gYSBncmVlbiBiYXks\r\n"+\
            b"PC9wPjxwIHN0eWxlPSJtYXJnaW46MDsiPlJhZ2UsIHJhZ2UgYWdhaW5zdCB0aGUgZHlpbmcgb2Yg\r\n"+\
            b"dGhlIGxpZ2h0LjwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5XaWxkIG1lbiB3aG8gY2F1Z2h0IGFu\r\n"+\
            b"ZCBzYW5nIHRoZSBzdW4gaW4gZmxpZ2h0LDwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5BbmQgbGVh\r\n"+\
            b"cm4sIHRvbyBsYXRlLCB0aGV5IGdyaWV2ZWQgaXQgb24gaXRzIHdheSw8L3A+PHAgc3R5bGU9Im1h\r\n"+\
            b"cmdpbjowOyI+RG8gbm90IGdvIGdlbnRsZSBpbnRvIHRoYXQgZ29vZCBuaWdodC48L3A+PHAgc3R5\r\n"+\
            b"bGU9Im1hcmdpbjowOyI+R3JhdmUgbWVuLCBuZWFyIGRlYXRoLCB3aG8gc2VlIHdpdGggYmxpbmRp\r\n"+\
            b"bmcgc2lnaHQ8L3A+PHAgc3R5bGU9Im1hcmdpbjowOyI+QmxpbmQgZXllcyBjb3VsZCBibGF6ZSBs\r\n"+\
            b"aWtlIG1ldGVvcnMgYW5kIGJlIGdheSw8L3A+PHAgc3R5bGU9Im1hcmdpbjowOyI+UmFnZSwgcmFn\r\n"+\
            b"ZSBhZ2FpbnN0IHRoZSBkeWluZyBvZiB0aGUgbGlnaHQuPC9wPjxwIHN0eWxlPSJtYXJnaW46MDsi\r\n"+\
            b"PkFuZCB5b3UsIG15IGZhdGhlciwgdGhlcmUgb24gdGhlIHNhZCBoZWlnaHQsPC9wPjxwIHN0eWxl\r\n"+\
            b"PSJtYXJnaW46MDsiPkN1cnNlLCBibGVzcyBtZSBub3cgd2l0aCB5b3VyIGZpZXJjZSB0ZWFycywg\r\n"+\
            b"SSBwcmF5LjwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5EbyBub3QgZ28gZ2VudGxlIGludG8gdGhh\r\n"+\
            b"dCBnb29kIG5pZ2h0LjwvcD48ZGl2IHN0eWxlPSJtYXJnaW46MDsiPlJhZ2UsIHJhZ2UgYWdhaW5z\r\n"+\
            b"dCB0aGUgZHlpbmcgb2YgdGhlIGxpZ2h0LiZuYnNwOzwvZGl2PjxkaXYgc3R5bGU9Im1hcmdpbjow\r\n"+\
            b"OyI+PGJyPjwvZGl2PjxkaXYgc3R5bGU9Im1hcmdpbjowOyI+PGJyPjwvZGl2PjwvZGl2Pg==\r\n"+\
            b"------=_Part_111219_2139611906.1680524601073--\r\n"+\
            b"\r\n"+\
            b"------=_Part_111217_462031992.1680524601073--\r\n"

text_and_attachment_body=b"------=_Part_111217_462031992.1680524601073\r\n"+\
            b"Content-Type: multipart/alternative;\r\n"+\
            b"\tboundary=\"----=_Part_111219_2139611906.1680524601073\"\r\n"+\
            b"\r\n"+\
            b"------=_Part_111219_2139611906.1680524601073\r\n"+\
            b"Content-Type: text/plain; charset=GBK\r\n"+\
            b"Content-Transfer-Encoding: base64\r\n"+\
            b"\r\n"+\
            b"RG8gbm90IGdvIGdlbnRsZSBpbnRvIHRoYXQgZ29vZCBuaWdodCwKCk9sZCBhZ2Ugc2hvdWxkIGJ1\r\n"+\
            b"cm4gYW5kIHJhdmUgYXQgY2xvc2Ugb2YgZGF5OwoKUmFnZSwgcmFnZSBhZ2FpbnN0IHRoZSBkeWlu\r\n"+\
            b"ZyBvZiB0aGUgbGlnaHQuCgpUaG91Z2ggd2lzZSBtZW4gYXQgdGhlaXIgZW5kIGtub3cgZGFyayBp\r\n"+\
            b"cyByaWdodCwKCkJlY2F1c2UgdGhlaXIgd29yZHMgaGFkIGZvcmtlZCBubyBsaWdodG5pbmcgdGhl\r\n"+\
            b"eQoKRG8gbm90IGdvIGdlbnRsZSBpbnRvIHRoYXQgZ29vZCBuaWdodC4KCkdvb2QgbWVuLCB0aGUg\r\n"+\
            b"bGFzdCB3YXZlIGJ5LCBjcnlpbmcgaG93IGJyaWdodAoKVGhlaXIgZnJhaWwgZGVlZHMgbWlnaHQg\r\n"+\
            b"aGF2ZSBkYW5jZWQgaW4gYSBncmVlbiBiYXksCgpSYWdlLCByYWdlIGFnYWluc3QgdGhlIGR5aW5n\r\n"+\
            b"IG9mIHRoZSBsaWdodC4KCldpbGQgbWVuIHdobyBjYXVnaHQgYW5kIHNhbmcgdGhlIHN1biBpbiBm\r\n"+\
            b"bGlnaHQsCgpBbmQgbGVhcm4sIHRvbyBsYXRlLCB0aGV5IGdyaWV2ZWQgaXQgb24gaXRzIHdheSwK\r\n"+\
            b"CkRvIG5vdCBnbyBnZW50bGUgaW50byB0aGF0IGdvb2QgbmlnaHQuCgpHcmF2ZSBtZW4sIG5lYXIg\r\n"+\
            b"ZGVhdGgsIHdobyBzZWUgd2l0aCBibGluZGluZyBzaWdodAoKQmxpbmQgZXllcyBjb3VsZCBibGF6\r\n"+\
            b"ZSBsaWtlIG1ldGVvcnMgYW5kIGJlIGdheSwKClJhZ2UsIHJhZ2UgYWdhaW5zdCB0aGUgZHlpbmcg\r\n"+\
            b"b2YgdGhlIGxpZ2h0LgoKQW5kIHlvdSwgbXkgZmF0aGVyLCB0aGVyZSBvbiB0aGUgc2FkIGhlaWdo\r\n"+\
            b"dCwKCkN1cnNlLCBibGVzcyBtZSBub3cgd2l0aCB5b3VyIGZpZXJjZSB0ZWFycywgSSBwcmF5LgoK\r\n"+\
            b"RG8gbm90IGdvIGdlbnRsZSBpbnRvIHRoYXQgZ29vZCBuaWdodC4KClJhZ2UsIHJhZ2UgYWdhaW5z\r\n"+\
            b"dCB0aGUgZHlpbmcgb2YgdGhlIGxpZ2h0LiAKCgoK\r\n"+\
            b"------=_Part_111219_2139611906.1680524601073\r\n"+\
            b"Content-Type: text/html; charset=GBK\r\n"+\
            b"Content-Transfer-Encoding: base64\r\n"+\
            b"\r\n"+\
            b"PGRpdiBzdHlsZT0ibGluZS1oZWlnaHQ6MS43O2NvbG9yOiMwMDAwMDA7Zm9udC1zaXplOjE0cHg7\r\n"+\
            b"Zm9udC1mYW1pbHk6QXJpYWwiPjxwIHN0eWxlPSJtYXJnaW46MDsiPkRvIG5vdCBnbyBnZW50bGUg\r\n"+\
            b"aW50byB0aGF0IGdvb2QgbmlnaHQsPC9wPjxwIHN0eWxlPSJtYXJnaW46MDsiPk9sZCBhZ2Ugc2hv\r\n"+\
            b"dWxkIGJ1cm4gYW5kIHJhdmUgYXQgY2xvc2Ugb2YgZGF5OzwvcD48cCBzdHlsZT0ibWFyZ2luOjA7\r\n"+\
            b"Ij5SYWdlLCByYWdlIGFnYWluc3QgdGhlIGR5aW5nIG9mIHRoZSBsaWdodC48L3A+PHAgc3R5bGU9\r\n"+\
            b"Im1hcmdpbjowOyI+VGhvdWdoIHdpc2UgbWVuIGF0IHRoZWlyIGVuZCBrbm93IGRhcmsgaXMgcmln\r\n"+\
            b"aHQsPC9wPjxwIHN0eWxlPSJtYXJnaW46MDsiPkJlY2F1c2UgdGhlaXIgd29yZHMgaGFkIGZvcmtl\r\n"+\
            b"ZCBubyBsaWdodG5pbmcgdGhleTwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5EbyBub3QgZ28gZ2Vu\r\n"+\
            b"dGxlIGludG8gdGhhdCBnb29kIG5pZ2h0LjwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5Hb29kIG1l\r\n"+\
            b"biwgdGhlIGxhc3Qgd2F2ZSBieSwgY3J5aW5nIGhvdyBicmlnaHQ8L3A+PHAgc3R5bGU9Im1hcmdp\r\n"+\
            b"bjowOyI+VGhlaXIgZnJhaWwgZGVlZHMgbWlnaHQgaGF2ZSBkYW5jZWQgaW4gYSBncmVlbiBiYXks\r\n"+\
            b"PC9wPjxwIHN0eWxlPSJtYXJnaW46MDsiPlJhZ2UsIHJhZ2UgYWdhaW5zdCB0aGUgZHlpbmcgb2Yg\r\n"+\
            b"dGhlIGxpZ2h0LjwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5XaWxkIG1lbiB3aG8gY2F1Z2h0IGFu\r\n"+\
            b"ZCBzYW5nIHRoZSBzdW4gaW4gZmxpZ2h0LDwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5BbmQgbGVh\r\n"+\
            b"cm4sIHRvbyBsYXRlLCB0aGV5IGdyaWV2ZWQgaXQgb24gaXRzIHdheSw8L3A+PHAgc3R5bGU9Im1h\r\n"+\
            b"cmdpbjowOyI+RG8gbm90IGdvIGdlbnRsZSBpbnRvIHRoYXQgZ29vZCBuaWdodC48L3A+PHAgc3R5\r\n"+\
            b"bGU9Im1hcmdpbjowOyI+R3JhdmUgbWVuLCBuZWFyIGRlYXRoLCB3aG8gc2VlIHdpdGggYmxpbmRp\r\n"+\
            b"bmcgc2lnaHQ8L3A+PHAgc3R5bGU9Im1hcmdpbjowOyI+QmxpbmQgZXllcyBjb3VsZCBibGF6ZSBs\r\n"+\
            b"aWtlIG1ldGVvcnMgYW5kIGJlIGdheSw8L3A+PHAgc3R5bGU9Im1hcmdpbjowOyI+UmFnZSwgcmFn\r\n"+\
            b"ZSBhZ2FpbnN0IHRoZSBkeWluZyBvZiB0aGUgbGlnaHQuPC9wPjxwIHN0eWxlPSJtYXJnaW46MDsi\r\n"+\
            b"PkFuZCB5b3UsIG15IGZhdGhlciwgdGhlcmUgb24gdGhlIHNhZCBoZWlnaHQsPC9wPjxwIHN0eWxl\r\n"+\
            b"PSJtYXJnaW46MDsiPkN1cnNlLCBibGVzcyBtZSBub3cgd2l0aCB5b3VyIGZpZXJjZSB0ZWFycywg\r\n"+\
            b"SSBwcmF5LjwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5EbyBub3QgZ28gZ2VudGxlIGludG8gdGhh\r\n"+\
            b"dCBnb29kIG5pZ2h0LjwvcD48ZGl2IHN0eWxlPSJtYXJnaW46MDsiPlJhZ2UsIHJhZ2UgYWdhaW5z\r\n"+\
            b"dCB0aGUgZHlpbmcgb2YgdGhlIGxpZ2h0LiZuYnNwOzwvZGl2PjxkaXYgc3R5bGU9Im1hcmdpbjow\r\n"+\
            b"OyI+PGJyPjwvZGl2PjxkaXYgc3R5bGU9Im1hcmdpbjowOyI+PGJyPjwvZGl2PjwvZGl2Pg==\r\n"+\
            b"------=_Part_111219_2139611906.1680524601073--\r\n"+\
            b"\r\n"+\
            b"------=_Part_111217_462031992.1680524601073\r\n"+\
            b"Content-Type: application/zip; name=whatever.zip\r\n"+\
            b"Content-Transfer-Encoding: base64\r\n"+\
            b"Content-Disposition: attachment; filename=\"whatever.zip\"\r\n"+\
            b"\r\n"+\
            b"UEsDBBQAAAAIACule1azQxFOCgAAAAgAAAAMAAAAd2hhdGV2ZXIudHh0K89ILEktSy0CAFBLAQIU\r\n"+\
            b"ABQAAAAIACule1azQxFOCgAAAAgAAAAMACQAAAAAAAAAIAAAAAAAAAB3aGF0ZXZlci50eHQKACAA\r\n"+\
            b"AAAAAAEAGAB14rFuqWDZAXK5MW+pYNkBGBwcaKlg2QFQSwUGAAAAAAEAAQBeAAAANAAAAAAA\r\n"+\
            b"------=_Part_111217_462031992.1680524601073--\r\n"

text_and_url_body=b"------=_Part_111217_462031992.1680524601073\r\n"+\
            b"Content-Type: multipart/alternative;\r\n"+\
            b"\tboundary=\"----=_Part_111219_2139611906.1680524601073\"\r\n"+\
            b"\r\n"+\
            b"------=_Part_111219_2139611906.1680524601073\r\n"+\
            b"Content-Type: text/plain; charset=GBK\r\n"+\
            b"Content-Transfer-Encoding: base64\r\n"+\
            b"\r\n"+\
            b"RG8gbm90IGdvIGdlbnRsZSBpbnRvIHRoYXQgZ29vZCBuaWdodCwKCk9sZCBhZ2Ugc2hvdWxkIGJ1\r\n"+\
            b"cm4gYW5kIHJhdmUgYXQgY2xvc2Ugb2YgZGF5OwoKUmFnZSwgcmFnZSBhZ2FpbnN0IHRoZSBkeWlu\r\n"+\
            b"ZyBvZiB0aGUgbGlnaHQuCgpUaG91Z2ggd2lzZSBtZW4gYXQgdGhlaXIgZW5kIGtub3cgZGFyayBp\r\n"+\
            b"cyByaWdodCwKCkJlY2F1c2UgdGhlaXIgd29yZHMgaGFkIGZvcmtlZCBubyBsaWdodG5pbmcgdGhl\r\n"+\
            b"eQoKRG8gbm90IGdvIGdlbnRsZSBpbnRvIHRoYXQgZ29vZCBuaWdodC4KCkdvb2QgbWVuLCB0aGUg\r\n"+\
            b"bGFzdCB3YXZlIGJ5LCBjcnlpbmcgaG93IGJyaWdodAoKVGhlaXIgZnJhaWwgZGVlZHMgbWlnaHQg\r\n"+\
            b"aGF2ZSBkYW5jZWQgaW4gYSBncmVlbiBiYXksCgpSYWdlLCByYWdlIGFnYWluc3QgdGhlIGR5aW5n\r\n"+\
            b"IG9mIHRoZSBsaWdodC4KCldpbGQgbWVuIHdobyBjYXVnaHQgYW5kIHNhbmcgdGhlIHN1biBpbiBm\r\n"+\
            b"bGlnaHQsCgpBbmQgbGVhcm4sIHRvbyBsYXRlLCB0aGV5IGdyaWV2ZWQgaXQgb24gaXRzIHdheSwK\r\n"+\
            b"CkRvIG5vdCBnbyBnZW50bGUgaW50byB0aGF0IGdvb2QgbmlnaHQuCgpHcmF2ZSBtZW4sIG5lYXIg\r\n"+\
            b"ZGVhdGgsIHdobyBzZWUgd2l0aCBibGluZGluZyBzaWdodAoKQmxpbmQgZXllcyBjb3VsZCBibGF6\r\n"+\
            b"ZSBsaWtlIG1ldGVvcnMgYW5kIGJlIGdheSwKClJhZ2UsIHJhZ2UgYWdhaW5zdCB0aGUgZHlpbmcg\r\n"+\
            b"b2YgdGhlIGxpZ2h0LgoKQW5kIHlvdSwgbXkgZmF0aGVyLCB0aGVyZSBvbiB0aGUgc2FkIGhlaWdo\r\n"+\
            b"dCwKCkN1cnNlLCBibGVzcyBtZSBub3cgd2l0aCB5b3VyIGZpZXJjZSB0ZWFycywgSSBwcmF5LgoK\r\n"+\
            b"RG8gbm90IGdvIGdlbnRsZSBpbnRvIHRoYXQgZ29vZCBuaWdodC4KClJhZ2UsIHJhZ2UgYWdhaW5z\r\n"+\
            b"dCB0aGUgZHlpbmcgb2YgdGhlIGxpZ2h0LiAKdHNpbmdodWEuZWR1LmNuCgo=\r\n"+\
            b"------=_Part_111219_2139611906.1680524601073\r\n"+\
            b"Content-Type: text/html; charset=GBK\r\n"+\
            b"Content-Transfer-Encoding: base64\r\n"+\
            b"\r\n"+\
            b"PGRpdiBzdHlsZT0ibGluZS1oZWlnaHQ6MS43O2NvbG9yOiMwMDAwMDA7Zm9udC1zaXplOjE0cHg7\r\n"+\
            b"Zm9udC1mYW1pbHk6QXJpYWwiPjxwIHN0eWxlPSJtYXJnaW46MDsiPkRvIG5vdCBnbyBnZW50bGUg\r\n"+\
            b"aW50byB0aGF0IGdvb2QgbmlnaHQsPC9wPjxwIHN0eWxlPSJtYXJnaW46MDsiPk9sZCBhZ2Ugc2hv\r\n"+\
            b"dWxkIGJ1cm4gYW5kIHJhdmUgYXQgY2xvc2Ugb2YgZGF5OzwvcD48cCBzdHlsZT0ibWFyZ2luOjA7\r\n"+\
            b"Ij5SYWdlLCByYWdlIGFnYWluc3QgdGhlIGR5aW5nIG9mIHRoZSBsaWdodC48L3A+PHAgc3R5bGU9\r\n"+\
            b"Im1hcmdpbjowOyI+VGhvdWdoIHdpc2UgbWVuIGF0IHRoZWlyIGVuZCBrbm93IGRhcmsgaXMgcmln\r\n"+\
            b"aHQsPC9wPjxwIHN0eWxlPSJtYXJnaW46MDsiPkJlY2F1c2UgdGhlaXIgd29yZHMgaGFkIGZvcmtl\r\n"+\
            b"ZCBubyBsaWdodG5pbmcgdGhleTwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5EbyBub3QgZ28gZ2Vu\r\n"+\
            b"dGxlIGludG8gdGhhdCBnb29kIG5pZ2h0LjwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5Hb29kIG1l\r\n"+\
            b"biwgdGhlIGxhc3Qgd2F2ZSBieSwgY3J5aW5nIGhvdyBicmlnaHQ8L3A+PHAgc3R5bGU9Im1hcmdp\r\n"+\
            b"bjowOyI+VGhlaXIgZnJhaWwgZGVlZHMgbWlnaHQgaGF2ZSBkYW5jZWQgaW4gYSBncmVlbiBiYXks\r\n"+\
            b"PC9wPjxwIHN0eWxlPSJtYXJnaW46MDsiPlJhZ2UsIHJhZ2UgYWdhaW5zdCB0aGUgZHlpbmcgb2Yg\r\n"+\
            b"dGhlIGxpZ2h0LjwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5XaWxkIG1lbiB3aG8gY2F1Z2h0IGFu\r\n"+\
            b"ZCBzYW5nIHRoZSBzdW4gaW4gZmxpZ2h0LDwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5BbmQgbGVh\r\n"+\
            b"cm4sIHRvbyBsYXRlLCB0aGV5IGdyaWV2ZWQgaXQgb24gaXRzIHdheSw8L3A+PHAgc3R5bGU9Im1h\r\n"+\
            b"cmdpbjowOyI+RG8gbm90IGdvIGdlbnRsZSBpbnRvIHRoYXQgZ29vZCBuaWdodC48L3A+PHAgc3R5\r\n"+\
            b"bGU9Im1hcmdpbjowOyI+R3JhdmUgbWVuLCBuZWFyIGRlYXRoLCB3aG8gc2VlIHdpdGggYmxpbmRp\r\n"+\
            b"bmcgc2lnaHQ8L3A+PHAgc3R5bGU9Im1hcmdpbjowOyI+QmxpbmQgZXllcyBjb3VsZCBibGF6ZSBs\r\n"+\
            b"aWtlIG1ldGVvcnMgYW5kIGJlIGdheSw8L3A+PHAgc3R5bGU9Im1hcmdpbjowOyI+UmFnZSwgcmFn\r\n"+\
            b"ZSBhZ2FpbnN0IHRoZSBkeWluZyBvZiB0aGUgbGlnaHQuPC9wPjxwIHN0eWxlPSJtYXJnaW46MDsi\r\n"+\
            b"PkFuZCB5b3UsIG15IGZhdGhlciwgdGhlcmUgb24gdGhlIHNhZCBoZWlnaHQsPC9wPjxwIHN0eWxl\r\n"+\
            b"PSJtYXJnaW46MDsiPkN1cnNlLCBibGVzcyBtZSBub3cgd2l0aCB5b3VyIGZpZXJjZSB0ZWFycywg\r\n"+\
            b"SSBwcmF5LjwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5EbyBub3QgZ28gZ2VudGxlIGludG8gdGhh\r\n"+\
            b"dCBnb29kIG5pZ2h0LjwvcD48ZGl2IHN0eWxlPSJtYXJnaW46MDsiPlJhZ2UsIHJhZ2UgYWdhaW5z\r\n"+\
            b"dCB0aGUgZHlpbmcgb2YgdGhlIGxpZ2h0LiZuYnNwOzwvZGl2PjxkaXYgc3R5bGU9Im1hcmdpbjow\r\n"+\
            b"OyI+PGEgaHJlZj0iaHR0cHM6Ly93d3cudHNpbmdodWEuZWR1LmNuLyI+dHNpbmdodWEuZWR1LmNu\r\n"+\
            b"PC9hPjwvZGl2PjxkaXYgc3R5bGU9Im1hcmdpbjowOyI+PGJyPjwvZGl2PjwvZGl2Pg==\r\n"+\
            b"------=_Part_111219_2139611906.1680524601073--\r\n"+\
            b"\r\n"+\
            b"------=_Part_111217_462031992.1680524601073--\r\n"

text_and_url_and_attachment_body=b"------=_Part_111217_462031992.1680524601073\r\n"+\
            b"Content-Type: multipart/alternative;\r\n"+\
            b"\tboundary=\"----=_Part_111219_2139611906.1680524601073\"\r\n"+\
            b"\r\n"+\
            b"------=_Part_111219_2139611906.1680524601073\r\n"+\
            b"Content-Type: text/plain; charset=GBK\r\n"+\
            b"Content-Transfer-Encoding: base64\r\n"+\
            b"\r\n"+\
            b"RG8gbm90IGdvIGdlbnRsZSBpbnRvIHRoYXQgZ29vZCBuaWdodCwKCk9sZCBhZ2Ugc2hvdWxkIGJ1\r\n"+\
            b"cm4gYW5kIHJhdmUgYXQgY2xvc2Ugb2YgZGF5OwoKUmFnZSwgcmFnZSBhZ2FpbnN0IHRoZSBkeWlu\r\n"+\
            b"ZyBvZiB0aGUgbGlnaHQuCgpUaG91Z2ggd2lzZSBtZW4gYXQgdGhlaXIgZW5kIGtub3cgZGFyayBp\r\n"+\
            b"cyByaWdodCwKCkJlY2F1c2UgdGhlaXIgd29yZHMgaGFkIGZvcmtlZCBubyBsaWdodG5pbmcgdGhl\r\n"+\
            b"eQoKRG8gbm90IGdvIGdlbnRsZSBpbnRvIHRoYXQgZ29vZCBuaWdodC4KCkdvb2QgbWVuLCB0aGUg\r\n"+\
            b"bGFzdCB3YXZlIGJ5LCBjcnlpbmcgaG93IGJyaWdodAoKVGhlaXIgZnJhaWwgZGVlZHMgbWlnaHQg\r\n"+\
            b"aGF2ZSBkYW5jZWQgaW4gYSBncmVlbiBiYXksCgpSYWdlLCByYWdlIGFnYWluc3QgdGhlIGR5aW5n\r\n"+\
            b"IG9mIHRoZSBsaWdodC4KCldpbGQgbWVuIHdobyBjYXVnaHQgYW5kIHNhbmcgdGhlIHN1biBpbiBm\r\n"+\
            b"bGlnaHQsCgpBbmQgbGVhcm4sIHRvbyBsYXRlLCB0aGV5IGdyaWV2ZWQgaXQgb24gaXRzIHdheSwK\r\n"+\
            b"CkRvIG5vdCBnbyBnZW50bGUgaW50byB0aGF0IGdvb2QgbmlnaHQuCgpHcmF2ZSBtZW4sIG5lYXIg\r\n"+\
            b"ZGVhdGgsIHdobyBzZWUgd2l0aCBibGluZGluZyBzaWdodAoKQmxpbmQgZXllcyBjb3VsZCBibGF6\r\n"+\
            b"ZSBsaWtlIG1ldGVvcnMgYW5kIGJlIGdheSwKClJhZ2UsIHJhZ2UgYWdhaW5zdCB0aGUgZHlpbmcg\r\n"+\
            b"b2YgdGhlIGxpZ2h0LgoKQW5kIHlvdSwgbXkgZmF0aGVyLCB0aGVyZSBvbiB0aGUgc2FkIGhlaWdo\r\n"+\
            b"dCwKCkN1cnNlLCBibGVzcyBtZSBub3cgd2l0aCB5b3VyIGZpZXJjZSB0ZWFycywgSSBwcmF5LgoK\r\n"+\
            b"RG8gbm90IGdvIGdlbnRsZSBpbnRvIHRoYXQgZ29vZCBuaWdodC4KClJhZ2UsIHJhZ2UgYWdhaW5z\r\n"+\
            b"dCB0aGUgZHlpbmcgb2YgdGhlIGxpZ2h0LiAKdHNpbmdodWEuZWR1LmNuCgo=\r\n"+\
            b"------=_Part_111219_2139611906.1680524601073\r\n"+\
            b"Content-Type: text/html; charset=GBK\r\n"+\
            b"Content-Transfer-Encoding: base64\r\n"+\
            b"\r\n"+\
            b"PGRpdiBzdHlsZT0ibGluZS1oZWlnaHQ6MS43O2NvbG9yOiMwMDAwMDA7Zm9udC1zaXplOjE0cHg7\r\n"+\
            b"Zm9udC1mYW1pbHk6QXJpYWwiPjxwIHN0eWxlPSJtYXJnaW46MDsiPkRvIG5vdCBnbyBnZW50bGUg\r\n"+\
            b"aW50byB0aGF0IGdvb2QgbmlnaHQsPC9wPjxwIHN0eWxlPSJtYXJnaW46MDsiPk9sZCBhZ2Ugc2hv\r\n"+\
            b"dWxkIGJ1cm4gYW5kIHJhdmUgYXQgY2xvc2Ugb2YgZGF5OzwvcD48cCBzdHlsZT0ibWFyZ2luOjA7\r\n"+\
            b"Ij5SYWdlLCByYWdlIGFnYWluc3QgdGhlIGR5aW5nIG9mIHRoZSBsaWdodC48L3A+PHAgc3R5bGU9\r\n"+\
            b"Im1hcmdpbjowOyI+VGhvdWdoIHdpc2UgbWVuIGF0IHRoZWlyIGVuZCBrbm93IGRhcmsgaXMgcmln\r\n"+\
            b"aHQsPC9wPjxwIHN0eWxlPSJtYXJnaW46MDsiPkJlY2F1c2UgdGhlaXIgd29yZHMgaGFkIGZvcmtl\r\n"+\
            b"ZCBubyBsaWdodG5pbmcgdGhleTwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5EbyBub3QgZ28gZ2Vu\r\n"+\
            b"dGxlIGludG8gdGhhdCBnb29kIG5pZ2h0LjwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5Hb29kIG1l\r\n"+\
            b"biwgdGhlIGxhc3Qgd2F2ZSBieSwgY3J5aW5nIGhvdyBicmlnaHQ8L3A+PHAgc3R5bGU9Im1hcmdp\r\n"+\
            b"bjowOyI+VGhlaXIgZnJhaWwgZGVlZHMgbWlnaHQgaGF2ZSBkYW5jZWQgaW4gYSBncmVlbiBiYXks\r\n"+\
            b"PC9wPjxwIHN0eWxlPSJtYXJnaW46MDsiPlJhZ2UsIHJhZ2UgYWdhaW5zdCB0aGUgZHlpbmcgb2Yg\r\n"+\
            b"dGhlIGxpZ2h0LjwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5XaWxkIG1lbiB3aG8gY2F1Z2h0IGFu\r\n"+\
            b"ZCBzYW5nIHRoZSBzdW4gaW4gZmxpZ2h0LDwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5BbmQgbGVh\r\n"+\
            b"cm4sIHRvbyBsYXRlLCB0aGV5IGdyaWV2ZWQgaXQgb24gaXRzIHdheSw8L3A+PHAgc3R5bGU9Im1h\r\n"+\
            b"cmdpbjowOyI+RG8gbm90IGdvIGdlbnRsZSBpbnRvIHRoYXQgZ29vZCBuaWdodC48L3A+PHAgc3R5\r\n"+\
            b"bGU9Im1hcmdpbjowOyI+R3JhdmUgbWVuLCBuZWFyIGRlYXRoLCB3aG8gc2VlIHdpdGggYmxpbmRp\r\n"+\
            b"bmcgc2lnaHQ8L3A+PHAgc3R5bGU9Im1hcmdpbjowOyI+QmxpbmQgZXllcyBjb3VsZCBibGF6ZSBs\r\n"+\
            b"aWtlIG1ldGVvcnMgYW5kIGJlIGdheSw8L3A+PHAgc3R5bGU9Im1hcmdpbjowOyI+UmFnZSwgcmFn\r\n"+\
            b"ZSBhZ2FpbnN0IHRoZSBkeWluZyBvZiB0aGUgbGlnaHQuPC9wPjxwIHN0eWxlPSJtYXJnaW46MDsi\r\n"+\
            b"PkFuZCB5b3UsIG15IGZhdGhlciwgdGhlcmUgb24gdGhlIHNhZCBoZWlnaHQsPC9wPjxwIHN0eWxl\r\n"+\
            b"PSJtYXJnaW46MDsiPkN1cnNlLCBibGVzcyBtZSBub3cgd2l0aCB5b3VyIGZpZXJjZSB0ZWFycywg\r\n"+\
            b"SSBwcmF5LjwvcD48cCBzdHlsZT0ibWFyZ2luOjA7Ij5EbyBub3QgZ28gZ2VudGxlIGludG8gdGhh\r\n"+\
            b"dCBnb29kIG5pZ2h0LjwvcD48ZGl2IHN0eWxlPSJtYXJnaW46MDsiPlJhZ2UsIHJhZ2UgYWdhaW5z\r\n"+\
            b"dCB0aGUgZHlpbmcgb2YgdGhlIGxpZ2h0LiZuYnNwOzwvZGl2PjxkaXYgc3R5bGU9Im1hcmdpbjow\r\n"+\
            b"OyI+PGEgaHJlZj0iaHR0cHM6Ly93d3cudHNpbmdodWEuZWR1LmNuLyI+dHNpbmdodWEuZWR1LmNu\r\n"+\
            b"PC9hPjwvZGl2PjxkaXYgc3R5bGU9Im1hcmdpbjowOyI+PGJyPjwvZGl2PjwvZGl2Pg==\r\n"+\
            b"------=_Part_111219_2139611906.1680524601073--\r\n"+\
            b"\r\n"+\
            b"------=_Part_111217_462031992.1680524601073\r\n"+\
            b"Content-Type: application/zip; name=whatever.zip\r\n"+\
            b"Content-Transfer-Encoding: base64\r\n"+\
            b"Content-Disposition: attachment; filename=\"whatever.zip\"\r\n"+\
            b"\r\n"+\
            b"UEsDBBQAAAAIACule1azQxFOCgAAAAgAAAAMAAAAd2hhdGV2ZXIudHh0K89ILEktSy0CAFBLAQIU\r\n"+\
            b"ABQAAAAIACule1azQxFOCgAAAAgAAAAMACQAAAAAAAAAIAAAAAAAAAB3aGF0ZXZlci50eHQKACAA\r\n"+\
            b"AAAAAAEAGAB14rFuqWDZAXK5MW+pYNkBGBwcaKlg2QFQSwUGAAAAAAEAAQBeAAAANAAAAAAA\r\n"+\
            b"------=_Part_111217_462031992.1680524601073--\r\n"
content_boundary_begin=b"------=_Part_111219_2139611906.1680524601073\r\n"
content_boundary_end=b"------=_Part_111217_462031992.1680524601073--\r\n"

plain_text = b"Do not go gentle into that good night,\r\n"+\
            b"Old age should burn and rave at close of day;\r\n"+\
            b"Rage, rage against the dying of the light.\r\n"+\
            b"Though wise men at their end know dark is right,\r\n"+\
            b"Because their words had forked no lightning they\r\n"+\
            b"Do not go gentle into that good night.\r\n"+\
            b"Good men, the last wave by, crying how bright\r\n"+\
            b"Their frail deeds might have danced in a green bay,\r\n"+\
            b"Rage, rage against the dying of the light.\r\n"+\
            b"Wild men who caught and sang the sun in flight,\r\n"+\
            b"And learn, too late, they grieved it on its way,\r\n"+\
            b"Do not go gentle into that good night.\r\n"+\
            b"Grave men, near death, who see with blinding sight\r\n"+\
            b"Blind eyes could blaze like meteors and be gay,\r\n"+\
            b"Rage, rage against the dying of the light.\r\n"+\
            b"And you, my father, there on the sad height,\r\n"+\
            b"Curse, bless me now with your fierce tears, I pray.\r\n"+\
            b"Do not go gentle into that good night.\r\n"+\
            b"Rage, rage against the dying of the light.\r\n"