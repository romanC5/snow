import customtkinter as ctk

def create_movement_tab(parent_tabview):
    movement_frame = ctk.CTkFrame(parent_tabview.tab("Movement"))
    movement_frame.pack(expand=True, fill="both", padx=20, pady=20)

    # Add "Coming Soon" text in bold, red color, and center-aligned
    ctk.CTkLabel(
        movement_frame, 
        text="Coming Soon", 
        font=("Helvetica", 16, "bold"),  # Bold only
        text_color="red"
    ).pack(pady=20, padx=20, anchor="center")
