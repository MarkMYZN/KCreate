# Kivy Project Creator

A lightweight Python script designed to automate the tedious parts of setting up a new Kivy development environment. It handles directory creation, virtual environment configuration, dependency installation, and boilerplate generation in one go.

---

## ✨ Features

* **Automated Setup**

  * Creates a `kivy-project` directory and moves into it automatically. You can edit the name of the project folder after the process.

* **Environment Management**

  * Automatically creates and configures a Python Virtual Environment (`venv`).

* **Dependency Handling**

  * Installs `kivy[full]` and essential system libraries (on Linux).

* **Boilerplate Generation**

  * Writes a functional **"Hello World"** `main.py` so you can start testing immediately.

* **IDE Integration**

  * Automatically opens the finished project in **VS Code**.

---

## 🚀 How to Use

### 🪟 Windows

1. Ensure **Python 3.13** is installed.
2. Run the creator script:

```bash
python main.py
```

---

### 🐧 Linux (Ubuntu / Debian)

1. Run the creator script:

```bash
python3 main.py
```

> **Note**
> The script will ask for your **sudo password** to install required system dependencies
> (SDL2, GStreamer, etc.) necessary for Kivy to render windows.

---

## 🛠️ Requirements

* **Python**

  * Windows version specifically looks for `py -3.13`

* **VS Code**

  * Must be installed and available in your system `PATH` (so the `code` command works)

---

## 📦 Distribution

If you want to compile this creator into a single executable file:

### 🪟 Windows

```bash
pyinstaller main.py --onefile
```

---

### 🐧 Linux

```bash
pipx install pyinstaller
pyinstaller --onefile main.py
```

---

## 📝 Generated Boilerplate

Once the script finishes, your `main.py` will contain:

```python
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Hello, Kivy!")

if __name__ == "__main__":
    MyApp().run()
```
* PS: 
In linux, If you encounter the error where it says "App has no known associated programs with it", just go to the file's properties and enable "Allow executing files as program" and you should be good to go.

---

Thats all and Happy coding with **Kivy**!

---
