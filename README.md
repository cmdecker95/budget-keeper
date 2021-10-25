## Easy as 1, 2, 3 🤑

### 1. Shortcuts App & UI

Using a custom **Shortcut**, the user chooses a budgeting function (like adding a credit card purchase or logging a deposit) and enters all relevant values into the Shortcut's input prompt.

### 2. Pythonista Webhook Arguments

The user input is parsed into arguments (by newline), then encoded and concatenated to a Safari webhook, which launches `main.py` via **Pythonista 3**, passing in the arguments as `sys.args[1:0]`. Arguments are handled according to the user-selected function, each of which **reads and modifies the most recent budget file** in the `budgets/` directory.

### 3. File Syncing

Pythonista doesn't currently support accessing iCloud files *outside* its own working directory, so the `budgets/` directory sits at the root of `//iCloud/Pythonista/`. Working Copy syncs its local copy of this repo to `//iCloud/Pythonista/budget-keeper/` so that it can access the budget files.