import yattag
import subprocess

# Crear un objeto Doc
doc, tag, text = yattag.Doc().tagtext()

# Crear un título para el menú
with tag('h1'):
    text('Menú de Opciones')

# Crear un tabla para el menú
with tag('table', border='1'):
    # Crear una fila de título
    with tag('tr'):
        with tag('th'):
            text('Opción')
        with tag('th'):
            text('Descripción')

    # Crear filas para cada opción del menú
    for option in menu_options:
        with tag('tr'):
            with tag('td'):
                text(option['name'])
            with tag('td'):
                text(option['description'])

# Crear un archivo HTML temporal
with open('menu.html', 'w') as f:
    f.write(doc.getvalue())

# Abrir el archivo HTML en la aplicación predeterminada de Termux
subprocess.run(['termux-open', 'menu.html'])