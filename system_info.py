
import platform
import os


def read_os_release():
    data = {}

    try:
        with open("/etc/os-release", encoding="utf-8") as file:
            for line in file:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    data[key] = value.strip('"')
    except OSError:
        pass

    return data


def get_system_info():
    os_data = read_os_release()

    desktop = (
        os.environ.get("XDG_CURRENT_DESKTOP")
        or os.environ.get("XDG_SESSION_DESKTOP")
        or "Unknown"
    )

    if "HYPRLAND_INSTANCE_SIGNATURE" in os.environ:
        window_manager = "Hyprland"
    elif "hyprland" in desktop.lower():
        window_manager = "Hyprland"
    else:
        window_manager = "Unknown"

    display = (
        "Wayland" if os.environ.get("WAYLAND_DISPLAY")
        else "X11" if os.environ.get("DISPLAY")
        else "Unknown"
    )

    if "hyprland" in desktop.lower():
        desktop_environment = "Standalone WM"
    else:
        desktop_environment = desktop

    return {
        "distro": os_data.get("PRETTY_NAME", "Unknown"),
        "version": os_data.get("VERSION_ID", "Unknown"),
        "kernel": platform.release(),
        "architecture": platform.machine(),
        "desktop_environment": desktop_environment,
        "window_manager": window_manager,
        "display_server": display,
    }
