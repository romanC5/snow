import customtkinter as ctk
import os
import platform
import subprocess

# Global variable to keep track of the current theme
current_theme = "light"

def create_settings_tab(parent_tabview):
    settings_frame = ctk.CTkFrame(parent_tabview.tab("Settings"))
    settings_frame.pack(expand=True, fill="both", padx=20, pady=20)

    # Add dark mode switch
    dark_mode_switch = ctk.CTkSwitch(settings_frame, text="Dark Mode", command=lambda: toggle_dark_mode(dark_mode_switch))
    dark_mode_switch.pack(pady=10)

    # Add "Open SnowRunner .pak Directory" button
    open_directory_button = ctk.CTkButton(settings_frame, text="Open SnowRunner .pak Directory", command=open_snowrunner_directory)
    open_directory_button.pack(pady=10)

def toggle_dark_mode(switch):
    global current_theme
    if switch.get():
        if current_theme != "dark":
            apply_dark_theme()
            current_theme = "dark"
    else:
        if current_theme != "light":
            apply_light_theme()
            current_theme = "light"

def apply_dark_theme():
    ctk.set_appearance_mode("dark")
    print("Dark mode enabled")

def apply_light_theme():
    ctk.set_appearance_mode("light")
    print("Light mode enabled")

def open_snowrunner_directory():
    # Path to the SnowRunner .pak directory (change this to your specific path)
    pak_directory = r"C:\Path\To\SnowRunner\pak_files"  # Example path, adjust as needed

    if platform.system() == "Windows":
        subprocess.Popen(f'explorer "{pak_directory}"')
    elif platform.system() == "Darwin":  # macOS
        subprocess.Popen(["open", pak_directory])
    elif platform.system() == "Linux":
        subprocess.Popen(["xdg-open", pak_directory])
    else:
        print("Unsupported OS")
