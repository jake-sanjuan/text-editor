"""Program Text Editor by Jacob San Juan

A simple text editor that allows users to create files, save text, and access saved files."""

import tkinter as tk


def open_editor(new_or_saved, filename):
    """Opens blank text editor window"""
    editor_window = tk.Tk()

    greeting = tk.Label(text="Hannibal's Text Editor", width=78)
    greeting.pack()

    text_window = tk.Text(width=80, height=50)
    text_window.pack()

    if new_or_saved:
        open_saved_file(text_window, filename)

    save_button = tk.Button(master=editor_window, text='Save', activeforeground='#878889',
                            command=lambda: save_text(text_window, filename))
    save_button.pack()

    editor_window.mainloop()


def open_saved_file_window():
    """Opens window that allows user to enter the name of a file that they have saved"""
    saved_file_window = tk.Tk()

    label = tk.Label(text="Please enter filename without format specifier: ")
    label.pack()

    entry = tk.Entry(width=35)
    entry.pack()

    button = tk.Button(text='open', command=lambda: close_window(
        saved_file_window,
        button='open',
        arg=entry.get()
    ))
    button.pack()

    saved_file_window.mainloop()


def new_or_saved():
    """Opens window that prompts user to choose whether they would like to open a new
    or a saved file"""
    new_or_saved_window = tk.Tk()

    greeting = tk.Label(text="Would you like to open a new file or load a saved one?")
    greeting.pack()

    saved_button = tk.Button(master=new_or_saved_window,
                             text='saved',
                             command=lambda: close_window(new_or_saved_window, "save"))
    saved_button.pack()

    new_button = tk.Button(master=new_or_saved_window,
                           text='new',
                           command=lambda: close_window(new_or_saved_window, "new"))
    new_button.pack()

    new_or_saved_window.mainloop()


def filename_window():
    """Window opens when new file button is chosen.  Allows user to input name of file"""
    filename_window = tk.Tk()

    label = tk.Label(text="Enter filename without file format (will be made txt file): ")
    label.pack()

    entry = tk.Entry(width=35)
    entry.pack()

    button = tk.Button(text='create',
                       command=lambda: close_window(arg=entry.get(),
                                                    window=filename_window,
                                                    button='create'))
    button.pack()

    filename_window.mainloop()


def save_text(text_window, filename):
    """Function saves text in file filename"""
    text = text_window.get(1.0, tk.END)
    with open(filename, "w") as f_obj:
        f_obj.write(text)


def open_saved_file(text_window, filename):
    """Used to open saved file"""
    try:
        filename = filename + '.txt'
        with open(filename, 'r') as f_obj:
            text = f_obj.read()
        text_window.insert(1.0, text)
    except FileNotFoundError:
        print("File not found!")
        exit(1)


def open_saved(filename=None):
    """Opens saved text file for user"""
    open_editor(True, filename)


def create_new_file(user_text):
    """Creates new file with user-entered filename"""
    filename = user_text + '.txt'
    open_editor(False, filename)


def close_window(window, button=None, arg=None):
    """Invoked to close window, opens window associated with command from button click"""
    window.destroy()
    if button == 'save':
        open_saved_file_window()
    if button == 'new':
        filename_window()
    if button == 'create':
        create_new_file(arg)
    if button == 'open':
        open_saved(arg)


def main():
    """Calls new_or_saved window to start program"""
    new_or_saved()


if __name__ == '__main__':
    main()
