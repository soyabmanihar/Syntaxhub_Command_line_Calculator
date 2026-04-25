# 🧮 Command-Line Calculator (Python)

A simple command-line Calculator built using Python. It allows users to perform basic arithmetic operations with input validation and error handling.

---

## 📌 Features

Basic arithmetic operations:

* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`×`, `*`)
* Division (`÷`, `/`)

Tracks recent calculations (history)

Handles invalid inputs and division by zero

User-friendly prompts and instructions

Clear history option

---

## 💻 How to Use

Enter calculations in the format:

```
<number1> <operator> <number2>
```

### Example:

```
10 + 5
20 * 3
15 / 2
```

---

## 🧠 Program Logic

* User input is parsed into numbers and operator
* Input is validated before calculation
* Appropriate function is called based on operator
* Result is displayed and stored in history
* Only last 3 calculations are shown

---

## 🔁 Commands

* `clear` → Clears calculation history
* `exit` → Exits the calculator

---

## ⚠️ Error Handling

* Invalid input format is rejected
* Unsupported operators are handled
* Division by zero shows an error message

---

## 📜 License

This project is open-source and free to use.
