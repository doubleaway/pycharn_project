#컴퓨터 외부 및 내부 IP확인
#가상환경 등의 내부 아이피 변경되더라도 정확한 IP찾을 수 있음
import socket
'''
#여러개의 가상환경이나 다른 환경으로 인해 정확하지 않은 호스트 주소를 리턴
in_addr = socket.gethostbyname(socket.gethostname())
print(in_addr)'''

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))
print(in_addr.getsockname()[0])