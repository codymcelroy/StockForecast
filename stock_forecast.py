# To Do - build a GUI 

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label
import numpy as np  
import pandas as pd  
from pandas_datareader import data as wb 
import matplotlib.pyplot as plt 
from scipy.stats import norm

root = tk.Tk()
root.title('Stock Forecast')
root.geometry('600x500+50+50')
root.iconbitmap('./assets/favicon.ico')

def adj_close_chart(ticker):
    data = pd.DataFrame()
    data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2017-1-1')['Adj Close']
    data.plot(figsize=(10, 6))
    plt.show()

# label with a specific font
label = ttk.Label(
    root,
    text='TICKER SYMBOL',
    font=("Helvetica", 14))

label.pack(ipadx=10, ipady=10)


email = tk.StringVar()
# email_entry = ttk.Entry(adj_close_chart, textvariable=email)

login_button = ttk.Button(root, text="Login", command=lambda: adj_close_chart(2))
login_button.pack(fill='x', expand=True, pady=10)

# exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=20,
    ipady=20,
    expand=True
)




root.mainloop()