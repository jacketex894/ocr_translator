import customtkinter
from functools import partial
from util.ocr_translation import start_recognition_thread,start_translate_thread
WINDOW_TITLE = "OCR Translator"
WINDOW_SIZE = "800x400"
LABEL_TEXT_COLOR = "#FFFFFF"
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
    recognition_label = customtkinter.CTkLabel(root, text="Recognize Text:{}", text_color=LABEL_TEXT_COLOR)
    recognition_label.grid(row=3, column=0, padx=0, pady=10)

    recognition_button = customtkinter.CTkButton(
        root, 
        text="Start OCR", 
        command=partial(start_recognition_thread, recognition_label), 
        fg_color=BUTTON_COLOR
    )
    recognition_button.grid(row=2, column=0, padx=0, pady=10)

    translate_label = customtkinter.CTkLabel(root, text="Translate Text:{}", text_color=LABEL_TEXT_COLOR)
    translate_label.grid(row=5, column=0, padx=0, pady=10)
    button = customtkinter.CTkButton(
        root, 
        text="Start translate", 
        command=partial(start_translate_thread, translate_label), 
        fg_color=BUTTON_COLOR
    )
    button.grid(row=4, column=0, padx=0, pady=10)

    

def main():
    root = create_main_window()
    setup_widgets(root)
    root.mainloop()

if __name__ == "__main__":
    main()