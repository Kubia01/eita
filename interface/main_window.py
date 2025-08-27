import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from database import DB_NAME
from utils.theme import apply_theme, style_header_frame, PALETTE, FONTS

class MainWindow:
    def __init__(self, root, user_id, role, nome_completo):
        self.root = root
        self.user_id = user_id
        self.role = role
        self.nome_completo = nome_completo
        
        # Sistema de eventos para comunicação entre módulos
        self.event_listeners = []
        
        self.setup_main_window()
        self.create_main_ui()
        
        # Mostrar janela principal
        self.root.deiconify()
        
    def setup_main_window(self):
        """Configurar janela principal"""
        self.root.title(f"Sistema CRM Compressores - {self.nome_completo} ({self.role})")
        self.root.geometry("1400x800")
        try:
            apply_theme(self.root)
        except Exception:
            pass
        self.root.configure(bg=PALETTE["bg_app"]) 
        
        # Centralizar janela
        self.center_window()
        
    def center_window(self):
        """Centralizar a janela na tela"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def has_role(self, role_name: str) -> bool:
        """Verifica se o usuário possui o perfil informado (suporta múltiplos perfis separados por vírgula)."""
        try:
            roles = [r.strip().lower() for r in (self.role or '').split(',') if r.strip()]
            return role_name.lower() in roles
        except Exception:
            return self.role == role_name
        
    def register_listener(self, listener_func):
        """Registrar um listener para eventos do sistema"""
        self.event_listeners.append(listener_func)
        
    def emit_event(self, event_type, data=None):
        """Emitir um evento para todos os listeners"""
        for listener in self.event_listeners:
            try:
                listener(event_type, data)
            except Exception as e:
                print(f"Erro ao processar evento {event_type}: {e}")
        
    def create_main_ui(self):
        # Frame superior com menu
        self.create_header()
        
        # Notebook para abas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        # Criar módulos
        self._load_user_permissions()
        self.create_modules()
        
    def create_header(self):
        """Criar cabeçalho com informações do usuário e botões"""
        header_frame = tk.Frame(self.root, bg=PALETTE["bg_header"], height=60)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)
        
        # Frame esquerdo - título
        left_frame = tk.Frame(header_frame, bg=PALETTE["bg_header"]) 
        left_frame.pack(side="left", fill="y", padx=20, pady=10)
        
        title_label = tk.Label(left_frame, 
                              text="Sistema CRM Compressores",
                              font=FONTS["title"],
                              bg=PALETTE["bg_header"],
                              fg='white')
        title_label.pack(anchor="w")
        
        # Frame direito - informações do usuário e logout
        right_frame = tk.Frame(header_frame, bg=PALETTE["bg_header"]) 
        right_frame.pack(side="right", fill="y", padx=20, pady=10)
        
        user_label = tk.Label(right_frame,
                             text=f"Usuário: {self.nome_completo} ({self.role})",
                             font=FONTS["base"],
                             bg=PALETTE["bg_header"],
                             fg='#e2e8f0')
        user_label.pack(anchor="e")
        
        logout_btn = ttk.Button(right_frame,
                              text="Logout",
                              style='Danger.TButton',
                              command=self.logout)
        logout_btn.pack(anchor="e", pady=(5, 0))
        
    def create_modules(self):
        """Criar todos os módulos do sistema com importação isolada e tolerante a falhas"""
        def add_module(tab_text, module_path, class_name):
            frame = tk.Frame(self.notebook)
            self.notebook.add(frame, text=tab_text)
            try:
                mod = __import__(module_path, fromlist=[class_name])
                cls = getattr(mod, class_name)
                instance = cls(frame, self.user_id, self.role, self)
                # Se módulo estiver como somente leitura, tentar aplicar
                module_key = self._tab_text_to_key(tab_text)
                if not self.can_edit(module_key) and hasattr(instance, 'set_read_only'):
                    try:
                        instance.set_read_only(True)
                    except Exception:
                        pass
                return instance
            except Exception as e:
                messagebox.showerror("Erro ao carregar módulo", f"Falha ao carregar {tab_text}:\n\n{e}")
                return None

        # Dashboard
        if self.has_access('dashboard'):
            self.dashboard_module = add_module("📊 Dashboard", "interface.modules.dashboard", "DashboardModule")
        # Clientes
        if self.has_access('clientes'):
            self.clientes_module = add_module("👥 Clientes", "interface.modules.clientes", "ClientesModule")
        # Produtos
        if self.has_access('produtos'):
            self.produtos_module = add_module("📦 Produtos", "interface.modules.produtos", "ProdutosModule")
        # Compras (Cotações de compra)
        if self.has_access('cotacoes'):
            self.cotacoes_module = add_module("💰 Compras", "interface.modules.cotacoes", "CotacoesModule")
        # Locações (aba separada - módulo independente)
        if self.has_access('relatorios') or self.has_access('cotacoes'):
            # manter lógica de locações na permissão de cotações/relatórios se necessário, ou crie chave própria
            if self.has_access('relatorios') or self.has_access('cotacoes'):
                self.locacoes_module = add_module("📄 Locações", "interface.modules.locacoes_full", "LocacoesModule")
        # Relatórios
        if self.has_access('relatorios'):
            self.relatorios_module = add_module("📋 Relatórios", "interface.modules.relatorios", "RelatoriosModule")
        # Usuários e Permissões
        if self.has_access('usuarios'):
            self.usuarios_module = add_module("👤 Usuários", "interface.modules.usuarios", "UsuariosModule")
        if self.has_access('permissoes'):
            self.permissoes_module = add_module("🔐 Permissões", "interface.modules.permissoes", "PermissoesModule")

    def _tab_text_to_key(self, tab_text: str) -> str:
        mapping = {
            '📊 Dashboard': 'dashboard',
            '👥 Clientes': 'clientes',
            '📦 Produtos': 'produtos',
            '💰 Compras': 'cotacoes',
            '📄 Locações': 'relatorios',
            '📋 Relatórios': 'relatorios',
            '👤 Usuários': 'usuarios',
            '🔐 Permissões': 'permissoes',
        }
        return mapping.get(tab_text, '')

    def _load_user_permissions(self):
        """Carrega as permissões do usuário corrente em self.user_permissions"""
        self.user_permissions = {}
        try:
            conn = sqlite3.connect(DB_NAME)
            c = conn.cursor()
            c.execute("SELECT modulo, nivel_acesso FROM permissoes_usuarios WHERE usuario_id = ?", (self.user_id,))
            self.user_permissions = dict(c.fetchall())
        except Exception as e:
            print(f"Aviso: falha ao carregar permissões: {e}")
            self.user_permissions = {}
        finally:
            try:
                conn.close()
            except Exception:
                pass

    def has_access(self, module_key: str) -> bool:
        """Retorna True se o usuário pode ver o módulo (ou se for admin)."""
        if self.has_role('admin'):
            return True
        level = (self.user_permissions or {}).get(module_key, 'sem_acesso')
        return level in ('consulta', 'controle_total')

    def can_edit(self, module_key: str) -> bool:
        """Retorna True se o usuário pode editar o módulo (ou se for admin)."""
        if self.has_role('admin'):
            return True
        level = (self.user_permissions or {}).get(module_key, 'sem_acesso')
        return level == 'controle_total'
        
    def logout(self):
        """Fazer logout e voltar para tela de login"""
        if messagebox.askyesno("Logout", "Tem certeza que deseja sair?"):
            self.root.withdraw()
            
            # Criar nova janela de login
            from interface.login import LoginWindow
            LoginWindow(self.root)