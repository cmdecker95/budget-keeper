Script to add purchases or other transactions to a budget file. Launched via Apple Shortcuts, which runs a webhook to run the script in Pythonista, given arguments passed to the Shortcut. The webhook runs the script from its synced location in iCloud, thanks to Working Copy’s repo sync feature. Budget scripts are thus able to be privatized within iCloud while the script can remain publicized and version controlled.

## How it works right now
- Through an **iOS Shortcut**, the user selects a budgeting function (like adding an expense or logging a deposit) and enters all relevant values.
- User input from the iOS Shortcut is converted into a webhook that launches this code in the **Pythonista** app (iOS).
- Along with launching the code, the **webhook** also passes the relevant values as `[sys.argv]` for use within the code.
- Arguments are handled according to the user-selected function, each of which **reads and modifies the most recent budget file** in `/budgets`.
- Finally, the modified budget file is **summarized in the Python console**.

## What I want to change
Writing budgets to text files was the original way I handled my budgets, but they are now an unnecessary middleman. I want to refactor this project to utilize secure databasing (like MongoDB or Firebase), which will improve this repo in two main ways:
- I can publicize the code while still privatizing the sensitive budget information.
- The code will not have to turn a text file into a JSON-like object *just to turn it back into text after use*.
