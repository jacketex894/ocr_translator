import customtkinter
from functools import partial
from util.image_test_recognition import start_recognition_thread

WINDOW_TITLE = "OCR Tra"
WINDOW_SIZE = "1024x768"
LABEL_TEXT = "Recognize Text:{}"
LABEL_TEXT_COLOR = "#FFFFFF"
BUTTON_TEXT = "Start OCR"
BUTTON_COLOR = "#46A3FF"
BACKGROUND_COLOR = "#272727"

def create_main_window():
    root = customtkinter.CTk()
    root.title(WINDOW_TITLE)
    root.geometry(WINDOW_SIZE)
    root.configure(fg_color=BACKGROUND_COLOR)
    root.grid_columnconfigure(0, weight=1)
    return root

def setup_widgets(root):
    label = customtkinter.CTkLabel(root, text=LABEL_TEXT, text_color=LABEL_TEXT_COLOR)
    label.grid(row=1, column=0, padx=0, pady=10)

    button = customtkinter.CTkButton(
        root, 
        text=BUTTON_TEXT, 
        command=partial(start_recognition_thread, label), 
        fg_color=BUTTON_COLOR
    )
    button.grid(row=0, column=0, padx=0, pady=10)

    return label, button

def main():
    root = create_main_window()
    setup_widgets(root)
    root.mainloop()

if __name__ == "__main__":
    main()