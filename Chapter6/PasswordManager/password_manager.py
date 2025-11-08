import pyperclip

PASSWORDS = {
    "email": "ifvn0fvr0e5404ghrieghfogeogt9043ghgi045",
    "blog": "jHBdlcblbBIB92474774fdbcshkbKHBKSQJAhdh",
    "luggage": "12345",
}

def main():
    """
    NOTE:
        to work correctly the OS must
        have copy/past mechanism
    """
    print("Enter account name: ", end="")
    account_name = input()

    if account_name in PASSWORDS:
        pyperclip.copy(PASSWORDS[account_name])
        print(f"Password for {account_name} copied to OS buffer.")
    else:
        print(f"{account_name} not exists.")