class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr
    def print_info(self):
        print(f"이름: {self.name}, 전화번호: {self.phone_number}, 이메일: {self.e_mail}, 주소: {self.addr}")
def run():
    contact_ins = Contact('홍길동','01012345678','hongildong@gmail.com','경기도 부천시 ')
    contact_ins.print_info()
if __name__ == "__main__":
    run()