<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stellar</title>
</head>
<body>
    <h1>Stellar</h1>
    <p>
        <a href="https://github.com/ellerbrock/open-source-badges/">
            <img src="https://img.shields.io/badge/Código%20Abierto-yes-blue.svg" alt="Código Abierto">
        </a>
        <a href="https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity">
            <img src="https://img.shields.io/badge/Mantenido%20por%20el%20desarrollador-sí-green.svg" alt="Mantenido por el desarrollador">
        </a>
        <a href="https://www.python.org/">
            <img src="https://img.shields.io/badge/Hecho%20con-Python-1f425f.svg?logo=python&logoColor=white" alt="Hecho con Python">
        </a>
        <a href="https://www.gnu.org/software/bash/">
            <img src="https://img.shields.io/badge/Hecho%20con-Bash-1f425f.svg?logo=gnu-bash&logoColor=white" alt="Hecho con Bash">
        </a>
        <a href="https://opensource.org/licenses/MIT">
            <img src="https://img.shields.io/badge/Licencia-MIT-blue.svg" alt="Licencia MIT">
        </a>
        <a href="https://GitHub.com/Keiji821/Stellar/watchers/">
            <img src="https://img.shields.io/github/watchers/Keiji821/Stellar.svg?style=social&label=Watch&maxAge=2592000" alt="GitHub watchers">
        </a>
    </p>
    <h2>Versión 1.0.0</h2>
    <p>
        <a href="https://github.com/Keiji821/Stellar/releases">
            <img src="https://img.shields.io/badge/Versión-1.0.0-blue.svg" alt="Versión 1.0.0">
        </a>
    </p>
    <p><strong>Stellar</strong> es una herramienta de hacking para Termux diseñada para personalizar y mejorar la apariencia de tu terminal. Cambia el entorno predeterminado con un diseño más atractivo y funcional.</p>
    
    <h3>Tabla de Contenidos</h3>
    <ul>
        <li><a href="#pasos-de-instalación">Pasos de Instalación</a></li>
        <li><a href="#características">Características</a></li>
        <li><a href="#guía-de-uso">Guía de Uso</a></li>
        <li><a href="#registro-de-cambios">Registro de Cambios</a></li>
        <li><a href="#contribuciones">Contribuciones</a></li>
        <li><a href="#licencia">Licencia</a></li>
    </ul>

    <h3 id="pasos-de-instalación">Pasos de Instalación</h3>
    <p><strong>Nota:</strong> Abre tu terminal y copia y pega los siguientes comandos:</p>

    <h4>Termux</h4>
    <pre>
        <code>
pkg upgrade -y && pkg update -y
pkg install -y git
git clone https://github.com/Keiji821/Stellar
cd Stellar
bash install.sh
        </code>
    </pre>
    <p>Comando único:</p>
    <pre>
        <code>
pkg upgrade -y && pkg update -y && pkg install -y git && git clone https://github.com/Keiji821/Stellar && cd Stellar && bash install.sh
        </code>
    </pre>

    <h4>Linux (Debian/Ubuntu/Kali Linux)</h4>
    <p>En desarrollo...</p>

    <h3 id="características">Características</h3>
    <h4>Misc</h4>
    <table>
        <thead>
            <tr>
                <th>Comando</th>
                <th>Descripción</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>ia</td>
                <td>Un pequeño servicio de inteligencia artificial mediante una API gratuita.</td>
            </tr>
            <tr>
                <td>myip</td>
                <td>Muestra tu IP real y obtiene información de la IP.</td>
            </tr>
        </tbody>
    </table>

    <h4>Osint</h4>
    <table>
        <thead>
            <tr>
                <th>Comando</th>
                <th>Descripción</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>ipinfo</td>
                <td>Obtiene la información de una IP, ya sea IPV4 o IPV6.</td>
            </tr>
            <tr>
                <td>phoneinfo</td>
                <td>Obtiene la información de un número de teléfono.</td>
            </tr>
            <tr>
                <td>metadatainfo</td>
                <td>Recupera los metadatos de una imagen, archivo o video.</td>
            </tr>
            <tr>
                <td>urlinfo</td>
                <td>Obtiene información relevante de una URL o enlace.</td>
            </tr>
            <tr>
                <td>emailsearch</td>
                <td>Busca correos electrónicos con el nombre y apellido proporcionados.</td>
            </tr>
        </tbody>
    </table>

    <h4>Pentest</h4>
    <table>
        <thead>
            <tr>
                <th>Comando</th>
                <th>Descripción</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>En desarrollo</td>
                <td></td>
            </tr>
        </tbody>
    </table>

    <h4>Phishing</h4>
    <table>
        <thead>
            <tr>
                <th>Comando</th>
                <th>Descripción</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>En desarrollo</td>
                <td></td>
            </tr>
        </tbody>
    </table>

    <h4>Encryption</h4>
    <table>
        <thead>
            <tr>
                <th>Comando</th>
                <th>Descripción</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>En desarrollo</td>
                <td></td>
            </tr>
        </tbody>
    </table>

    <h4>Chat Tor</h4>
    <table>
        <thead>
            <tr>
                <th>Comando</th>
                <th>Descripción</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>En desarrollo</td>
                <td></td>
            </tr>
        </tbody>
    </table>

    <p><strong>Seguridad:</strong> La herramienta anonimiza todas las acciones usando Tor en la terminal.</p>

    <h3 id="guía-de-uso">Guía de Uso</h3>
    <p>Después de ejecutar el archivo <code>install.sh</code>, tu sesión de Termux se reiniciará y la herramienta se iniciará automáticamente. Para ver la lista de comandos disponibles, ejecuta <code>menu</code> en la terminal.</p>

    <h3 id="registro-de-cambios">Registro de Cambios</h3>
    <h4>Actualización 00/00/2024</h4>
    <ul>
        <li>Descripción de los cambios realizados.</li>
    </ul>

    <h3 id="contribuciones">Contribuciones</h3>
    <p>Las contribuciones son bienvenidas. Si deseas contribuir, por favor sigue los siguientes pasos:</p>
    <ol>
        <li>Realiza un fork del repositorio.</li>
        <li>Crea una nueva rama (<code>git checkout -b feature/nueva-funcionalidad</code>).</li>
        <li>Realiza los cambios necesarios y realiza commit (<code>git commit -am 'Agregar nueva funcionalidad'</code>).</li>
        <li>Envía tus cambios a la rama (<code>git push origin feature/nueva-funcionalidad</code>).</li>
        <li>Crea un nuevo Pull Request.</li>
    </ol>

    <h3 id="licencia">Licencia</h3>
    <p>Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo <a href="LICENSE">LICENSE</a> para más detalles.</p>
</body>
</html>