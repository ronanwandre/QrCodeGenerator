import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser

def gerar_qr():
    dado = entrada_texto.get()
    if not dado:
        messagebox.showerror("Erro", "Digite um texto ou URL para gerar o QR Code!")
        return
    
    cor_fg = colorchooser.askcolor(title="Escolha a cor do QR Code")[1]
    cor_bg = colorchooser.askcolor(title="Escolha a cor de fundo")[1]

    if not cor_fg or not cor_bg:
        messagebox.showerror("Erro", "Escolha cores válidas!")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(dado)
    qr.make(fit=True)

    img = qr.make_image(fill_color=cor_fg, back_color=cor_bg)
    
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if caminho_arquivo:
        img.save(caminho_arquivo)
        messagebox.showinfo("Sucesso", f"QR Code salvo em:\n{caminho_arquivo}")

root = tk.Tk()
root.title("Gerador de QR Code")
root.geometry("400x250")

tk.Label(root, text="Digite a URL ou mensagem:", font=("Arial", 12)).pack(pady=10)
entrada_texto = tk.Entry(root, width=40, font=("Arial", 12))
entrada_texto.pack(pady=5)

btn_gerar = tk.Button(root, text="Gerar QR Code", font=("Arial", 12), command=gerar_qr)
btn_gerar.pack(pady=10)

root.mainloop()