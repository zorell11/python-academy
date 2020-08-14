my_str = '''Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Mauris vulputate lacus id eros consequat tempus.
Nam viverra velit sit amet lorem lobortis, at tincidunt
nunc ultricies. Duis facilisis ultrices lacus, id
tiger123@email.cz auctor massa molestie at. Nunc tristique
fringilla congue. Donec ante diam cnn@info.com, dapibus
lacinia vulputate vitae, ullamcorper in justo. Maecenas
massa purus, ultricies a dictum ut, dapibus vitae massa.
Cras abc@gmail.com vel libero felis. In augue elit, porttitor
nec molestie quis, auctor a quam. Quisque b2b@money.fr
pretium dolor et tempor feugiat. Morbi libero lectus,
porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam
erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
Pellentesque id dui viverra, auctor enim ut, fringilla est.
Maecenas gravida turpis nec ultrices aliquet.
'''

#$ python3 collect_emails.py
#{'domains': ['email.cz', 'info.com,', 'gmail.com', 'money.fr', 'info.cz.'],
#'emails_with_nums': ['tiger123@email.cz', 'b2b@money.fr']}

def extract_emails(text):
    emails = []
    for i in text.split():
        if '@' in i:
            emails.append(i.strip('.,'))
    return emails

def domains(mail_list):
    domain =[]
    for i in mail_list:
        domain.append(i.split('@')[-1])
    return domain

def contain_number(word):
    for number in range(10):
        if str(number) in word:
            return True
    return False

def emails_with_nums(mail_list):
    num_mail = []
    for mail in mail_list:
        if contain_number(mail):
            num_mail.append(mail)
    return num_mail


def main():
    emails = extract_emails(my_str)
    domain = domains(emails)
    num_mail = emails_with_nums(emails)
    result = {'domains' : domain, 'emails_with_nums': num_mail}
    print(result)

main()
