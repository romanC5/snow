import customtkinter as ctk

def create_recovery_tab(parent_tabview):
    recovery_frame = ctk.CTkFrame(parent_tabview.tab("Recovery"))
    recovery_frame.pack(expand=True, fill="both", padx=20, pady=20)

    # Add label for Recovery Options
    ctk.CTkLabel(recovery_frame, text="Recovery Options").grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="n")

    # Add buttons to the Recovery tab
    ctk.CTkButton(recovery_frame, text="Set 500 Million Cash", command=lambda: print("500 Million Cash set")).grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    ctk.CTkButton(recovery_frame, text="Set Level 30", command=lambda: print("Level 30 set")).grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    ctk.CTkButton(recovery_frame, text="Unlock All Maps", command=lambda: print("All Maps Unlocked")).grid(row=2, column=0, padx=10, pady=10, sticky="ew")
    ctk.CTkButton(recovery_frame, text="Complete Game", command=lambda: print("Game Completed")).grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    # Center the buttons
    recovery_frame.grid_columnconfigure(0, weight=1)
    recovery_frame.grid_columnconfigure(1, weight=1)
    recovery_frame.grid_rowconfigure(1, weight=1)
    recovery_frame.grid_rowconfigure(2, weight=1)
