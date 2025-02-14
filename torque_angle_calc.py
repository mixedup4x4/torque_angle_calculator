import tkinter as tk
from tkinter import messagebox

def calculate_final_torque():
    try:
        initial_torque = float(entry_torque.get())
        angle = float(entry_angle.get())
        torque_angle_constant = float(entry_constant.get()) if entry_constant.get() else 0.6
        
        final_torque = initial_torque + (torque_angle_constant * angle)
        result_label.config(text=f"Estimated Final Torque: {final_torque:.2f} ft-lbs")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# GUI Setup
root = tk.Tk()
root.title("Torque-Angle Calculator")
root.geometry("350x250")

tk.Label(root, text="Initial Torque (ft-lbs):").pack()
entry_torque = tk.Entry(root)
entry_torque.pack()

tk.Label(root, text="Angle (degrees):").pack()
entry_angle = tk.Entry(root)
entry_angle.pack()

tk.Label(root, text="Torque-Angle Constant (optional, default 0.6):").pack()
entry_constant = tk.Entry(root)
entry_constant.pack()

tk.Button(root, text="Calculate", command=calculate_final_torque).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
