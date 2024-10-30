import yattag
import subprocess
import os

doc, tag, text = yattag.Doc().tagtext()

with tag('html'):
    with tag('head'):
        with tag('title'):
            text('Menú de Opciones')

    with tag('body'):
        with tag('h1'):
            text('Menú de Opciones')

        with tag('table', border='1'):
            with tag('tr'):
                with tag('th'):
                    text('Opción')
                with tag('th'):
                    text('Descripción')

        menu_options = [
            {'name': 'Opción 1', 'description': 'Descripción de la opción 1'},
            {'name': 'Opción 2', 'description': 'Descripción de la opción 2'},
            {'name': 'Opción 3', 'description': 'Descripción de la opción 3'},
        ]

        for option in menu_options:
            with tag('tr'):
                with tag('td'):
                    text(option['name'])
                with tag('td'):
                    text(option['description'])

with open('menu.html', 'w') as f:
    f.write(doc.getvalue())

os.system("termux-open menu.html")