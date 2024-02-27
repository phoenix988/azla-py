# from src.widgets.button.main import Button
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


# Create a box class
class Box:

    main_menu = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                        spacing=6)
    question_menu = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                            spacing=6)

    # Set the box to center
    main_menu.set_valign(Gtk.Align.CENTER)
    question_menu.set_valign(Gtk.Align.CENTER)

    # Hide the question box
    question_menu.hide()
