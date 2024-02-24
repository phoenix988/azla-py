from src.widgets.button.main import Button
from src.widgets.window.main import Window
from src.widgets.list.main import Combo
from src.widgets.box.main import Box
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


# Define a callback function for the button click event


class Azla:
    # Initialize GTK
    Gtk.init()

    Box.main_menu.add(Combo.word_combo)
    Box.main_menu.add(Button.start)
    Box.main_menu.add(Button.exit)

    # Add main menu box to the window
    Window.main.add(Box.main_menu)

    # Show all widgets
    Window.main.show_all()

    def run():
        # Run the GTK main loop
        Gtk.main()
