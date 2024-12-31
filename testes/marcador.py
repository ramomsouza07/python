import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
from datetime import datetime
import os

# Diretório do Banco de Dados
def get_db_path():
    user_data_dir = os.path.join(os.path.expanduser("~"), "RastreadorDeEstudo")
    os.makedirs(user_data_dir, exist_ok=True)
    return os.path.join(user_data_dir, "study_tracker.db")

DB_NAME = get_db_path()

def setup_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS study_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_name TEXT,
            start_time TEXT,
            end_time TEXT
        )
    ''')
    connection.commit()
    connection.close()

# Salvar sessão
def save_session(name, start, end):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO study_sessions (session_name, start_time, end_time)
        VALUES (?, ?, ?)
    ''', (name, start, end))
    connection.commit()
    connection.close()

# Recuperar sessões
def fetch_sessions():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute('SELECT session_name, start_time, end_time FROM study_sessions')
    sessions = cursor.fetchall()
    connection.close()
    return sessions

# Interface Gráfica
def main():
    setup_database()
    
    def handle_button_click():
        nonlocal tracking, start_time, session_name

        if not tracking:
            session_name = simpledialog.askstring("Nome da Sessão", "Digite o nome da sessão:")
            if not session_name:
                messagebox.showwarning("Nome da Sessão", "Você precisa fornecer um nome para a sessão.")
                return

            start_time = datetime.now()
            tracking = True
            button.config(text="Parar")
            label_status.config(text=f"Sessão '{session_name}' iniciada em: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            end_time = datetime.now()
            tracking = False
            button.config(text="Iniciar")
            label_status.config(text=f"Sessão '{session_name}' finalizada em: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

            # Salvar dados
            save_session(session_name, start_time.strftime('%Y-%m-%d %H:%M:%S'), end_time.strftime('%Y-%m-%d %H:%M:%S'))
            messagebox.showinfo("Sessão Salva", f"Sessão '{session_name}' registrada com sucesso!")

    def show_sessions():
        sessions = fetch_sessions()
        if sessions:
            session_list = "\n".join([f"Sessão: {s[0]} | Início: {s[1]} | Término: {s[2]}" for s in sessions])
            messagebox.showinfo("Histórico de Sessões", session_list)
        else:
            messagebox.showinfo("Histórico de Sessões", "Nenhuma sessão registrada ainda.")

    # Variáveis
    tracking = False
    start_time = None
    session_name = None

    # Interface
    root = tk.Tk()
    root.title("Batedor de Ponto 1.0")
    root.geometry("400x300")
    root.configure(bg="#f0f8ff")

    frame = tk.Frame(root, bg="#f0f8ff")
    frame.pack(pady=20, padx=20)

    label_title = tk.Label(frame, text="Batedor de Ponto 1.0", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#4682b4")
    label_title.pack(pady=10)

    label_status = tk.Label(frame, text="Pressione 'Iniciar' para começar.", font=("Helvetica", 12), bg="#f0f8ff", fg="#696969")
    label_status.pack(pady=10)

    button = tk.Button(frame, text="Iniciar", font=("Helvetica", 12, "bold"), bg="#87cefa", fg="white", command=handle_button_click)
    button.pack(pady=5)

    button_history = tk.Button(frame, text="Ver Histórico", font=("Helvetica", 12, "bold"), bg="#87cefa", fg="white", command=show_sessions)
    button_history.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
