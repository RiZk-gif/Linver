
import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk, Gdk
from system_info import get_system_info


def create_window(app):
    info = get_system_info()

    window = Gtk.ApplicationWindow(
        application=app,
        title="Linver"
    )

    window.set_default_size(440, 440)
    window.set_resizable(False)

    main_box = Gtk.Box(
        orientation=Gtk.Orientation.VERTICAL,
        spacing=18
    )
    main_box.set_margin_top(24)
    main_box.set_margin_bottom(20)
    main_box.set_margin_start(24)
    main_box.set_margin_end(24)

    # Header
    title = Gtk.Label(label="Linver")
    title.add_css_class("title-1")

    subtitle = Gtk.Label(label="Linux Version Information")
    subtitle.add_css_class("dim-label")

    main_box.append(title)
    main_box.append(subtitle)

    # Fedora identity
    distro = Gtk.Label(label=info["distro"])
    distro.add_css_class("title-2")
    main_box.append(distro)

    # System information
    grid = Gtk.Grid()
    grid.set_row_spacing(12)
    grid.set_column_spacing(24)
    grid.set_margin_top(12)

    rows = [
        ("Version", info["version"]),
        ("Kernel", info["kernel"]),
        ("Architecture", info["architecture"]),
        ("Desktop", info["desktop_environment"]),
        ("Window Manager", info["window_manager"]),
        ("Display Server", info["display_server"]),
    ]

    for index, (name, value) in enumerate(rows):
        label_name = Gtk.Label(label=name)
        label_name.set_halign(Gtk.Align.START)
        label_name.add_css_class("dim-label")

        label_value = Gtk.Label(label=value)
        label_value.set_halign(Gtk.Align.END)
        label_value.set_selectable(True)

        grid.attach(label_name, 0, index, 1, 1)
        grid.attach(label_value, 1, index, 1, 1)

    main_box.append(grid)

    # Footer
    footer = Gtk.Label(label="Linver v0.1")
    footer.add_css_class("dim-label")

    main_box.append(footer)

    # Close button
    close_button = Gtk.Button(label="Close")
    close_button.set_halign(Gtk.Align.END)
    close_button.add_css_class("suggested-action")
    close_button.connect("clicked", lambda button: window.close())

    main_box.append(close_button)

    window.set_child(main_box)

    return window
