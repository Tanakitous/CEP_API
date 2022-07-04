
from threading import local
import requests, tkinter

#funções
def busca_cep():
    x = str(e1.get())
    if len(x) != 8:
        final.set("Inválido")
        
    else:
        request= requests.get("https://viacep.com.br/ws/"+ x +"/json/")
        address = request.json()
        if 'erro' not in address:
            final.set("Válido")
            rua.set(""+address['logradouro'])
            complemento.set(""+address['complemento'])
            bairro.set(""+address['bairro'])
            localidade.set(""+address['localidade'])
            uf.set(""+address['uf'])
        else:
            final.set("Inválido")
            
    
def correct(inp):
    if inp.isdigit():
        return True
    elif inp is "":
        return True
    else:
        return False


#GUI

root = tkinter.Tk()
root.title("Busca CEP")
root.configure(background="#dde")



#widget
l1=tkinter.Label(root, text="CEP: ", background="#dde").grid(sticky="e")
e1=tkinter.Entry(root)
e1.grid(row=0, column=1)
reg=root.register(correct)
e1.config(validate="key", validatecommand=(reg, "%P"))

final = tkinter.StringVar()
rua = tkinter.StringVar()
complemento = tkinter.StringVar()
bairro = tkinter.StringVar()
localidade = tkinter.StringVar()
uf = tkinter.StringVar()

l2=tkinter.Label(root, text="Logradouro: ", justify='right', background="#dde").grid(sticky="e")
l21=tkinter.Label(root,textvariable=rua, background="#dde").grid(row=1, column=1)

l3=tkinter.Label(root, text="Complemento: ", background="#dde").grid(sticky="e")
l31=tkinter.Label(root,textvariable=complemento, background="#dde").grid(row=2, column=1)

l4=tkinter.Label(root, text="Bairro: ", background="#dde").grid(sticky="e")
l41=tkinter.Label(root,textvariable=bairro, background="#dde").grid(row=3, column=1)

l5=tkinter.Label(root, text="Localidade: ", background="#dde").grid(sticky="e")
l51=tkinter.Label(root,textvariable=localidade, background="#dde").grid(row=4, column=1)

l6=tkinter.Label(root, text="UF: ", background="#dde").grid(sticky="e")
l61=tkinter.Label(root,textvariable=uf, background="#dde").grid(row=5, column=1)

b1=tkinter.Button(root, text="Buscar", command=busca_cep).grid(sticky="w",column=1)

l11=tkinter.Label(root, textvariable=final, background="#dde").grid(sticky="w", column=1)

root.mainloop()

#layout

