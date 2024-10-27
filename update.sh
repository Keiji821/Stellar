# Verificar si el archivo.bashrc existe en la carpeta stellar
if [! -f ~/Stellar/.bashrc ]; then
  # Crear un nuevo archivo.bashrc en la carpeta stellar
  touch ~/Stellar/.bashrc
  echo "Archivo.bashrc creado de nuevo en la carpeta stellar!"
fi