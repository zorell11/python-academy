# C:\Users\zveres\Desktop\docx\learning\python\python-academy\9. Errors & Debugging\Exercises\ctecka_radku.txt
def read_file():
    file_name = input('Zadaj meno suboru: ')
    file_name = file_name.split('\\')[-1]
    output = []
    try:
        with open(file_name, 'r') as file:
            for i in file.readlines():
                output.append(i)
        print(output)
    except FileNotFoundError:
        print(output)
        print('Soubor %s nebyl nalezen!' %file_name)
def main():
    read_file()

main()
