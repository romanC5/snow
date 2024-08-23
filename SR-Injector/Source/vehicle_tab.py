import customtkinter as ctk

def create_vehicle_tab(parent_tabview):
    vehicle_frame = ctk.CTkFrame(parent_tabview.tab("Vehicle"))
    vehicle_frame.pack(expand=True, fill="both", padx=20, pady=20)

    # Add label for Vehicle Options
    ctk.CTkLabel(vehicle_frame, text="Vehicle Options").grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="n")

    # Add options for the Vehicle tab in two rows, centered
    ctk.CTkButton(vehicle_frame, text="No Damage", command=lambda: print("No Damage Activated")).grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    ctk.CTkButton(vehicle_frame, text="Unlimited Fuel", command=lambda: print("Unlimited Fuel Activated")).grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    ctk.CTkButton(vehicle_frame, text="Unlimited Spare Tires", command=lambda: print("Unlimited Spare Tires Activated")).grid(row=2, column=0, padx=10, pady=10, sticky="ew")
    ctk.CTkButton(vehicle_frame, text="Skip 1 Hour", command=lambda: print("Skipped 1 Hour")).grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    # Center the content
    vehicle_frame.grid_columnconfigure(0, weight=1)
    vehicle_frame.grid_columnconfigure(1, weight=1)
    vehicle_frame.grid_rowconfigure(1, weight=1)
    vehicle_frame.grid_rowconfigure(2, weight=1)
