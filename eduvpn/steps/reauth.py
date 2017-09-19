import logging
import gi
from gi.repository import Gtk
from eduvpn.steps.browser import browser_step
from eduvpn.manager import delete_provider

logger = logging.getLogger(__name__)


def reauth(meta, verifier, builder, window):
    """called when the authorization is expired"""
    logger.info("looks like authorization is expired or removed")
    dialog = Gtk.MessageDialog(window, Gtk.DialogFlags.MODAL, Gtk.MessageType.QUESTION,
                               Gtk.ButtonsType.YES_NO,
                               "Authorization for {}is expired or removed.".format(meta.display_name))
    dialog.format_secondary_text("Do you want to re-authorize?")
    response = dialog.run()
    if response == Gtk.ResponseType.YES:
        browser_step(builder, meta, verifier, window=window)
        delete_provider(meta.uuid)
    elif response == Gtk.ResponseType.NO:
        pass
    dialog.destroy()