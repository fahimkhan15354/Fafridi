class Friend:
    def __init__(self, name, contact_no):
        self.name = name
        self.contact_no = contact_no


def add_friend():
    name = input("Enter friend's name: ")
    contact_no = input("Enter contact number: ")
    friend = Friend(name, contact_no)
    return friend


def display_friends(friends):
    if len(friends) == 0:
        print("No friends to display.")
    else:
        print("Friends list:")
        for friend in friends:
            print(f"Name: {friend.name}, Contact No: {friend.contact_no}")


def main():
    friends = []
    while True:
        print("\n------ Friends Management System ------")
        print("1. Add a friend")
        print("2. Display all friends")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            friend = add_friend()
            friends.append(friend)
            print("Friend added successfully!")
        elif choice == "2":
            display_friends(friends)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
