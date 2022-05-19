from tkinter import *
import tkinter.font

root = Tk()
root.geometry("800x600")

class PaintApp:

    text_font = StringVar()
    text_size = IntVar()
    bold_text = IntVar()
    italic_text = IntVar()
    drawing_tool = StringVar()

    left_but = "up"
    x_pos, y_pos = None, None
    x1_line_pt, y1_line_pt,x2_line_pt, y2_line_pt = None, None, None, None

    @staticmethod
    def quit_app():
        root.quit()

    def make_menu_bar(self):
        the_menu = Menu(root)

        #File menu
        file_menu = Menu(the_menu, tearoff=0)
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.quit_app)
        the_menu.add_cascade(label="File", menu=file_menu)

        # Font menu

        font_menu = Menu(the_menu, tearoff=0)
        font_type_menu = Menu(font_menu, tearoff=0)

        font_type_menu.add_radiobutton(label="Times", variable=self.text_font)
        font_type_menu.add_radiobutton(label="Courier", variable=self.text_font)
        font_type_menu.add_radiobutton(label="Ariel", variable=self.text_font)

        font_menu.add_cascade(label="Font Type", menu=font_type_menu)

        font_size_menu = Menu(font_menu, tearoff=0)
        font_size_menu.add_radiobutton(label="12",
                                       variable=self.text_font,
                                       value=12)
        font_size_menu.add_radiobutton(label="16",
                                       variable=self.text_font,
                                       value=16)
        font_size_menu.add_radiobutton(label="20",
                                       variable=self.text_font,
                                       value=20)
        font_size_menu.add_radiobutton(label="25",
                                       variable=self.text_font,
                                       value=25)
        font_menu.add_cascade(label="Font Size",
                              menu=font_size_menu)
        font_menu.add_checkbutton(label="Bold",
                                  variable=self.bold_text,
                                  onvalue=1, offvalue=0)
        font_menu.add_checkbutton(label="Italic",
                                  variable=self.italic_text,
                                  onvalue=1, offvalue=0)

        the_menu.add_cascade(label="Font", menu=font_menu)

        #Tool menu
        tool_menu = Menu(the_menu, tearoff=0)
        tool_menu.add_radiobutton(label="Pencil",
                                  variable=self.drawing_tool,
                                  value="pencil")
        tool_menu.add_radiobutton(label="Line",
                                  variable=self.drawing_tool,
                                  value="line")
        tool_menu.add_radiobutton(label="Arc",
                                  variable=self.drawing_tool,
                                  value="arc")
        tool_menu.add_radiobutton(label="Oval",
                                  variable=self.drawing_tool,
                                  value="oval")
        tool_menu.add_radiobutton(label="Rectangle",
                                  variable=self.drawing_tool,
                                  value="rectangle")
        tool_menu.add_radiobutton(label="Text",
                                  variable=self.drawing_tool,
                                  value="text")
        the_menu.add_cascade(label="Tool", menu=tool_menu)
        root.config(menu=the_menu)

    def __init__(self, root):
        drawing_area = Canvas(root)
        drawing_area.pack()
        self.text_font.set("Times")
        self.text_size.set(20)
        self.bold_text.set(0)
        self.italic_text.set(0)
        self.drawing_tool.set("line")
        self.make_menu_bar()


paint_app = PaintApp(root)
root.mainloop()

