import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
						"packages": ["os", "pygame"],
						"excludes": ["tkinter"],
						"include_files" : ["data"]
					}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None

if sys.platform == "win32":
    base = "Win32GUI"

target = Executable(
						script="run_game.pyw",
						base=base,
						targetName="HostilPlanet.exe",
						compress=False,
						copyDependentFiles=True,
						appendScriptToExe=True,
						appendScriptToLibrary=False,
						icon="icon.ico",
						shortcutName="Hostil Planet",
						shortcutDir="DesktopFolder",
)

setup(	name = "Hostil Planet",
		version = "0.1",
		author="Jauria Studios",
		description = "Hostil Planet by Jauria Studios",
		options = {"build_exe": build_exe_options},
		executables = [target]
)
