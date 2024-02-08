import tkinter as tk
from tkinter import filedialog

def create_new_id(id_list):
    new_id = []
    for number in id_list:
        new_id.append(add_star(number.strip()))  #remove end of line character
    return new_id

def add_star(number): #adds stars to the 7 numbers in the middle of the id
    if len(number) != 11:
        return number

    left_index = 2
    right_index = 9

    new_id = number[:left_index] + "*******" + number[right_index:]
    return new_id

def select_file():
    file_name = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_name:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_name)

def process_file():
    file_name = file_entry.get()
    try:
        with open(file_name, 'r') as file:
            ids = file.readlines()
    except FileNotFoundError:
        result_label.config(text="File not found.")
        return

    new_id = create_new_id(ids)

    output_file_name = "new_id.txt" # save as a txt
    with open(output_file_name, 'w') as output_file:
        for number in new_id:
            output_file.write("%s\n" % number)

    result_label.config(text="Done. New starred ids saved as 'new_id.txt'.")

# Create GUI
root = tk.Tk()
root.title("ID Star Adder by purtas")

file_label = tk.Label(root, text="Select txt file:")
file_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=5, pady=5)

select_button = tk.Button(root, text="Select", command=select_file)
select_button.grid(row=0, column=2, padx=5, pady=5)

process_button = tk.Button(root, text="Process", command=process_file)
process_button.grid(row=1, column=1, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
