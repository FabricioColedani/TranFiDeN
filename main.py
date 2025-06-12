# main.py

import tkinter as tk
from tkinter import ttk, messagebox
from logica import conversion_rates, convertir_moneda  # Importamos backend

# ===== Interfaz =====
root = tk.Tk()
root.title("💱 Conversor Moderno de Moneda")
root.geometry("480x420")
root.configure(bg="#1e1e2f")

# Estilo general
fuente = ("Segoe UI", 12)
fuente_titulo = ("Segoe UI", 18, "bold")
estilo_label = {"font": fuente, "bg": "#2d2d44", "fg": "#f0f0f0"}

# Card visual
card = tk.Frame(root, bg="#2d2d44", bd=0, relief="flat")
card.place(relx=0.5, rely=0.5, anchor="center", width=400, height=350)

tk.Label(card, text="💸 Conversor de Moneda", font=fuente_titulo, bg="#2d2d44", fg="#ffffff").pack(pady=(20, 10))

# Monto
tk.Label(card, text="Monto a convertir:", **estilo_label).pack()
entry_monto = tk.Entry(card, font=fuente, justify="center", bg="#383857", fg="white", bd=0,
                       insertbackground="white", relief="flat")
entry_monto.pack(pady=8, ipady=5, ipadx=20)

# Moneda
tk.Label(card, text="Seleccionar moneda:", **estilo_label).pack()
combo_moneda = ttk.Combobox(card, values=list(conversion_rates.keys()), font=fuente, state="readonly")
combo_moneda.set("🇺🇸 Dólar Estadounidense")
combo_moneda.pack(pady=8)

# Resultado
label_resultado = tk.Label(card, text="", font=("Segoe UI", 14, "bold"), bg="#2d2d44", fg="#00B894")
label_resultado.pack(pady=(10, 0))

# Función de conversión conectada al botón
def ejecutar_conversion():
    texto, color = convertir_moneda(entry_monto.get(), combo_moneda.get())
    label_resultado.config(text=texto, fg=color)

# Botón
boton_convertir = tk.Button(card, text="Convertir", font=("Segoe UI", 12, "bold"),
                            bg="#00cec9", fg="white", activebackground="#00b894",
                            relief="flat", command=ejecutar_conversion)
boton_convertir.pack(pady=12, ipadx=10, ipady=5)

# Estilo del Combobox
style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox",
    fieldbackground="#383857",
    background="#383857",
    foreground="white",
    arrowcolor="white",
    selectbackground="#2d2d44",
    selectforeground="white",
    bordercolor="#383857",
    lightcolor="#383857",
    darkcolor="#383857",
    borderwidth=0
)

root.mainloop()
