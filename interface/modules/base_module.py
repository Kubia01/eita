import tkinter as tk
from tkinter import ttk
from utils.theme import PALETTE, FONTS

class BaseModule:
    """Classe base para todos os módulos do sistema"""
    
    def __init__(self, parent, user_id, role, main_window):
        self.parent = parent
        self.user_id = user_id
        self.role = role
        self.main_window = main_window
        
        # Registrar para receber eventos
        if hasattr(main_window, 'register_listener'):
            main_window.register_listener(self.handle_event)
        
        # Frame principal do módulo (container visual)
        self.frame = tk.Frame(parent, bg=PALETTE["bg_app"])
        self.frame.pack(fill="both", expand=True)
        
        # Configurar UI específica do módulo
        self.setup_ui()
        
    def setup_ui(self):
        """Método a ser implementado pelos módulos filhos"""
        pass
        
    def handle_event(self, event_type, data=None):
        """Manipular eventos recebidos do sistema"""
        pass
        
    def emit_event(self, event_type, data=None):
        """Emitir evento para outros módulos"""
        if hasattr(self.main_window, 'emit_event'):
            self.main_window.emit_event(event_type, data)
    
    def has_role(self, role_name: str) -> bool:
        """Verifica se o usuário possui o perfil informado (suporta múltiplos perfis separados por vírgula)."""
        try:
            roles = [r.strip().lower() for r in (self.role or '').split(',') if r.strip()]
            return role_name.lower() in roles
        except Exception:
            return self.role == role_name
    
    def create_section_frame(self, parent, title, padx=10, pady=10):
        """Criar frame de seção com título (visual moderno)"""
        outer = tk.Frame(parent, bg=PALETTE["bg_app"])  # spacing wrapper
        outer.pack_propagate(False)
        card = tk.Frame(outer, bg='#ffffff', highlightthickness=1, highlightbackground=PALETTE["border"])
        card.pack(fill="both", expand=True)
        header = tk.Label(card, text=title, font=FONTS["subtitle"], bg='#ffffff', fg=PALETTE["text_primary"])
        header.pack(anchor="w", padx=12, pady=(12, 6))
        body = tk.Frame(card, bg='#ffffff')
        body.pack(fill="both", expand=True, padx=12, pady=(0, 12))
        # Return the body so callers add content as antes
        body._outer_container = outer  # allow caller to pack/place the whole block if needed
        return body
    
    def create_button(self, parent, text, command, variant='primary', **kwargs):
        """Criar botão estilizado (mantém assinatura compatível por kwargs)."""
        style = {
            'primary': 'Primary.TButton',
            'success': 'Success.TButton',
            'danger': 'Danger.TButton',
        }.get(variant, 'Primary.TButton')
        button = ttk.Button(parent, text=text, command=command, style=style, **kwargs)
        return button
    
    def create_search_frame(self, parent, placeholder="Buscar...", command=None):
        """Criar frame de busca padronizado"""
        search_frame = tk.Frame(parent, bg='#ffffff', highlightthickness=1, highlightbackground=PALETTE["border"]) 
        
        search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=search_var)
        search_entry.pack(side="left", fill="x", expand=True, ipady=5, padx=(8, 0), pady=6)
        search_entry.insert(0, placeholder)

        def _on_focus_in(_e):
            if search_entry.get() == placeholder:
                search_entry.delete(0, 'end')
        def _on_focus_out(_e):
            if not search_entry.get().strip():
                search_entry.insert(0, placeholder)
        search_entry.bind('<FocusIn>', _on_focus_in)
        search_entry.bind('<FocusOut>', _on_focus_out)
        
        if command:
            search_btn = self.create_button(search_frame, "Buscar", command, variant='primary')
            search_btn.pack(side="right", padx=8, pady=6)
            search_entry.bind('<Return>', lambda e: command())
        
        return search_frame, search_var
    
    def show_success(self, message):
        """Mostrar mensagem de sucesso"""
        from tkinter import messagebox
        messagebox.showinfo("Sucesso", message)
        
    def show_error(self, message):
        """Mostrar mensagem de erro"""
        from tkinter import messagebox
        messagebox.showerror("Erro", message)
        
    def show_warning(self, message):
        """Mostrar mensagem de aviso"""
        from tkinter import messagebox
        messagebox.showwarning("Aviso", message)
        
    def show_info(self, title, message):
        """Mostrar mensagem informativa"""
        from tkinter import messagebox
        messagebox.showinfo(title, message)