import socket
website = input("enter the website name : ")
Full_web_url = f"www.{website}"
Ip_Address = socket.gethostbyname(Full_web_url)
print(Ip_Address)