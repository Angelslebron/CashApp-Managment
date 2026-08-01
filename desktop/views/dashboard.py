import tkinter as tk

from tkinter import ttk
from tkinter import messagebox

import requests

from desktop.controllers.movement_controller import MovementController

class Dashboard:

    def __init__(self, root):
        self.root = root
        self.root.title("CashApp Management")
        self.root.geometry("900x600")

        self.controller = MovementController()

        self.summary_frame = ttk.LabelFrame(
            self.root,
            text="Financial Summary"
        )

        self.summary_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.create_widgets()
        self.load_movements()

    def create_widgets(self):

        form_frame = ttk.LabelFrame(
            self.root,
            text="Movement"
        )

        form_frame.pack(
            padx=20,
            pady=20,
            fill="x"
        )

        ttk.Label(
            form_frame,
            text="Description"
        ).grid(row=0, column=0, padx=5, pady=5)

        self.description_entry = ttk.Entry(
            form_frame,
            width=30
        )

        self.description_entry.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            form_frame,
            text="Amount"
        ).grid(row=0, column=2, padx=5, pady=5)

        self.amount_entry = ttk.Entry(
            form_frame,
            width=20
        )

        self.amount_entry.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

        self.description_entry.bind(
            "<FocusOut>",
            self.auto_predict_category
        )

        ttk.Label(
            form_frame,
            text="Category"
        ).grid(row=1, column=0, padx=5, pady=5)

        self.category_entry = ttk.Entry(
            form_frame,
            width=30
        )

        self.category_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            form_frame,
            text="Type"
        ).grid(row=1, column=2, padx=5, pady=5)

        self.type_combo = ttk.Combobox(
            form_frame,
            values=["INCOME", "EXPENSE"],
            state="readonly"
        )

        self.type_combo.grid(
            row=1,
            column=3,
            padx=5,
            pady=5
        )

        self.type_combo.set("INCOME")

        ttk.Button(
            form_frame,
            text="Add",
            command=self.add_movement
        ).grid(row=2, column=0, padx=5, pady=10)

        ttk.Button(
            form_frame,
            text="Update",
            command=self.update_movement
        ).grid(row=2, column=1, padx=5, pady=10)

        ttk.Button(
            form_frame,
            text="Delete",
            command=self.delete_movement
        ).grid(row=2, column=2, padx=5, pady=10)

        ttk.Button(
            form_frame,
            text="Clear",
            command=self.clear_form
        ).grid(row=2, column=3, padx=5, pady=10)

        self.table = ttk.Treeview(
            self.root,
            columns=(
                "id",
                "description",
                "amount",
                "category",
                "type",
                "created_at"
            ),
            show="headings"
        )

        self.table.heading("id", text="ID")
        self.table.heading("description", text="Description")
        self.table.heading("amount", text="Amount")
        self.table.heading("category", text="Category")
        self.table.heading("type", text="Type")
        self.table.heading("created_at", text="Created")

        self.table.pack(
            padx=20,
            pady=10,
            fill="both",
            expand=True
        )

        self.table.bind(
            "<<TreeviewSelect>>",
            self.select_movement
        )

    def load_movements(self):

        try:
            movements = self.controller.get_movements()

            for item in self.table.get_children():
                self.table.delete(item)

            for movement in movements:
                self.table.insert(
                    "",
                    "end",
                    values=(
                        movement["id"],
                        movement["description"],
                        movement["amount"],
                        movement["category"],
                        movement["movement_type"],
                        movement["created_at"]
                    )
                )

        except requests.RequestException:
            messagebox.showerror(
                "Error",
                "Could not connect to the API."
            )

    def add_movement(self):

        try:
            description = self.description_entry.get()
            amount = float(self.amount_entry.get())
            category = self.category_entry.get()
            movement_type = self.type_combo.get()

            self.controller.create_movement(
                description,
                amount,
                category,
                movement_type
            )

            self.clear_form()
            self.load_movements()

            messagebox.showinfo(
                "Success",
                "Movement created successfully."
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Amount must be a number."
            )

        except requests.RequestException:
            messagebox.showerror(
                "Error",
                "Could not create the movement."
            )

    def select_movement(self, event):

        selected = self.table.selection()

        if not selected:
            return

        values = self.table.item(
            selected[0],
            "values"
        )

        self.description_entry.delete(0, tk.END)
        self.description_entry.insert(0, values[1])

        self.amount_entry.delete(0, tk.END)
        self.amount_entry.insert(0, values[2])

        self.category_entry.delete(0, tk.END)
        self.category_entry.insert(0, values[3])

        self.type_combo.set(values[4])

    def update_movement(self):

        selected = self.table.selection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Select a movement first."
            )
            return

        values = self.table.item(
            selected[0],
            "values"
        )

        movement_id = values[0]

        try:
            self.controller.update_movement(
                movement_id,
                self.description_entry.get(),
                float(self.amount_entry.get()),
                self.category_entry.get(),
                self.type_combo.get()
            )

            self.clear_form()
            self.load_movements()

            messagebox.showinfo(
                "Success",
                "Movement updated successfully."
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Amount must be a number."
            )

        except requests.RequestException:
            messagebox.showerror(
                "Error",
                "Could not update the movement."
            )

    def delete_movement(self):

        selected = self.table.selection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Select a movement first."
            )
            return

        values = self.table.item(
            selected[0],
            "values"
        )

        movement_id = values[0]

        confirm = messagebox.askyesno(
            "Confirm",
            "Are you sure you want to delete this movement?"
        )

        if not confirm:
            return

        try:
            self.controller.delete_movement(
                movement_id
            )

            self.clear_form()
            self.load_movements()

            messagebox.showinfo(
                "Success",
                "Movement deleted successfully."
            )

        except requests.RequestException:
            messagebox.showerror(
                "Error",
                "Could not delete the movement."
            )

    def clear_form(self):

        self.description_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)

        self.type_combo.set("INCOME")

    def auto_predict_category(self, event):

        description = self.description_entry.get().strip()

        if description == "":
            return

        try:

            category = self.controller.predict_category(
                description
            )

            self.category_entry.delete(
                0,
                tk.END
            )

            self.category_entry.insert(
                0,
                category
            )

        except Exception:
            pass