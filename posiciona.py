x1 = y1 = 0  # Armazenam a posição inicial de x e y

print('''Botão Esquerdo: 'place' <Clique na posição inicial e arraste até a posição final>
Botão Scroll:   'geometry' <Mostra as medidas para o posicionamento da janela> "geometry"
Botao Direito: 'X e Y' <Mostra as coordenadas atuais do ponteiro do mouse>''')


def inicio_place(arg):
    global x1, y1
    x1 = arg.x
    y1 = arg.y


def fim_place(arg, master):
    global x1, y1
    print(f'Copiado! .place(width={arg.x - x1}, height={arg.y - y1}, x={x1}, y={y1})')
    master.clipboard_clear()
    master.clipboard_append(f'.place(width={arg.x - x1}, height={arg.y - y1}, x={x1}, y={y1})')


def para_geometry(master):
    print(f'Copiado! .geometry("{master.geometry()}")')
    master.clipboard_clear()
    master.clipboard_append(f'.geometry("{master.geometry()}")')