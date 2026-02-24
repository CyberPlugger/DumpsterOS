import tkinter as tk
from tkinter import filedialog, messagebox
import os
import sys
import subprocess

# --- 1. НАСТРОЙКА ПУТЕЙ (ДЛЯ EXE) ---
# Определяем папку, где лежит программа (скрипт или EXE)
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Файл, где хранятся ярлыки
SAVE_FILE = os.path.join(BASE_DIR, "installed_apps.txt")


# --- 2. ЛОГИКА СИСТЕМЫ ---

def run_app(path):
    """Функция запуска приложений"""
    path = os.path.normpath(path)  # Исправляем слэши для Windows

    if not os.path.exists(path):
        return messagebox.showerror("Error", f"File not found:\n{path}")

    try:
        # Если это скрипт (.py или .dump), запускаем его через интерпретатор Python
        # Это предотвращает открытие файла в PyCharm/Блокноте
        if path.endswith((".py", ".dump")):
            # sys.executable - это путь к Python (или к твоему EXE)
            subprocess.Popen([sys.executable, path], shell=True)
        else:
            # Если это .exe или другой файл, запускаем стандартно через Windows
            os.startfile(path)
    except Exception as e:
        messagebox.showerror("System Error", f"Failed to launch:\n{str(e)}")


def add_to_desktop():
    """Выбор файла и добавление в базу данных"""
    path = filedialog.askopenfilename(
        title="Export App to Dumpster OS",
        filetypes=[("Dumpster Apps", "*.exe *.py *.dump"), ("All files", "*.*")]
    )
    if path:
        # Записываем путь в файл с новой строки (\n)
        with open(SAVE_FILE, "a", encoding="utf-8") as f:
            f.write(path + "\n")
        # Обновляем иконки на экране
        refresh_desktop()


def refresh_desktop():
    """Очистка и перерисовка иконок на рабочем столе"""
    # Удаляем все старые кнопки
    for widget in desktop_frame.winfo_children():
        widget.destroy()

    if not os.path.exists(SAVE_FILE):
        return

    # Читаем список путей из файла
    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        # strip() убирает пробелы и лишние переносы строк
        apps = [line.strip() for line in f if line.strip()]

    row, col = 0, 0
    for path in apps:
        app_name = os.path.basename(path)

        # Создаем кнопку.
        # Lambda p=path: важно для сохранения пути конкретной кнопки
        btn = tk.Button(
            desktop_frame,
            text=app_name,
            width=18,
            height=3,
            bg="#222",
            fg="lime",
            font=("Consolas", 10, "bold"),
            relief="raised",
            bd=2,
            activebackground="lime",
            command=lambda p=path: run_app(p)
        )

        btn.grid(row=row, column=col, padx=15, pady=15)

        # Сетка: 6 кнопок в ряд
        col += 1
        if col > 5:
            col = 0
            row += 1


def reset_os():
    """Удаление всех ярлыков"""
    if messagebox.askyesno("Reset", "Do you want to clear all apps from the desktop?"):
        if os.path.exists(SAVE_FILE):
            os.remove(SAVE_FILE)
        refresh_desktop()


# --- 3. ИНТЕРФЕЙС (GUI) ---

root = tk.Tk()
root.title("DUMPSTER OS")
root.attributes("-fullscreen", True)  # Полноэкранный режим
root.configure(bg="#0a0a0a")  # Черный фон

# Верхняя панель (Header)
header = tk.Frame(root, bg="#1a1a1a", pady=5)
header.pack(fill="x")

tk.Label(
    header,
    text="🗑️ DUMPSTER OS CORE",
    fg="lime",
    bg="#1a1a1a",
    font=("Consolas", 12, "bold")
).pack(side="left", padx=20)

# Кнопки управления в верхнем углу
tk.Button(header, text="EXIT", bg="#440000", fg="white", width=10, command=root.destroy, bd=0).pack(side="right",
                                                                                                    padx=10)
tk.Button(header, text="RESET", bg="#333", fg="white", width=10, command=reset_os, bd=0).pack(side="right", padx=10)
tk.Button(header, text="EXPORT", bg="#004400", fg="white", width=15, command=add_to_desktop, bd=0).pack(side="right",
                                                                                                        padx=10)

# Область рабочего стола (Desktop)
desktop_frame = tk.Frame(root, bg="#0a0a0a")
desktop_frame.pack(fill="both", expand=True, padx=30, pady=30)

# Загружаем ярлыки при старте программы
refresh_desktop()

root.mainloop()
