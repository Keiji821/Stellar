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
     width: 100%;
 }
 th, td {
     border: 1px solid #dddddd;
     text-align: left;
     padding: 8px;
 }
 th {
     background-color: #00698f;
     color: #ffffff;
 }
''')

    with tag('body'):
        with tag('h1'):
            text('Menú de Opciones')

        # Tabla 1: Comandos principales
        with tag('table', border='1'):
            with tag('tr'):
                with tag('th', colspan='2'):
                    text('Comandos principales')
            with tag('tr'):
                with tag('td'):
                    text('reload')

        # Tabla 2: Utilidades
        with tag('table', border='1'):
            with tag('tr'):
                with tag('th', colspan='2'):
                    text('Utilidades')
            with tag('tr'):
                with tag('td'):
                    text('ia')

        # Tabla 3: OSINT
        with tag('table', border='1'):
            with tag('tr'):
                with tag('th', colspan='2'):
                    text('OSINT')
            with tag('tr'):
                with tag('td'):
                    text('ipinfo')
            with tag('tr'):
                with tag('td'):
                    text('phoneinfo')
            with tag('tr'):
                with tag('td'):
                    text('urlinfo')
            with tag('tr'):
                with tag('td'):
                    text('metadatainfo')

with open('menu.html', 'w') as f:
    f.write(doc.getvalue())

os.system("termux-open --view menu.html")