import tkinter as tk
from tkinter import messagebox


def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning!", "Please enter task!")


def delete_task():
    try:
        selected_task_indx = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_indx)
    except IndexError:
        messagebox.showwarning("Warning!", "Please select a task to delete!")


root = tk.Tk()
root.title("To-Do list")

task_entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Add Task", width=10, command=add_task)
delete_button = tk.Button(root, text="Delete Task", width=10, command=delete_task)
tasks_listbox = tk.Listbox(root, width=50)

task_entry.grid(row=0, column=0, padx=10, pady=10)
add_button.grid(row=0, column=1, padx=5, pady=10)
delete_button.grid(row=0, column=2, padx=5, pady=10)
tasks_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

root.mainloop()
