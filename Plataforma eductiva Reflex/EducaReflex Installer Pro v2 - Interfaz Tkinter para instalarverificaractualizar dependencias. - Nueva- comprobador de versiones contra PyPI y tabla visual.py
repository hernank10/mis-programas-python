#!/usr/bin/env python3
"""
EducaReflex Installer Pro v2
- Interfaz Tkinter para instalar/verificar/actualizar dependencias.
- Nueva: comprobador de versiones contra PyPI y tabla visual.
"""
import os
import sys
import subprocess
import platform
import json
import threading
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# Try imports for version detection and HTTP requests
try:
    # Python 3.8+
    from importlib.metadata import version as get_version, PackageNotFoundError
except Exception:
    try:
        # importlib-metadata backport
        from importlib_metadata import version as get_version, PackageNotFoundError
    except Exception:
        get_version = None
        PackageNotFoundError = Exception

try:
    import requests
except Exception:
    requests = None

# ---------------------------
# Configuration
# ---------------------------
DEPENDENCIAS = [
    "django", "fastapi", "uvicorn", "reflex",
    "psycopg2-binary", "reportlab", "pdfkit",
    "pandas", "openpyxl", "python-docx", "python-pptx",
    "odfpy", "pypandoc", "requests", "flask-socketio",
    "websockets", "aiohttp", "PyJWT", "python-dotenv"
]

LOG_FILE = "edu_installer_log.json"

# ---------------------------
# Utilities
# ---------------------------
def ejecutar_comando(comando):
    """Ejecuta comando shell y devuelve (stdout or stderr)."""
    try:
        resultado = subprocess.run(
            comando, shell=True, check=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        return resultado.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr or str(e)

def guardar_log(accion, detalle):
    log = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "accion": accion,
        "detalle": detalle
    }
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            try:
                logs = json.load(f)
            except Exception:
                logs = []
    logs.append(log)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)

def detectar_sistema():
    so = platform.system().lower()
    if "darwin" in so:
        return "macOS"
    elif "windows" in so:
        return "Windows"
    elif "linux" in so:
        if "android" in platform.platform().lower():
            return "Termux/Android"
        return "Linux"
    else:
        return "Desconocido"

def get_installed_version(package_name):
    if not get_version:
        return None
    try:
        return get_version(package_name)
    except PackageNotFoundError:
        return None
    except Exception:
        # Some pip names differ from import names; try fallback by replacing - with _
        try:
            return get_version(package_name.replace('-', '_'))
        except Exception:
            return None

def get_pypi_latest(package_name, timeout=10):
    """
    Consulta la API JSON de PyPI para obtener la última versión.
    Retorna None si falla (no hay conexión o paquete no existe).
    """
    if requests is None:
        return None
    url = f"https://pypi.org/pypi/{package_name}/json"
    try:
        r = requests.get(url, timeout=timeout)
        if r.status_code == 200:
            data = r.json()
            return data.get("info", {}).get("version")
        else:
            # Try common normalization: replace '_' with '-'
            if '_' in package_name:
                r = requests.get(f"https://pypi.org/pypi/{package_name.replace('_','-')}/json", timeout=timeout)
                if r.status_code == 200:
                    return r.json().get("info", {}).get("version")
    except Exception:
        return None
    return None

