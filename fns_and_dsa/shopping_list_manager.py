def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter item to add: ").strip()
            shopping_list.append(item)
            print(f"{item} added.")
        elif choice == 2:
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed.")
            else:
                print("Item not found.")
        elif choice == 3:
            print("\nCurrent Shopping List:")
            if shopping_list:
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1-4.")

if __name__ == "__main__":
    main()