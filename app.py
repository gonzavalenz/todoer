import os

from todo import configuracion

configuracion.cargar_variables()

import subprocess

def ejecutar_flask_run():
    subprocess.call(['flask', 'run'])

ejecutar_flask_run()

