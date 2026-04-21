# Password Strength Checker (Task-2)

## Objective

The objective of this task is to create a Python-based password strength checker that evaluates whether a password is strong, medium, or weak based on security rules.

## Description

This project is a simple password strength checking tool developed using Python. It analyzes a user-entered password and checks whether it meets essential security requirements such as length, uppercase letters, lowercase letters, digits, and special characters.

Based on these conditions, the program classifies the password as:

* Strong Password
* Medium Password
* Weak Password

This tool helps users understand how secure their passwords are and promotes better password practices.

## Tools & Technologies Used

* Python
* Regular Expressions (re module)
* VS Code

## How It Works

The program checks the password using the following criteria:

1. Password must be at least 8 characters long
2. Must contain uppercase letters
3. Must contain lowercase letters
4. Must include numbers
5. Must include special characters

Based on how many conditions are satisfied:

* 5 conditions → Strong Password
* 3–4 conditions → Medium Password
* Less than 3 conditions → Weak Password

## Example Output

Enter your password: Secure@123
Strong Password

Enter your password: hello123
Medium Password

Enter your password: abc
Weak Password

## Learning Outcome

Through this task, I learned:

* Basics of password security
* Use of Regular Expressions in Python
* How to validate user input
* Implementing conditional logic for security evaluation

## Conclusion

This project demonstrates how Python can be used to evaluate password strength using security validation techniques. It helps improve understanding of secure password creation and input validation in cybersecurity applications.
