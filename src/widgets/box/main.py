from src.widgets.button.main import Button
from gi.repository import Gtk
import gi
gi.require_version('Gtk', '3.0')


# Create a box class
class Box:

    main_menu = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                        spacing=6)

    # Set the box to center
    main_menu.set_valign(Gtk.Align.CENTER)
