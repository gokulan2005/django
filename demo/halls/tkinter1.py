import tkinter as tk
from tkinter import messagebox

class AbsenteesApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Absentees")

        self.current_attendance_exam_id = "your_initial_exam_id"  # Replace with appropriate initial value

        # Components
        self.add_absentees_button = tk.Button(self.master, text="Add Absentees", command=self.add_absentee)
        self.remove_button = tk.Button(self.master, text="Remove", command=self.remove_absentee)

        self.absentee_details_frame = tk.Frame(self.master, bd=5, relief=tk.GROOVE)
        self.reg_no_label = tk.Label(self.absentee_details_frame, text="Reg No.")
        self.name_label = tk.Label(self.absentee_details_frame, text="Name")
        self.reg_no_entry = tk.Entry(self.absentee_details_frame, state=tk.DISABLED)
        self.name_entry = tk.Entry(self.absentee_details_frame, state=tk.DISABLED)

        self.absentees_list_frame = tk.Frame(self.master, bd=5, relief=tk.GROOVE)
        self.absentees_list_label = tk.Label(self.absentees_list_frame, text="Absentees List")
        self.absentees_listbox = tk.Listbox(self.absentees_list_frame, selectmode=tk.SINGLE)
        self.absentees_listbox.bind("<ButtonRelease-1>", self.absentee_list_click)

        self.search_entry = tk.Entry(self.master, bd=5, relief=tk.GROOVE)
        self.search_entry.bind("<Return>", self.search)

        # Layout
        self.add_absentees_button.pack(pady=5)
        self.absentees_list_frame.pack(side=tk.LEFT, padx=10)
        self.search_entry.pack(side=tk.BOTTOM, pady=5)
        self.absentee_details_frame.pack(side=tk.RIGHT, padx=10)
        self.remove_button.pack(side=tk.BOTTOM)

        self.absentees_list_label.pack()
        self.absentees_listbox.pack()

        self.reg_no_label.grid(row=0, column=0, sticky=tk.E)
        self.name_label.grid(row=1, column=0, sticky=tk.E)
        self.reg_no_entry.grid(row=0, column=1, padx=5, pady=5)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        # Initial load
        self.load_data_to_fields()

    def add_absentee(self):
        # TODO: Implement the functionality to add absentee
        pass

    def remove_absentee(self):
        absentee_id = self.absentee_id  # Get the selected absentee ID
        if absentee_id:
            confirmation = messagebox.askokcancel("Absentee Delete", "Delete This Absentee?")
            if confirmation:
                # TODO: Implement the functionality to remove absentee
                self.load_data_to_fields()  # Reload data after removal
        else:
            messagebox.showinfo("Select a Absentee", "Select a Absentee !!!")

    def absentee_list_click(self, event):
        selected_index = self.absentees_listbox.curselection()
        if selected_index:
            student_reg_no = self.absentees_listbox.get(selected_index)
            # TODO: Implement the functionality to populate reg_no_entry and name_entry based on student_reg_no

    def search(self, event):
        search_text = self.search_entry.get()
        # TODO: Implement the functionality to search for absentees based on search_text
        self.load_data_to_fields()

    def load_data_to_fields(self):
        # TODO: Implement the functionality to load data into the absentees listbox based on current_attendance_exam_id
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = AbsenteesApp(root)
    root.geometry("600x400")
    root.mainloop()
