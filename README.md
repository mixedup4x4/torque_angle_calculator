# Torque-Angle Calculator

## Overview
The **Torque-Angle Calculator** is a cross-platform tool designed to calculate the estimated final torque (ft-lbs) based on an initial torque value and an applied angle of rotation. It features a user-friendly GUI built with Tkinter, making it easy to use for automotive and mechanical applications.

## Features
- Simple and intuitive **Graphical User Interface (GUI)**.
- Allows users to enter:
  - **Initial Torque (ft-lbs)**
  - **Angle of Rotation (degrees)**
  - **Optional Torque-Angle Constant** (default: `0.6` ft-lbs per degree, adjustable).
- Displays the **calculated final torque** instantly.
- Works on **Windows, macOS, and Linux**.

## Installation
### Prerequisites
Ensure you have **Python 3.7+** installed. If you don’t have it, download and install it from:
- [Python.org](https://www.python.org/downloads/)

### Install Dependencies
Tkinter is included in most Python distributions. However, if you encounter issues, install Tkinter as follows:

#### **macOS**
```bash
brew install python-tk
```

#### **Ubuntu/Debian**
```bash
sudo apt update && sudo apt install python3-tk
```

#### **Fedora/Red Hat**
```bash
sudo dnf install python3-tkinter
```

#### **Windows**
Tkinter is included by default in the official Python installer. If missing, reinstall Python and ensure **Tcl/Tk** is selected during installation.

## Usage
### **Run the Application**
Navigate to the project directory and execute:
```bash
python torque_angle_calc.py
```

### **How to Use**
1. Enter the **Initial Torque** in ft-lbs.
2. Enter the **Angle** in degrees.
3. (Optional) Adjust the **Torque-Angle Constant**.
4. Click **Calculate** to see the estimated final torque.

## Example Calculation
For an **initial torque of 74 ft-lbs** and an **angle of 80°**, the calculation would be:
```
Final Torque = 74 + (0.6 × 80) = 122 ft-lbs
```

## Contributing
Feel free to fork the repository and submit pull requests for improvements or new features.

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

## Author
Created by [valkyrie].

