# This is To do list (Python)
# This is a new feature (feature 1)
import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List App")

        # Create and initialize the task list
        self.tasks = []

        # GUI elements
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=10, pady=10)

        self.view_button = tk.Button(root, text="View Tasks", command=self.view_tasks)
        self.view_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.task_listbox.insert(tk.END, f"{len(self.tasks)}. {task_text}")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task again.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def view_tasks(self):
        if self.tasks:
            task_text = "\n".join(self.tasks)
            messagebox.showinfo("Task List", task_text)
        else:
            messagebox.showinfo("Task List", "No tasks to display.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{i}. {task}")

def main():
    root = tk.Tk()
    root.geometry('400x300+600+200')
    root.resizable(False, False)

    app = TodoListApp(root)

    root.mainloop()



if __name__ == "__main__":
    main()
