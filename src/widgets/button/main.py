from src.main import Main
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Button:
    def __init__(self):
        pass
    # Create a button
    start = Gtk.Button(label="Start")
    exit = Gtk.Button(label="Exit")

    def start_clicked(button):
        options = Main.main_list()
        print(options)

    start.connect("clicked", start_clicked)
