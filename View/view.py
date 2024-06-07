import customtkinter as ctk
from tkinter import messagebox

class InventoryView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.title("STOCK SEC - Gerenciador de Estoque")
        self.geometry("800x600")

        self.create_home_screen()

    def create_home_screen(self):
        self.clear_screen()

        self.title_label = ctk.CTkLabel(self, text="STOCK SEC", font=("Arial", 24))
        self.title_label.pack(pady=20)

        self.add_product_button = ctk.CTkButton(self, text="Cadastro de Produtos", command=self.create_add_product_screen)
        self.add_product_button.pack(pady=10)

        self.manage_inventory_button = ctk.CTkButton(self, text="Gestão do Estoque", command=self.create_manage_inventory_screen)
        self.manage_inventory_button.pack(pady=10)

    def create_add_product_screen(self):
        self.clear_screen()

        self.name_label = ctk.CTkLabel(self, text="Nome do Produto:")
        self.name_label.pack(pady=5)
        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.pack(pady=5)

        self.quantity_label = ctk.CTkLabel(self, text="Quantidade:")
        self.quantity_label.pack(pady=5)
        self.quantity_entry = ctk.CTkEntry(self, validate="key", validatecommand=(self.register(self.validate_quantity), "%P"))
        self.quantity_entry.pack(pady=5)

        self.sector_label = ctk.CTkLabel(self, text="Setor:")
        self.sector_label.pack(pady=5)

        self.sector_var = ctk.StringVar(value="Informatica")
        self.sector_options = ["Informatica", "Papelaria", "Ferramentas", "Outros"]
        self.sector_menu = ctk.CTkOptionMenu(self, values=self.sector_options, variable=self.sector_var)
        self.sector_menu.pack(pady=5)

        self.add_button = ctk.CTkButton(self, text="Adicionar Produto", command=self.add_product)
        self.add_button.pack(pady=10)

        self.back_button = ctk.CTkButton(self, text="Voltar", command=self.create_home_screen)
        self.back_button.pack(pady=10)

    def validate_quantity(self, new_value):
        if new_value.isdigit() or new_value == "":
            return True
        return False

    def create_manage_inventory_screen(self):
        self.clear_screen()

        self.products_frame = ctk.CTkFrame(self)
        self.products_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.create_product_list()

        self.action_frame = ctk.CTkFrame(self)
        self.action_frame.pack(pady=10)

        self.remove_button = ctk.CTkButton(self.action_frame, text="Retirar Produto", command=self.show_remove_product_window)
        self.remove_button.pack(side="left", padx=10)

        self.delete_button = ctk.CTkButton(self.action_frame, text="Excluir Produto", command=self.show_delete_product_window)
        self.delete_button.pack(side="right", padx=10)

        self.back_button = ctk.CTkButton(self, text="Voltar", command=self.create_home_screen)
        self.back_button.pack(pady=10)


    def create_product_list(self):
        products = self.controller.get_all_products()
        self.products_table = ctk.CTkScrollableFrame(self.products_frame)
        self.products_table.pack(fill="both", expand=True, padx=10, pady=10)

        headers = ["ID", "Nome", "Quantidade", "Setor"]
        for i, header in enumerate(headers):
            header_label = ctk.CTkLabel(self.products_table, text=header, font=("Arial", 14, "bold"))
            header_label.grid(row=0, column=i, padx=5, pady=5)

        for row_num, product in enumerate(products, start=1):
            for col_num, detail in enumerate(product):
                detail_label = ctk.CTkLabel(self.products_table, text=detail, font=("Arial", 12))
                detail_label.grid(row=row_num, column=col_num, padx=5, pady=5)
                if col_num == 0:  # ID column
                    detail_label.bind("<Button-1>", lambda e, text=detail: self.copy_to_clipboard(text))

    def copy_to_clipboard(self, text):
        self.clipboard_clear()
        self.clipboard_append(text)
        messagebox.showinfo("ID Copiado", f"ID {text} copiado para a área de transferência!")

    def show_remove_product_window(self):
        self.remove_window = ctk.CTkToplevel(self)
        self.remove_window.title("Retirar Produto")
        self.remove_window.geometry("400x200")

        self.remove_id_name_label = ctk.CTkLabel(self.remove_window, text="ID ou Nome do Produto:")
        self.remove_id_name_label.pack(pady=5)
        self.remove_id_name_entry = ctk.CTkEntry(self.remove_window)
        self.remove_id_name_entry.pack(pady=5)

        self.remove_quantity_label = ctk.CTkLabel(self.remove_window, text="Quantidade a Retirar:")
        self.remove_quantity_label.pack(pady=5)
        self.remove_quantity_entry = ctk.CTkEntry(self.remove_window)
        self.remove_quantity_entry.pack(pady=5)

        self.remove_confirm_button = ctk.CTkButton(self.remove_window, text="Confirmar", command=self.remove_product)
        self.remove_confirm_button.pack(pady=10)

    def show_delete_product_window(self):
        self.delete_window = ctk.CTkToplevel(self)
        self.delete_window.title("Excluir Produto")
        self.delete_window.geometry("400x150")

        self.delete_id_name_label = ctk.CTkLabel(self.delete_window, text="ID ou Nome do Produto:")
        self.delete_id_name_label.pack(pady=5)
        self.delete_id_name_entry = ctk.CTkEntry(self.delete_window)
        self.delete_id_name_entry.pack(pady=5)

        self.delete_confirm_button = ctk.CTkButton(self.delete_window, text="Confirmar", command=self.delete_product)
        self.delete_confirm_button.pack(pady=10)

    def add_product(self):
        name = self.name_entry.get().strip()
        quantity = self.quantity_entry.get().strip()
        sector = self.sector_var.get()

        if not name:
            messagebox.showerror("Erro", "Por favor, preencha o nome do produto.")
            return

        if not quantity.isdigit():
            messagebox.showerror("Erro", "Por favor, insira uma quantidade válida.")
            return

        quantity = int(quantity)

        self.controller.add_product(name, quantity, sector)
        self.create_manage_inventory_screen()

    def remove_product(self):
        id_or_name = self.remove_id_name_entry.get().strip()
        quantity = self.remove_quantity_entry.get().strip()

        if not id_or_name:
            messagebox.showerror("Erro", "Por favor, preencha o ID ou Nome do produto.")
            return

        if not quantity.isdigit():
            messagebox.showerror("Erro", "Por favor, insira uma quantidade válida.")
            return

        quantity = int(quantity)

        if id_or_name.isdigit():
            self.controller.subtract_product_quantity_by_id(int(id_or_name), quantity)
        else:
            self.controller.subtract_product_quantity(id_or_name, quantity)

        self.remove_window.destroy()
        self.create_manage_inventory_screen()

    def delete_product(self):
        id_or_name = self.delete_id_name_entry.get().strip()

        if not id_or_name:
            messagebox.showerror("Erro", "Por favor, preencha o ID ou Nome do produto.")
            return

        if id_or_name.isdigit():
            self.controller.delete_product_by_id(int(id_or_name))
        else:
            self.controller.delete_product(id_or_name)

        self.delete_window.destroy()
        self.create_manage_inventory_screen()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
            