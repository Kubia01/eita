import tkinter as tk
from tkinter import ttk


# Centralized visual theme for the CRM application.
# This module intentionally does not change any business logic. It only
# defines styles, colors, and fonts and applies them globally to ttk widgets.


PALETTE = {
    # SAP Fiori-like palette
    "bg_app": "#f7f7f7",
    "bg_card": "#ffffff",
    "bg_header": "#0a6ed1",
    "text_primary": "#2c3f57",
    "text_secondary": "#6a7d95",
    "accent": "#0a6ed1",
    "success": "#107e3e",
    "danger": "#bb0000",
    "border": "#dde3ea",
    "focus": "#0854a0",
}


FONTS = {
    "base": ("Segoe UI", 10),
    "base_bold": ("Segoe UI", 10, "bold"),
    "title": ("Segoe UI", 18, "bold"),
    "subtitle": ("Segoe UI", 12, "bold"),
    "mono": ("Consolas", 10),
}


def apply_theme(root: tk.Misc) -> None:
    """Apply a modern, clean ttk theme and styles to the application.

    This function is safe to call once at startup. It does not modify
    application logic, only widget appearance.
    """
    try:
        # Use the built-in 'clam' theme as a base for consistent rendering
        style = ttk.Style(master=root)
        try:
            style.theme_use("clam")
        except Exception:
            # Fallback to any available theme
            for candidate in ("alt", "default", "classic"):
                try:
                    style.theme_use(candidate)
                    break
                except Exception:
                    continue

        root.configure(bg=PALETTE["bg_app"])  # background for tk containers

        # Global fonts (applies to ttk via style mappings below)
        root.option_add("*Font", FONTS["base"])

        # Base colors for common ttk widgets
        style.configure(
            "TLabel",
            background=PALETTE["bg_app"],
            foreground=PALETTE["text_primary"],
        )
        style.configure(
            "Card.TFrame",
            background=PALETTE["bg_card"],
            bordercolor=PALETTE["border"],
            relief="flat",
        )
        style.configure(
            "TFrame",
            background=PALETTE["bg_app"],
        )

        # Buttons
        style.configure(
            "Primary.TButton",
            background=PALETTE["accent"],
            foreground="#ffffff",
            bordercolor=PALETTE["accent"],
            focusthickness=1,
            focuscolor=PALETTE["focus"],
            padding=(14, 8),
        )
        style.map(
            "Primary.TButton",
            background=[("active", "#2563eb"), ("disabled", "#93c5fd")],
            foreground=[("disabled", "#e5e7eb")],
        )

        style.configure(
            "Success.TButton",
            background=PALETTE["success"],
            foreground="#ffffff",
            bordercolor=PALETTE["success"],
            padding=(14, 8),
        )
        style.map(
            "Success.TButton",
            background=[("active", "#059669"), ("disabled", "#6ee7b7")],
        )

        style.configure(
            "Danger.TButton",
            background=PALETTE["danger"],
            foreground="#ffffff",
            bordercolor=PALETTE["danger"],
            padding=(12, 6),
        )
        style.map(
            "Danger.TButton",
            background=[("active", "#dc2626")],
        )

        # Entries
        style.configure(
            "TEntry",
            fieldbackground="#ffffff",
            foreground=PALETTE["text_primary"],
            bordercolor=PALETTE["border"],
            lightcolor=PALETTE["focus"],
            darkcolor=PALETTE["border"],
            padding=(8, 6),
        )

        # Notebook (tabs)
        style.configure(
            "TNotebook",
            background=PALETTE["bg_app"],
            borderwidth=0,
        )
        style.configure(
            "TNotebook.Tab",
            font=FONTS["base"],
            padding=(16, 10),
        )
        style.map(
            "TNotebook.Tab",
            background=[("selected", "#e2e8f0")],
            foreground=[("selected", PALETTE["text_primary"])],
        )

        # Treeview
        style.configure(
            "Treeview",
            background="#ffffff",
            fieldbackground="#ffffff",
            foreground=PALETTE["text_primary"],
            bordercolor=PALETTE["border"],
            rowheight=28,
        )
        style.configure(
            "Treeview.Heading",
            font=FONTS["base_bold"],
        )

        # Header style (used by main window top bar)
        style.configure(
            "Header.TFrame",
            background=PALETTE["bg_header"],
        )
        style.configure(
            "Header.TLabel",
            background=PALETTE["bg_header"],
            foreground="#ffffff",
            font=FONTS["title"],
        )
        style.configure(
            "Subtle.TLabel",
            foreground=PALETTE["text_secondary"],
            background=PALETTE["bg_app"],
        )
    except Exception:
        # Fail-safe: never break the app if styling fails
        pass


def style_header_frame(frame: tk.Misc) -> None:
    try:
        frame.configure(bg=PALETTE["bg_header"])
    except Exception:
        pass


def card(frame: tk.Misc) -> None:
    try:
        frame.configure(bg=PALETTE["bg_card"])  # for tk.Frame usage
    except Exception:
        pass

