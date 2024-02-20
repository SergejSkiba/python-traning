def main():
    # request from user: name, surname, email
    name = input("first name: ")
    surname = input("last name: ")
    email = input("email: ")
    # file entry
    with open("userinfo.txt", "a") as file:
        file.write(name + " " + surname + "\n")
        file.write(email + "\n")


if __name__ == '__main__':
     main()
