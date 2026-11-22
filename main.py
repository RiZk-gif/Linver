
import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk, Gdk
from pathlib import Path
from ui import create_window


def on_activate(app):
    css_path = Path(__file__).parent / "style.css"

    if css_path.exists():
        provider = Gtk.CssProvider()
        provider.load_from_path(str(css_path))

        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    window = create_window(app)
    window.present()


app = Gtk.Application(
    application_id="io.github.linver.App"
)

app.connect("activate", on_activate)
app.run()

