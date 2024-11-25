import tkinter as tk

def sigma_calculator():
    global result_label
    result1 = 0
    result2 = 0
    
    # Calculate the sum for number1 and number2
    for num in range(1, int(number1.get()) + 1):
        result1 += num
    for num in range(1, int(number2.get()) + 1):
        result2 += num
    
    # Update the label with the results
    result_label.config(text=f"Result A: {result1}, Result B: {result2}")

# Initialize the Tkinter root window
root = tk.Tk()
number1 = tk.StringVar()
number2 = tk.StringVar()

root.geometry("300x200")

# Entry widgets for input
entry1 = tk.Entry(root, textvariable=number1)
entry1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

entry2 = tk.Entry(root, textvariable=number2)
entry2.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# Button to calculate the sigma sums
button = tk.Button(root, text="Result", command=sigma_calculator)
button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
label_number1= tk.Label(root, text = "Number A:")
label_number2= tk.Label(root, text = "Number B:")
label_number1.place(relx=0.15, rely=0.3, anchor=tk.CENTER)
label_number2.place(relx=0.15, rely=0.6, anchor=tk.CENTER)
# Label to display the result
result_label = tk.Label(root, text="Results will appear here")
result_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# Start the Tkinter main loop
root.mainloop()
