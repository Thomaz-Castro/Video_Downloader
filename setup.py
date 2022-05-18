import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter", "moviepy.editor", "emoji", "pytube"], "include_files": ["icone.ico"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
#Comando no terminal: python .\setup.py build_exe --include-files=mp
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Video Downloader",
    version="1.0",
    description="Downloader de videos do Youtube feito por Thomaz Castro",
    options={"build_exe": build_exe_options},
    executables=[Executable("Downloader.py", base=base, icon="icone.ico")]
)