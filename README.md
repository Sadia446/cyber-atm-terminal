# Cyber ATM Terminal

A console-based ATM simulator with a boxed, colorized terminal UI. Insert a virtual card, authenticate with a PIN, and check your balance, withdraw cash, or transfer funds — all rendered with clean ANSI-styled panels.

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen)

## Features

- PIN Authentication — 3 attempts before the card is retained
- Check Balance — view your current balance in a formatted panel
- Withdraw Cash — with validation for invalid, negative, or insufficient amounts
- Transfer Funds — send money to a 10-digit account number
- Styled Terminal UI — boxed panels and color-coded output (no external dependencies)
- Transaction Logging — every transaction is recorded to reference.log

## Preview

```
╔══════════════════════════════════════════════════════╗
║                 CYBER ATM TERMINAL                    ║
║           Author: Sadia Noreen                        ║
╚══════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════╗
║                     MAIN MENU                          ║
╠══════════════════════════════════════════════════════╣
║ 1. Check Balance                                        ║
║ 2. Withdraw                                              ║
║ 3. Transfer                                              ║
║ 4. Exit                                                  ║
╚══════════════════════════════════════════════════════╝
```

## Getting Started

### Prerequisites

- Python 3.7 or later
- A terminal that supports ANSI escape codes (most Linux/macOS terminals and Windows Terminal work out of the box)

### Installation

```bash
git clone https://github.com/<Sadia446>/cyber-atm-terminal.git
cd cyber-atm-terminal
```

No external packages required — the project only uses the Python standard library.

### Usage

```bash
python3 cyber_atm_terminal.py
```

Follow the on-screen prompts:

1. Enter your PIN when prompted (see Demo PINs below)
2. Choose an option from the main menu
3. Repeat transactions or exit when done

### Demo PINs

For demo purposes, any of the following PINs will authenticate:

```
1234, 1122, 1133, 1803, 1672, 1110, 1111
```

## Project Structure

```
cyber-atm-terminal/
├── cyber_atm_terminal.py   # Main application
├── reference.log           # Auto-generated transaction log
└── README.md
```

## How It Works

- `authenticate()` handles PIN entry and attempt limiting
- `Account` holds the current balance in memory for the session
- `run_session()` drives the main menu loop
- `check_balance()`, `withdraw()`, and `transfer()` handle each transaction type
- All actions are logged via Python's built-in `logging` module

## Roadmap

- [ ] Persist account balances between sessions
- [ ] Support multiple accounts / card numbers
- [ ] Add unit tests
- [ ] Optional configuration file for starting balance and PINs

## Contributing

Contributions are welcome. Feel free to open an issue or submit a pull request.


## Author

**Sadia Noreen**