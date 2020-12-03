import sys

print(__name__)
def main():
    try:
        sys.exit()

    except SystemExit:
        inp = input('Do you really wan\'t to exit? y/n ' )
        if inp == 'y':
            print('BYE')
            raise SystemExit
        elif inp == 'n':
            print('Program continue')

if __name__ == "__main__":
    main()
