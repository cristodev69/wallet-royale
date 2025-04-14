# Import built-in libraries
import json      # Used for reading/writing JSON files
import os        # Used for checking if the wallet file already exists

# Define the name of the file where we'll store wallets
WALLET_FILE = "wallets.json"

#Main Menu 
def main_menu():
    while True:
        print("1. Add Wallet")
        print("2. View Wallets")
        print("3. Remove Wallet")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_wallet()
        elif choice == "2":
            view_wallets()
        elif choice == "3":
            remove_wallet()
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")

# Define a function that adds a wallet
def add_wallet():
    # Check if the wallet file already exists
    if os.path.exists(WALLET_FILE):
        # If yes, open and load the existing wallets
        with open(WALLET_FILE, "r") as file:
            wallets = json.load(file)
    else:
        # If not, start with an empty list
        wallets = []

    # Ask the user to input a new wallet address
    new_wallet = input("Enter a wallet address to track: ").strip()


    # Check if this wallet address is already in the list
    for entry in wallets:
        if entry["address"] == new_wallet:
            print("This wallet is already listed.")
            return  # Stop the function if wallet already exists

    # If it's a new wallet, ask for a name/label
    name = input("Give this wallet a name: ").strip()

    # Create a dictionary to store name + address
    wallet_entry = {
        "name": name,
        "address": new_wallet
    }

    # Add the new wallet to the list
    wallets.append(wallet_entry)

    # Save the updated wallet list back to the JSON file
    with open(WALLET_FILE, "w") as file:
        json.dump(wallets, file, indent=4)

    # Confirm it worked
    print(f"Wallet '{name}' saved successfully!")

#View Wallets
def view_wallets():
    # Check if the wallet file exists
    if not os.path.exists(WALLET_FILE):
        print("No wallets found.")
        return

    # Load the existing wallets
    with open(WALLET_FILE, "r") as file:
        wallets = json.load(file)

    # Print each wallet's name and address
    for entry in wallets:
        print(f"Name: {entry['name']}, Address: {entry['address']}")
#Define a function that removes a wallet by name and address
def remove_wallet():
    # Check if the wallet file exists
    if not os.path.exists(WALLET_FILE):
        print("No wallets found.")
        return

    # Load the existing wallets
    with open(WALLET_FILE, "r") as file:
        wallets = json.load(file)

    # Ask the user for the name of the wallet to remove
    name = input("Enter the name of the wallet to remove: ").strip()

    # Ask for the address of the wallet to remove
    address = input("Enter the address of the wallet to remove: ").strip()

    # Find and remove the wallet entry
    for entry in wallets:
        if entry["name"] == name and entry["address"] == address:
            wallets.remove(entry)
            break
    else:
        print("Wallet not found.")
        return

    # Save the updated list back to the JSON file
    with open(WALLET_FILE, "w") as file:
        json.dump(wallets, file, indent=4)

    print(f"Wallet '{name}' removed successfully!")

# This ensures the menu runs only if the script is executed directly
if __name__ == "__main__":
    main_menu()