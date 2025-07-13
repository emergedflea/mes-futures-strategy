#Only main.py is being used for now. Other repositories are not needed.
#Futures/mes-futures-strategy/src/main.py


import tkinter as tk
from tkinter import messagebox

def evaluate_trade(rsi, price, sma):
    if rsi < 30 and price > sma:
        return "📈 LONG SIGNAL: RSI < 30 and price > SMA"
    elif rsi > 70 and price < sma:
        return "📉 SHORT SIGNAL: RSI > 70 and price < SMA"
    else:
        return "🤷‍♂️ NO SIGNAL: Conditions not met"

def on_submit():
    try:
        rsi = float(rsi_entry.get())
        price = float(price_entry.get())
        sma = float(sma_entry.get())
        decision = evaluate_trade(rsi, price, sma)
        result_label.config(text=decision)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("MES Futures Trade Recommendation")

tk.Label(root, text="RSI:").grid(row=0, column=0)
rsi_entry = tk.Entry(root)
rsi_entry.grid(row=0, column=1)

tk.Label(root, text="Current Price:").grid(row=1, column=0)
price_entry = tk.Entry(root)
price_entry.grid(row=1, column=1)

tk.Label(root, text="20-day SMA:").grid(row=2, column=0)
sma_entry = tk.Entry(root)
sma_entry.grid(row=2, column=1)

submit_btn = tk.Button(root, text="Get Recommendation", command=on_submit)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()