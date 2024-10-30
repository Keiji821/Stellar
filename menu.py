import yattag
import subprocess
import os

doc, tag, text = yattag.Doc().tagtext()

with tag('html'):
    with tag('head'):
        with tag('title'):
            text('Menú de Opciones')
        with tag('style', type='text/css'):
            text('''
body {
    background-image: url("fondo.jpg");
    background-size: cover;
    font-family: Arial, sans-serif;
    color: #ffffff;
}
table {
    border-collapse: collapse;
    width: 50%; /*Reducimos el ancho de las tablas*/
    margin: 0 auto; /* Centramos las tablas*/
}
th, td {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 5px; /*Reducimos el padding*/
}
th {
    background-color: #00698f;
    color: #ffffff;
    font-size: 12px; /*Reducimos el tamaño de la fuente de los títulos*/
}
td {
    font-size: 10px; /*Reducimos el tamaño de la fuente de las celdas*/
}
''')

    with tag('body'):
        with tag('h1'):
            text('Menú de Opciones')

        # Tabla 1: Comandos principales
        with tag('table', border='1'):
            with tag('tr'):
                with tag('th'):
                    text('Comandos')
                with tag('th'):
                    text('Descripción')
            with tag('tr'):
                with tag('td'):
                    text('reload')
                with tag('td'):
                    text('Recarga la terminal')

        # Tabla 2: Utilidades
        with tag('table', border='1'):
            with tag('tr'):
                with tag('th'):
                    text('Utilidades')
                with tag('th'):
                    text('Descripción')
            with tag('tr'):
                with tag('td'):
                    text('ia')
                with tag('td'):
                    text('Inteligencia Artificial')

        # Tabla 3: OSINT
        with tag('table', border='1'):
            with tag('tr'):
                with tag('th'):
                    text('OSINT')
                with tag('th'):
                    text('Descripción')
            with tag('tr'):
                with tag('td'):
                    text('ipinfo')
                with tag('td'):
                    text('Información de IP')
            with tag('tr'):
                with tag('td'):
                    text('phoneinfo')
                with tag('td'):
                    text('Información de teléfono')
            with tag('tr'):
                with tag('td'):
                    text('urlinfo')
                with tag('td'):
                    text('Información de URL')
            with tag('tr'):
                with tag('td'):
                    text('metadatainfo')
                with tag('td'):
                    text('Información de metadatos')

with open('menu.html', 'w') as f:
    f.write(doc.getvalue())

os.system("termux-open --view menu.html")