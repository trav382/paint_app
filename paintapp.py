from tkinter import *
import tkinter.font
from tkinter.colorchooser import *

root = Tk()
root.geometry("800x600")


class PaintApp:
    text_font = StringVar()
    text_size = IntVar()
    bold_text = IntVar()
    italic_text = IntVar()
    drawing_tool = StringVar()

    # Draw settings
    stroke_size = IntVar()
    fill_color = StringVar()
    stroke_color = StringVar()

    # Tracks whether left mouse is clicked
    left_but = "up"

    # Needed for finding where mouse is clicked and when it is released
    x_pos, y_pos = None, None
    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None

    @staticmethod
    def quit_app():
        root.quit()

    def make_menu_bar(self):
        # Creates menu object
        the_menu = Menu(root)

        #   FILE MENU
        # Creates Pull down menu that can't be removed
        file_menu = Menu(the_menu, tearoff=0)

        # Labels in the File Menu
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")

        # Line separator between Save and Quit
        file_menu.add_separator()

        # Clicking on quit will execute the quit function
        file_menu.add_command(label="Quit", command=self.quit_app)

        # Adds pull down menu to menu bar
        the_menu.add_cascade(label="File", menu=file_menu)

        # FONT MENU
        # Creates pull down menu
        font_menu = Menu(the_menu, tearoff=0)

        #Creates pull down menu for Font menu
        font_type_menu = Menu(font_menu, tearoff=0)

        # Buttons for Font type button in the Font submenu
        font_type_menu.add_radiobutton(label="Times", variable=self.text_font)
        font_type_menu.add_radiobutton(label="Courier", variable=self.text_font)
        font_type_menu.add_radiobutton(label="Ariel", variable=self.text_font)

        # Font type menu gets added to Font button on main menu
        font_menu.add_cascade(label="Font Type", menu=font_type_menu)

        # Same process for Font size button
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
        # Font size menu gets added
        font_menu.add_cascade(label="Font Size",
                              menu=font_size_menu)

        font_menu.add_checkbutton(label="Bold",
                                  variable=self.bold_text,
                                  onvalue=1, offvalue=0)
        font_menu.add_checkbutton(label="Italic",
                                  variable=self.italic_text,
                                  onvalue=1, offvalue=0)

        the_menu.add_cascade(label="Font", menu=font_menu)

        # TOOL MENU
        tool_menu = Menu(the_menu, tearoff=0)

        # Creating buttons for all the drawing tools
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

        # Adding Tool menu to the Main menu
        the_menu.add_cascade(label="Tool", menu=tool_menu)

        # COLOR MENU
        color_menu = Menu(the_menu, tearoff=0)

        color_menu.add_command(label="Fill", command=self.pick_fill)
        color_menu.add_command(label="Stroke",command=self.pick_stroke)

        #Creatin submenu for Stroke size
        stroke_width_submenu = Menu(color_menu, tearoff=0)
        stroke_width_submenu.add_radiobutton(label="2",
                                             variable=self.stroke_size,
                                             value=2)
        stroke_width_submenu.add_radiobutton(label="3",
                                             variable=self.stroke_size,
                                             value=3)
        stroke_width_submenu.add_radiobutton(label="4",
                                             variable=self.stroke_size,
                                             value=4)
        stroke_width_submenu.add_radiobutton(label="5",
                                             variable=self.stroke_size,
                                             value=5)
        color_menu.add_cascade(label="Stroke Size",
                               menu=stroke_width_submenu)
        the_menu.add_cascade(label="Color", menu=color_menu)

        root.config(menu=the_menu)

    # Handles when mouse is clicked
    def left_but_down(self, event=None):
        self.left_but = "down"
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y

    # Handles when button is released
    def left_but_up(self, event=None):
        self.left_but = "up"
        # reset line drawings
        self.x_pos = None
        self.y_pos = None
        # where mouse button is released
        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        if self.drawing_tool.get() == "line":
            self.line_draw(event)
        elif self.drawing_tool.get() == "arc":
            self.arc_draw(event)
        elif self.drawing_tool.get() == "oval":
            self.oval_draw(event)
        elif self.drawing_tool.get() == "rectangle":
            self.rectangle_draw(event)
        elif self.drawing_tool.get() == "text":
            self.text_draw(event)

    def motion(self, event=None):
        if self.drawing_tool.get() == "pencil":
            self.pencil_draw(event)

    def pencil_draw(self, event=None):
        if self.left_but == "down":
            if self.x_pos is not None and self.y_pos is not None:
                print("color ", self.stroke_color.get())
                event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y,
                                         smooth=TRUE,
                                         fill=self.stroke_color.get(),
                                         width=self.stroke_size.get())
            self.x_pos = event.x
            self.y_pos = event.y

    def line_draw(self, event=None):
        pass

    def arc_draw(self, event=None):
        pass

    def oval_draw(self, event=None):
        pass

    def rectangle_draw(self, event=None):
        pass

    def text_draw(self, event=None):
        pass

    # function that provides interface to pick a color
    def pick_fill(self, event=None):
        fill_color = askcolor(title='Pick Fill Color')
        if None not in fill_color:
            self.fill_color.set(fill_color[1])

        print("didn't work")

    def pick_stroke(self, event=None):
        stroke_color = askcolor(title='Pick Stroke Color')
        if None not in stroke_color:
            self.stroke_color.set(stroke_color[1])
            print("color ", self.stroke_color.get())

    def __init__(self, root):
        drawing_area = Canvas(root, width=800, height=600)
        drawing_area.pack()
        self.text_font.set("Times")
        self.text_size.set(20)
        self.bold_text.set(0)
        self.italic_text.set(0)
        self.drawing_tool.set("pencil")
        self.stroke_size.set(3)
        self.fill_color.set('#000000')
        self.stroke_color.set('#000000')

        self.make_menu_bar()

        # Set focus for catching events to the canvas
        drawing_area.focus_force()

        # binds motion, clicking and releasing of mouse
        drawing_area.bind("<Motion>", self.motion)
        drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        drawing_area.bind("<ButtonRelease-1>", self.left_but_up)


paint_app = PaintApp(root)
root.mainloop()
