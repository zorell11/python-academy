my_str='''Lorem ipsum dolor sit amet, consectetur adipiscing
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
        Maecenas gravida turpis nec ultrices aliquet.'''


def get_email(text):
    words = text.split()
    emails = []
    for i in words:
        if '@' in i:
            emails.append(i)
    return emails

def get_domains(mails):
    domains = []
    for i in mails:
        domains.append(i[i.find('@')+1:])
    return domains

def get_num_email(mails):
    email = []
    for i in mails:
        mail_part = i[:i.find('@')]
        if not mail_part.isalpha():
            email.append(mail_part)
    return email


def main():
    mails = get_email(my_str)
    result = {'domains':get_domains(mails), 'emails_with_nums':get_num_email(mails) }
    print(result)
    return result

main()
