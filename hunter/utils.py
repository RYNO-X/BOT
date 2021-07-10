from telethon import events
from . import *
import re
from .config import Config, XXX
from pathlib import Path
import inspect

def load_plugins(plugin_name):
    if plugin_name.startswith("__"):
        pass
    elif plugin_name.endswith("_"):
        import importlib
        from pathlib import Path

        path = Path(f"plugins/{plugin_name}.py")
        name = "plugins.{}".format(plugin_name)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    else:
        import importlib
        import sys
        from pathlib import Path
        path = Path(f"hunter/plugins/{plugin_name}.py")
        name = "hunter.plugins.{}".format(plugin_name)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.LOGS = LOGS
        mod.Config = Config
        spec.loader.exec_module(mod)
        if not plugin_name.startswith("_"):
            try:
                PLUGINS.append(plugin_name)
            except BaseException:
                if plugin_name not in PLUGINS:
                    PLUGINS.append(plugin_name)
                else:
                    pass

