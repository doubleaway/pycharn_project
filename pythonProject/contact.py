class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr
    def print_contact(self):
        print(f"이름: {self.name}, 전화번호: {self.phone_number}, 이메일: {self.e_mail}, 주소: {self.addr}")
def set_contact():
    user_name = input("Name: ")
    user_phone_number = input("Phone number: ")
    user_e_mail = input("E mail: ")
    user_addr = input("Address: ")
    contact = Contact(user_name, user_phone_number,user_e_mail, user_addr)
    return contact
def delete_contact(user_list, user_name):
    for item in user_list:
        if user_name == item.name:
            user_list.remove(item)
def store_contact(contact_list):
    f = open("contact_db_file.txt","wt")
    for item in contact_list:
        f.write(item.name + "\n")
        f.write(item.phone_number + "\n")
        f.write(item.e_mail + "\n")
        f.write(item.addr + "\n")
    f.close()
def load_contact(contact_list):
    f = open("contact_db_file.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 4
    num = int(num)
    for i in range(num):
        name = lines[4*i].rstrip('\n')
        phone = lines[(4 * i) + 1].rstrip('\n')
        email = lines[(4 * i) + 2].rstrip('\n')
        addr = lines[(4 * i) + 3].rstrip('\n')
        contact = Contact(name,phone,email,addr)
        contact_list.append(contact)
def run():
    contact_list = []
    load_contact(contact_list)
    def print_contact_list(print_list):
        for item in print_list:
            item.print_contact()
    while(True):
        menu = print_menu()
        if menu == 1:
            contact_user = set_contact()
            contact_list.append(contact_user)
        if menu == 2:
            print_contact_list(contact_list)
        if menu == 3:
            delete_user = input("삭제할 유저 이름 ")
            delete_contact(contact_list, delete_user)
        if menu == 4:
            store_contact(contact_list)
            break

def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)
if __name__ == "__main__":
    run()