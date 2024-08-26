# Python CLI Calculator: A Simple Arithmetic Operations Tool

This repository contains a Python script that implements a command-line interface (CLI) calculator capable of performing basic arithmetic operations: addition, subtraction, multiplication, and division. The calculator allows users to perform consecutive calculations using the result of the previous operation. The script also includes a simple ASCII art logo, adding a bit of fun to the user experience.

## Description

The calculator script performs the following operations:

1. **Addition (+)**
2. **Subtraction (-)**
3. **Multiplication (*)**
4. **Division (/)**

### Key Features

- **Simple User Interface:** 
  - Users can choose from four basic operations: addition, subtraction, multiplication, and division.
- **Continuous Calculation:**
  - After an operation, the user can choose to continue calculating with the current result or start a new calculation.
- **Recursive Design:**
  - The calculator can restart itself if the user chooses to start a new calculation.

### How It Works

1. **User Input:**
   - The user is prompted to enter the first number.
   - The available operations are displayed, and the user selects an operation.
   - The user is then prompted to enter the second number.

2. **Calculation:**
   - The script performs the selected arithmetic operation using the two numbers provided by the user.
   - The result is displayed, and the user is given the option to continue calculating with the current result or start a new calculation.

3. **Looping:**
   - If the user decides to continue, the script allows for further operations using the previous result as the first number.
   - If the user wants to start over, the calculator resets and begins a new session.

### Example

**User Input and Output:**

```bash
What is the first number?: 10
+
-
*
/
Pick an operation: *
What is the next number?: 5
10 * 5 = 50
Type 'y' to continue calculating with 50, or type 'n' to start a new calculation.: y
Pick an operation: +
What is the next number?: 20
50 + 20 = 70
