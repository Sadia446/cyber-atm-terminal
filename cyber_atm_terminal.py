"""
Cyber ATM Terminal
Author : Sadia Noreen


A console-based ATM simulator with a boxed, colorized UI.
Renamed from atm.py -> cyber_atm_terminal.py
"""

import os
import sys
import time
import logging
from datetime import datetime


# ---------------------------------------------------------------------------
# Visual styling helpers
# ---------------------------------------------------------------------------

class C:
    """ANSI color / style codes."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    GREEN = "\033[32m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    WHITE = "\033[97m"


WIDTH = 54


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def box_top():
    print(C.CYAN + "╔" + "═" * WIDTH + "╗" + C.RESET)


def box_bottom():
    print(C.CYAN + "╚" + "═" * WIDTH + "╝" + C.RESET)


def box_divider():
    print(C.CYAN + "╠" + "═" * WIDTH + "╣" + C.RESET)


def box_line(text="", color=C.WHITE, center=True):
    text = text[:WIDTH - 2]
    if center:
        text = text.center(WIDTH - 2)
    else:
        text = " " + text.ljust(WIDTH - 3)
    print(C.CYAN + "║" + C.RESET + color + text + C.RESET + C.CYAN + "║" + C.RESET)


def banner():
    box_top()
    box_line("CYBER ATM TERMINAL", C.BOLD + C.GREEN)
    box_line("Author: Sadia Noreen  ", C.DIM + C.WHITE)
    box_bottom()


def pause(msg, seconds=0.8):
    print(C.DIM + msg + C.RESET)
    time.sleep(seconds)


def money(amount):
    return f"${amount:,.2f}"


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    filename="reference.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(message)s",
)


# ---------------------------------------------------------------------------
# Account state
# ---------------------------------------------------------------------------

class Account:
    def __init__(self, balance=10000.0):
        self.balance = balance


# ---------------------------------------------------------------------------
# Transaction actions
# ---------------------------------------------------------------------------

def check_balance(account):
    box_top()
    box_line("ACCOUNT BALANCE", C.BOLD + C.YELLOW)
    box_divider()
    box_line(money(account.balance), C.GREEN)
    box_bottom()
    logging.debug("Transaction Type: CHECK BALANCE")


def withdraw(account):
    box_line("WITHDRAW CASH", C.BOLD + C.YELLOW)
    try:
        amount = float(input("  Enter amount to withdraw: "))
    except ValueError:
        print(C.RED + "  Invalid amount. Please use numbers only." + C.RESET)
        return

    if amount <= 0:
        print(C.RED + "  Amount must be greater than zero." + C.RESET)
        return
    if amount > account.balance:
        print(C.RED + "  Insufficient funds." + C.RESET)
        return

    pause("  Processing transaction...", 1)
    account.balance -= amount
    box_top()
    box_line("WITHDRAWAL SUCCESSFUL", C.BOLD + C.GREEN)
    box_divider()
    box_line(f"Dispensed: {money(amount)}", C.WHITE)
    box_line(f"New Balance: {money(account.balance)}", C.CYAN)
    box_bottom()
    print(C.DIM + "  Please take your cash." + C.RESET)
    logging.debug("Transaction Type: WITHDRAW - Amount: %s", amount)


def transfer(account):
    box_line("TRANSFER FUNDS", C.BOLD + C.YELLOW)
    receiver = input("  Enter recipient account number (10 digits): ").strip()
    if len(receiver) != 10 or not receiver.isdigit():
        print(C.RED + "  Invalid account number." + C.RESET)
        return

    try:
        amount = float(input("  Enter amount to transfer: "))
    except ValueError:
        print(C.RED + "  Invalid amount. Please use numbers only." + C.RESET)
        return

    if amount <= 0:
        print(C.RED + "  Amount must be greater than zero." + C.RESET)
        return
    if amount > account.balance:
        print(C.RED + "  Insufficient funds." + C.RESET)
        return

    pause("  Processing transfer...", 1)
    account.balance -= amount
    box_top()
    box_line("TRANSFER SUCCESSFUL", C.BOLD + C.GREEN)
    box_divider()
    box_line(f"Sent: {money(amount)} -> {receiver}", C.WHITE)
    box_line(f"New Balance: {money(account.balance)}", C.CYAN)
    box_bottom()
    logging.debug("Transaction Type: TRANSFER - Amount: %s To: %s", amount, receiver)


# ---------------------------------------------------------------------------
# Menu loop (replaces the old recursive transactions())
# ---------------------------------------------------------------------------

MENU_ACTIONS = {
    "1": ("Check Balance", check_balance),
    "2": ("Withdraw", withdraw),
    "3": ("Transfer", transfer),
}


def show_menu():
    box_top()
    box_line("MAIN MENU", C.BOLD + C.MAGENTA)
    box_divider()
    box_line("1. Check Balance", center=False)
    box_line("2. Withdraw", center=False)
    box_line("3. Transfer", center=False)
    box_line("4. Exit", center=False)
    box_bottom()


def run_session(account):
    while True:
        show_menu()
        choice = input(C.BOLD + "Choose an option (1-4): " + C.RESET).strip()

        if choice == "4":
            box_top()
            box_line("Thank you for banking with us!", C.BOLD + C.GREEN)
            box_line("GoodBye...", C.DIM)
            box_bottom()
            sys.exit()

        _, action = MENU_ACTIONS.get(choice, (None, None))
        if action is None:
            print(C.RED + "Please choose a valid option (1-4)." + C.RESET)
            continue

        print()
        action(account)
        print()

        again = input("Perform another transaction? (yes/no): ").strip().lower()
        if again != "yes":
            box_top()
            box_line("Thank you for banking with us!", C.BOLD + C.GREEN)
            box_line("GoodBye...", C.DIM)
            box_bottom()
            sys.exit()
        clear_screen()
        banner()


# ---------------------------------------------------------------------------
# PIN authentication
# ---------------------------------------------------------------------------

VALID_PINS = {1234, 1122, 1133, 1803, 1672, 1110, 1111}
MAX_ATTEMPTS = 3


def authenticate():
    box_top()
    box_line("CARD AUTHENTICATION", C.BOLD + C.YELLOW)
    box_bottom()

    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            pin = int(input(f"  Enter your PIN (attempt {attempt}/{MAX_ATTEMPTS}): "))
        except ValueError:
            print(C.RED + "  Use numbers only." + C.RESET)
            continue

        if pin in VALID_PINS:
            print(C.GREEN + "  Welcome to your account!" + C.RESET)
            time.sleep(1.2)
            return True

        print(C.RED + "  Incorrect PIN." + C.RESET)

    print(C.RED + C.BOLD + "  Too many failed attempts. Card retained for security." + C.RESET)
    return False


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    clear_screen()

    print(C.DIM + str(datetime.now()) + C.RESET)
    time.sleep(0.6)
    print(C.YELLOW + "Please insert your card..." + C.RESET)
    time.sleep(1.2)
    print(C.DIM + "Reading card..." + C.RESET)
    time.sleep(0.8)

    clear_screen()
    banner()

    if not authenticate():
        sys.exit()

    account = Account(balance=10000.0)
    run_session(account)


if __name__ == "__main__":
    main()