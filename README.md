# Ponyville Bank 🏦

> *It was an honor suffering with you.*

Ponyville Bank is a command-line banking system built with Python. It started as a project to practise Python fundamentals and eventually became my hands-on introduction to Object-Oriented Programming (OOP).

After months of development and two prototypes, this project is being archived as a learning project.

## About the Project

Ponyville Bank simulates a basic banking system where users can create accounts, log in, view account information, and perform basic banking operations.

It was built to practise programming concepts rather than to serve as a real banking application.

## Features

The project includes implementations of:

- **Account creation** – Create accounts with a name, account number, and PIN.
- **Login system** – Authenticate users using their account number and PIN.
- **Account information** – View account details and current balance.
- **Deposits** – Add money to an account, with a $10,000 deposit limit.
- **Withdrawals** – Withdraw money from an account.
- **Transfers** – Transfer money between account objects.
- **Input validation** – Validate account numbers, PINs, names, and numeric input.
- **Account management** – Create, find, and delete accounts through the `Bank` class.

*Some features have known bugs and are not fully reliable.*

## Project Structure

The project is separated into three Python files:

| File | Responsibility |
|---|---|
| `main.py` | Main menu, user interaction, and application flow |
| `classes.py` | `Bank` and `Account` classes and their methods |
| `validator.py` | Input validation functions |

### Object-Oriented Design

The project uses two main classes:

**`Bank`**
- Maintains a collection of account objects.
- Creates and finds accounts.
- Handles login and account deletion.

**`Account`**
- Stores account information.
- Maintains the account balance.
- Provides deposit, withdrawal, and transfer operations.

## Requirements

- Python 3.x
- No external libraries required.

## Running the Project

1. Download or clone the project.
2. Keep all three Python files in the same directory.
3. Open a terminal in that directory.
4. Run:

```bash
python main.py
```

The application starts with a command-line menu.

## Known Limitations

This is an archived prototype, not a finished banking application.

Some known limitations include:

- Account data is stored in memory and is lost when the program exits.
- Account lookup and duplicate-account checking have logical issues.
- Login attempt limiting is incomplete.
- Some invalid deposit and withdrawal amounts can still reach the account methods.
- Withdrawal and transfer operations have edge cases that need correction.
- The application does not use secure PIN storage or production-grade authentication.

These limitations are part of the project's development history.

## What I Learned

Ponyville Bank helped me practise and understand:

- Python functions, loops, conditionals, and data structures.
- Input validation and error handling.
- Working with multiple Python modules.
- Classes, objects, attributes, and methods.
- Object interaction and responsibility separation.
- Designing a project around a collection of objects.
- Debugging logical errors and tracing problems across multiple files.

Most importantly, it taught me that writing code is only one part of programming. Understanding how different parts of a system interact is just as important.

## Project Status

**Archived — Prototype 2**

No further prototypes are planned.

The project is being preserved as a record of my Python learning journey. Its purpose was educational, and it served that purpose.

---

*Thank you, Ponyville Bank. You were not the prettiest banking system, but you were my banking system.*

🫡
