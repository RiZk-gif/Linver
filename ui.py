import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk, Gdk
from system_info import get_system_info


DISTRO_ICONS = {
    "fedora": "fedora-logo-icon",
    "ubuntu": "ubuntu-logo-icon",
    "debian": "debian-logo",
    "arch": "archlinux",
    "opensuse": "opensuse-logo",
}


def create_distro_icon(distro_id):
    icon_name = DISTRO_ICONS.get(distro_id, "computer-symbolic")
    icon_theme = Gtk.IconTheme.get_for_display(Gdk.Display.get_default())

    if not icon_theme.has_icon(icon_name):
        icon_name = "computer-symbolic"

    icon = Gtk.Image.new_from_icon_name(icon_name)
    icon.set_pixel_size(52)
    icon.set_valign(Gtk.Align.CENTER)
    return icon


def create_window(app):
    info = get_system_info()

    window = Gtk.ApplicationWindow(
        application=app,
        title="Linver"
    )
    window.set_default_size(480, 520)
    window.set_resizable(False)

    main_box = Gtk.Box(
        orientation=Gtk.Orientation.VERTICAL,
        spacing=16
    )
    main_box.set_margin_top(28)
    main_box.set_margin_bottom(24)
    main_box.set_margin_start(28)
    main_box.set_margin_end(28)

    # Application heading
    app_title = Gtk.Label(label="Linver")
    app_title.add_css_class("app-title")
    app_title.set_halign(Gtk.Align.START)

    app_subtitle = Gtk.Label(label="Linux Version Information")
    app_subtitle.add_css_class("dim-label")
    app_subtitle.set_halign(Gtk.Align.START)

    main_box.append(app_title)
    main_box.append(app_subtitle)

    # Operating system identity: logo beside the OS name
    identity_box = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL,
        spacing=16
    )
    identity_box.set_margin_top(10)
    identity_box.set_valign(Gtk.Align.CENTER)

    identity_box.append(create_distro_icon(info["distro_id"]))

    identity_text = Gtk.Box(
        orientation=Gtk.Orientation.VERTICAL,
        spacing=6
    )
    identity_text.set_valign(Gtk.Align.CENTER)
    identity_text.set_hexpand(True)

    distro = Gtk.Label(label=info["distro"])
    distro.add_css_class("distro-title")
    distro.set_halign(Gtk.Align.START)
    distro.set_xalign(0)
    distro.set_wrap(True)

    description = Gtk.Label(
        label="A Linux distribution powered by the Linux kernel."
    )
    description.add_css_class("dim-label")
    description.add_css_class("description")
    description.set_halign(Gtk.Align.START)
    description.set_xalign(0)
    description.set_wrap(True)

    identity_text.append(distro)
    identity_text.append(description)
    identity_box.append(identity_text)
    main_box.append(identity_box)

    main_box.append(Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL))

    # System information
    section_title = Gtk.Label(label="System information")
    section_title.add_css_class("section-title")
    section_title.set_halign(Gtk.Align.START)
    main_box.append(section_title)

    grid = Gtk.Grid()
    grid.set_row_spacing(14)
    grid.set_column_spacing(20)
    grid.set_column_homogeneous(False)
    grid.set_hexpand(True)

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
        label_value.set_hexpand(True)
        label_value.set_selectable(True)
        label_value.set_ellipsize(3)

        grid.attach(label_name, 0, index, 1, 1)
        grid.attach(label_value, 1, index, 1, 1)

    main_box.append(grid)

    footer = Gtk.Label(label="Linver  ·  Version 0.1")
    footer.add_css_class("dim-label")
    footer.set_halign(Gtk.Align.START)
    footer.set_margin_top(4)
    main_box.append(footer)

    close_button = Gtk.Button(label="Close")
    close_button.set_halign(Gtk.Align.END)
    close_button.add_css_class("suggested-action")
    close_button.connect("clicked", lambda button: window.close())
    main_box.append(close_button)

    window.set_child(main_box)
    return window
