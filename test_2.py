def main():
    try:
        # request from user: name, surname, email
        name = input("first name: ")
        surname = input("last name: ")
        email = input("email: ")

        # file entry
        file = open("userinfo.txt", "a")
        file.write(name + " " + surname + "\n")
        file.write(email + "\n")
        file.write("\n")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # close the file in any case
        if 'file' in locals():
            file.close()


if __name__ == '__main__':
    main()
