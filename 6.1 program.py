def main():
    user_info = open("userinfo.txt", 'w')
    num_users = int(input("How many people do you want to add to the file?:"))
    counter = 0
    while counter < num_users:
        user_name = input("What is the name of the person?:")
        user_phone = input("What is their phone number?:")
        user_email = input("What is their email address?:")
        user_info.write(user_name + ", " + user_phone + ", " + user_email + "\n")
        counter = counter + 1
    user_info.close()


main()
