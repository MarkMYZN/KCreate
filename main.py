# if windows:
# pyinstaller main.py --onefile
# and you can just share the exe inside the dist folder



# if linux:
# if pyinstaller not installed, run these commands:
# sudo apt install pipx                   # this install pipx
# pipx ensure path                        # this adds it to your path
# pipx install pyinstaller                # this actually installs pyinstaller
# pyinstaller --onefile main.py           # this makes the script you made a .deb file to run in linux

# ======================================================================================================== #

import os
import subprocess
import platform

print("You are creating a project in:", platform.system(),"\n")

# default Kivy Hello World example
KDefault = """from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Hello, Kivy!")

if __name__ == "__main__":
    MyApp().run()
"""


# if System is Windows
if platform.system() == 'Windows':
  print("creating project...")

# creating the project
  os.mkdir("kivy-project")
  os.chdir("kivy-project")
  subprocess.run(["py","-3.13","-m","venv","venv"])
  subprocess.run(["venv/Scripts/pip","install","kivy[full]"])
  with open("main.kv","x") as file:
    file.write(KDefault)
  print("Done Creating Project")
  print("Openning Project in VSCode...")
  subprocess.run(["code", "."], shell=True)

# if System is Linux
elif platform.system() == 'Linux':
  print("Creating Project...\n\n")

  os.mkdir("kivy-project")
  os.chdir("kivy-project")

  print("Please input your linux password before continuing.")
  print("The program uses the command 'sudo' to install some dependencies and Kivy itself.\n")
  print("If you see this message interrupting the process again,")
  print("It is because you are running this in a new terminal.\n")
  subprocess.run([
    "sudo",
    "apt",
    "install",
    "-y",
    "python3-pip",
    "python3-setuptools",
    "python3-venv",
    "xclip",
    "xsel",
    "libsdl2-dev",
    "libsdl2-image-dev",
    "libsdl2-mixer-dev",
    "libsdl2-ttf-dev",
    "libportmidi-dev",
    "libswscale-dev",
    "libavformat-dev",
    "libavcodec-dev",
    "zlib1g-dev"])
  subprocess.run(["python3","-m","venv","venv"])
  subprocess.run(["venv/bin/pip","install","kivy[full]"])
  with open("main.kv","x") as file:
    file.write(KDefault)
  print("Done Creating Project")
  print("Openning Project in VSCode...")
  subprocess.run(["code", "."])

  
