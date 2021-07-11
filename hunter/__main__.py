from .utils import *
import glob
from pathlib import Path
import traceback
import sys
import os

path = "hunter/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        try:
            load_plugins(plugin_name.replace(".py", ""))
            if not plugin_name.startswith("__") or plugin_name.startswith("_"):
                LOGS.info(f"Loaded ~ {plugin_name}")
        except Exception:
            LOGS.info(f"Error ~ {plugin_name}")
            LOGS.info(str(traceback.print_exc()))
            sys.exit(1)



print("\n                       Bot Working Now                        \n")

if __name__ == "__main__":
    bot.run_until_disconnected()
