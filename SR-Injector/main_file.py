import customtkinter as ctk
import os
import platform
import subprocess
from Source.settings_tab import create_settings_tab 
from Source.recovery_tab import create_recovery_tab 
from Source.vehicle_tab import create_vehicle_tab  
from Source.movement_tab import create_movement_tab  

# Initialize the CustomTkinter application
app = ctk.CTk()
app.title("DerpyStudios SR Trainer")
app.geometry("800x600")  # Set the size of the window
app.resizable(False, False)  # Make the window non-resizable

# Set the application icon
#app.iconbitmap('path_to_your_icon.ico')  

# Create a tabview to hold the different menus
tabview = ctk.CTkTabview(app)
tabview.pack(side="left", fill="both", expand=True)

# Add tabs for each menu
tabview.add("Movement")
tabview.add("Vehicle")
tabview.add("Recovery")
tabview.add("Settings")

# Define a function to populate each tab with content
def populate_tabs():
    # Create Movement tab
    create_movement_tab(tabview)

    # Create Vehicle tab
    create_vehicle_tab(tabview)

    # Create Recovery tab
    create_recovery_tab(tabview)

    # Create Settings tab
    create_settings_tab(tabview)

# Populate the tabs with content
populate_tabs()

# Add version text in the bottom right corner of the main window
version_label = ctk.CTkLabel(app, text="Version 1.2", font=("Helvetica", 10))
version_label.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

# Run the application
app.mainloop()
