import tkinter as tk
from tkinter import ttk, messagebox

#Window setup
root = tk.Tk()
root.title("Multiplication Table")
root.configure(padx=20, pady=18, bg="#00d0fa")
WIDTH, HEIGHT = 420, 320
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = (screen_w - WIDTH) // 2
y = (screen_h - HEIGHT) // 3
root.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
root.resizable(False, False)

#Styles
style = ttk.Style(root)
style.configure("TLabel")
style.configure("Header.TLabel", font=("arial", 18, "bold"), foreground="#2b2e7a")
style.configure("TButton", font=("arial", 10, "bold"))
style.configure("TEntry", padding=4)

#Header
header = ttk.Label(root, text="Multiplication Table", style="Header.TLabel")
header.pack(pady=(0, 12))

#Input
frm = ttk.Frame(root)
frm.pack(fill="x", padx=6)

lbl_num = ttk.Label(frm, text="Number:")
lbl_num.grid(row=0, column=0, sticky="e", padx=(0,6))
ent_num = ttk.Entry(frm, width=10)
ent_num.grid(row=0, column=1, sticky="w")

lbl_upto = ttk.Label(frm, text="Up to:")
lbl_upto.grid(row=0, column=2, sticky="e", padx=(12,6))
ent_upto = ttk.Entry(frm, width=10)
ent_upto.grid(row=0, column=3, sticky="w")


#function of Buttons
btn_frame = ttk.Frame(root)
btn_frame.pack(pady=10)

def generate():
    try:
        n = int(ent_num.get().strip())
        upto = int(ent_upto.get().strip())
        if upto <= 0:
            raise ValueError("Up to must be > 0")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid integers (Up to > 0).")
        return

    txt_result.config(state="normal")
    txt_result.delete("1.0", "end")
    lines = [f"{n} × {i:2} = {n*i}" for i in range(1, upto+1)]
    txt_result.insert("1.0", "\n".join(lines))
    txt_result.config(state="disabled")

def clear():
    ent_num.delete(0, "end")
    ent_upto.delete(0, "end")
    txt_result.config(state="normal")
    txt_result.delete("1.0", "end")
    txt_result.config(state="disabled")
    ent_num.focus()
#buttons
btn_gen = ttk.Button(btn_frame, text="Generate", command=generate)
btn_gen.grid(row=0, column=0, padx=8)
btn_clear = ttk.Button(btn_frame, text="Clear", command=clear)
btn_clear.grid(row=0, column=1, padx=8)

#Result box 
res_frame = ttk.Frame(root)
res_frame.pack(fill="both", expand=True, padx=6)

txt_result = tk.Text(res_frame, height=9, wrap="none", font=("Courier New", 11), state="disabled", bd=1, relief="solid")
txt_result.pack(side="left", fill="both", expand=True)

scroll = ttk.Scrollbar(res_frame, orient="vertical", command=txt_result.yview)
scroll.pack(side="right", fill="y")
txt_result.config(yscrollcommand=scroll.set)

root.mainloop()
