import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Window:
    # Create a new GTK window
    main = Gtk.Window(title="Azla")
    main.set_default_size(200, 100)
    main.connect("destroy", Gtk.main_quit)