# ---------------------------
# GUI App
# ---------------------------
class EducaInstallerProV2:
    def __init__(self, root):
        self.root = root
        root.title("🧠 EducaReflex Installer Pro v2")
        root.geometry("980x650")
        # Header
        ttk.Label(root, text="EducaReflex Installer Pro v2 — Dependency Manager", font=("Segoe UI", 14, "bold")).pack(pady=10)

        # Progress bar
        self.progress = ttk.Progressbar(root, orient="horizontal", length=920, mode="determinate")
        self.progress.pack(pady=6)

        # Buttons row
        btn_frame = ttk.Frame(root)
        btn_frame.pack(pady=6)
        ttk.Button(btn_frame, text="Instalar Todo", command=self.thread_install_all).grid(row=0, column=0, padx=6)
        ttk.Button(btn_frame, text="Verificar Todo", command=self.thread_verify_all).grid(row=0, column=1, padx=6)
        ttk.Button(btn_frame, text="Actualizar Todo", command=self.thread_update_all).grid(row=0, column=2, padx=6)
        ttk.Button(btn_frame, text="Comprobar PyPI", command=self.thread_check_pypi).grid(row=0, column=3, padx=6)
        ttk.Button(btn_frame, text="Actualizar seleccionados", command=self.thread_update_selected).grid(row=0, column=4, padx=6)
        ttk.Button(btn_frame, text="Ver Log", command=self.mostrar_log).grid(row=0, column=5, padx=6)
        ttk.Button(btn_frame, text="Salir", command=root.quit).grid(row=0, column=6, padx=6)

        # Treeview for packages
        cols = ("package","installed","latest","status")
        self.tree = ttk.Treeview(root, columns=cols, show="headings", selectmode="extended", height=18)
        self.tree.heading("package", text="Package")
        self.tree.heading("installed", text="Installed")
        self.tree.heading("latest", text="Latest (PyPI)")
        self.tree.heading("status", text="Status")
        self.tree.column("package", width=300)
        self.tree.column("installed", width=120, anchor="center")
        self.tree.column("latest", width=120, anchor="center")
        self.tree.column("status", width=260, anchor="center")
        self.tree.pack(padx=10, pady=8)

        # Output log area
        self.output = scrolledtext.ScrolledText(root, height=9)
        self.output.pack(fill="both", padx=10, pady=6, expand=False)

        # initialize table
        self.populate_initial_table()

        # show system info
        sistema = detectar_sistema()
        self.log(f"System detected: {sistema}")
        if requests is None:
            self.log("Warning: `requests` not available. PyPI checks will fail. Install 'requests' to enable PyPI version checking.")

    def log(self, text):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.output.insert(tk.END, f"[{ts}] {text}\n")
        self.output.see(tk.END)

    def populate_initial_table(self):
        for pkg in DEPENDENCIAS:
            inst = get_installed_version(pkg)
            status = "Installed" if inst else "Not installed"
            latest = ""  # unknown yet
            self.tree.insert("", "end", values=(pkg, inst or "-", latest or "-", status))

    # ---- threaded operations ----
    def thread_check_pypi(self):
        threading.Thread(target=self.check_pypi_all, daemon=True).start()

    def thread_install_all(self):
        threading.Thread(target=self.install_all, daemon=True).start()

    def thread_verify_all(self):
        threading.Thread(target=self.verify_all, daemon=True).start()

    def thread_update_all(self):
        threading.Thread(target=self.update_all, daemon=True).start()

    def thread_update_selected(self):
        threading.Thread(target=self.update_selected, daemon=True).start()

    # ---- core operations ----
    def check_pypi_all(self):
        if requests is None:
            messagebox.showwarning("Requests missing", "La librería 'requests' no está instalada. Instala 'requests' para habilitar la comprobación en PyPI.")
            return
        total = len(self.tree.get_children())
        self.progress["value"] = 0
        i = 0
        for item in self.tree.get_children():
            pkg = self.tree.item(item, "values")[0]
            self.log(f"Checking PyPI for package: {pkg}")
            latest = get_pypi_latest(pkg)
            installed = get_installed_version(pkg)
            if latest is None:
                st = "PyPI: unknown"
            else:
                if installed is None:
                    st = "Not installed"
                else:
                    st = "Up-to-date" if self._vercmp(installed, latest) >= 0 else "Outdated"
            # update tree row (must run in main thread)
            self.root.after(0, lambda it=item, lt=latest, ins=installed, stt=st: self.tree.item(it, values=(self.tree.item(it,"values")[0], ins or "-", lt or "-", stt)))
            i += 1
            self.progress["value"] = (i/total) * 100
        self.log("PyPI check completed.")
        guardar_log("pypi_check", "Checked PyPI versions for all packages.")

    def install_all(self):
        total = len(DEPENDENCIAS)
        self.progress["value"] = 0
        for i, pkg in enumerate(DEPENDENCIAS, start=1):
            self.log(f"Installing/upgrading {pkg} ...")
            out = ejecutar_comando(f"{sys.executable} -m pip install --upgrade {pkg}")
            self.log(out.strip())
            # update installed version in table
            inst = get_installed_version(pkg)
            self._update_tree_pkg(pkg, installed=inst)
            self.progress["value"] = (i/total) * 100
        self.log("Install/upgrade all completed.")
        guardar_log("install_all", "Installed/updated all packages.")

    def verify_all(self):
        total = len(DEPENDENCIAS)
        self.progress["value"] = 0
        for i, pkg in enumerate(DEPENDENCIAS, start=1):
            inst = get_installed_version(pkg)
            status = "Installed" if inst else "Not installed"
            self._update_tree_pkg(pkg, installed=inst, status=status)
            self.log(f"{pkg}: {status} (installed={inst})")
            self.progress["value"] = (i/total) * 100
        self.log("Verification completed.")
        guardar_log("verify_all", "Verified all packages.")

    def update_all(self):
        total = len(DEPENDENCIAS)
        self.progress["value"] = 0
        for i, pkg in enumerate(DEPENDENCIAS, start=1):
            self.log(f"Upgrading {pkg} ...")
            out = ejecutar_comando(f"{sys.executable} -m pip install --upgrade {pkg}")
            self.log(out.strip())
            inst = get_installed_version(pkg)
            self._update_tree_pkg(pkg, installed=inst)
            self.progress["value"] = (i/total) * 100
        self.log("Update all completed.")
        guardar_log("update_all", "Updated all packages.")

    def update_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("No selection", "Selecciona los paquetes a actualizar en la tabla.")
            return
        total = len(sel)
        self.progress["value"] = 0
        for i, item in enumerate(sel, start=1):
            pkg = self.tree.item(item, "values")[0]
            self.log(f"Upgrading {pkg} ...")
            out = ejecutar_comando(f"{sys.executable} -m pip install --upgrade {pkg}")
            self.log(out.strip())
            inst = get_installed_version(pkg)
            self._update_tree_pkg(pkg, installed=inst)
            self.progress["value"] = (i/total) * 100
        self.log("Selected update completed.")
        guardar_log("update_selected", f"Updated selected packages: {', '.join([self.tree.item(i,'values')[0] for i in sel])}")

    # ---- helpers to update UI ----
    def _update_tree_pkg(self, pkg, installed=None, latest=None, status=None):
        for item in self.tree.get_children():
            if self.tree.item(item, "values")[0] == pkg:
                current = list(self.tree.item(item, "values"))
                if installed is not None:
                    current[1] = installed or "-"
                if latest is not None:
                    current[2] = latest or "-"
                if status is not None:
                    current[3] = status
                self.root.after(0, lambda it=item, vals=tuple(current): self.tree.item(it, values=vals))
                break

    def mostrar_log(self):
        if not os.path.exists(LOG_FILE):
            messagebox.showinfo("Historial", "No hay historial disponible.")
            return
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = json.load(f)
        ventana = tk.Toplevel(self.root)
        ventana.title("Historial de instalaciones")
        ventana.geometry("700x400")
        txt = scrolledtext.ScrolledText(ventana)
        txt.pack(fill="both", expand=True)
        txt.insert(tk.END, json.dumps(logs, indent=2, ensure_ascii=False))
        txt.configure(state="disabled")

    # simple version compare: returns 1 if a>b, 0 if equal, -1 if a<b
    def _vercmp(self, a, b):
        try:
            import re
            def norm(v):
                return [int(x) if x.isdigit() else x for x in re.split(r'[\.\-]', v)]
            na = norm(a)
            nb = norm(b)
            # compare element-wise
            for x, y in zip(na, nb):
                if isinstance(x, int) and isinstance(y, int):
                    if x > y:
                        return 1
                    if x < y:
                        return -1
                else:
                    xs, ys = str(x), str(y)
                    if xs > ys:
                        return 1
                    if xs < ys:
                        return -1
            # if all equal until now, compare lengths
            if len(na) > len(nb):
                return 1
            if len(na) < len(nb):
                return -1
            return 0
        except Exception:
            return 0

# ---------------------------
# Run app
# ---------------------------
def main():
    root = tk.Tk()
    app = EducaInstallerProV2(root)
    root.mainloop()

if __name__ == "__main__":
    main()
