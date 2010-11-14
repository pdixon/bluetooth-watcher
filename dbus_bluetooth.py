import dbus

from dbus.mainloop.glib import DBusGMainLoop

DBusGMainLoop(set_as_default=True)

bus = dbus.SystemBus()

def default_adapter_path():
    """return the default bluetooth host adapters path."""
    return bus.get_object('org.bluez', '/').DefaultAdapter(dbus_interface='org.bluez.Manager')

def default_adapter():
    """return an interface to the default adapter."""
    return dbus.Interface(bus.get_object('org.bluez', default_adapter_path()),
            dbus_interface='org.bluez.Adapter')

def device(path):
    """return a device interface for the device at path."""
    return dbus.Interface(bus.get_object('org.bluez', path),
            dbus_interface='org.bluez.Device')

