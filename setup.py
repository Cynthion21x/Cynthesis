import sys
from cx_Freeze import setup, Executable

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="Cynthesis",
    version="1",
    description="Particle Life Simulation",
    executables=[Executable("main.py", base=base, target_name="Cynthesis.exe")],
)