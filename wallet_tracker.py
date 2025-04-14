# Import built-in libraries
import json      # Used for reading/writing JSON files
import os        # Used for checking if the wallet file already exists

# Define the name of the file where we'll store wallets
WALLET_FILE = "wallets.json"

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

# This ensures the function runs only if the script is executed directly
if __name__ == "__main__":
    add_wallet()