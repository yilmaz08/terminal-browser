### MODULES ###
import argparse
import tb_display
import json
import readline

import tb_tabs as tabs
from tb_tabs import tab_new, tab_close, tab_reload


### CONSTANTS ###
VERSION = "Development"

### VARIABLES ###
startup_url = None # Opens home page with None
shortcut_cache = []
with open("shortcuts.json", "r") as json_file:
    keyboard_shortcuts = json.loads(str(json_file.read()))

### ARGUMENT PARSING ###
parser = argparse.ArgumentParser(
    prog="Terminal Browser",
    description="A TUI-based web browser",
    epilog="Developed by: Abdürrahim YILMAZ <ayilmaz08@proton.me>"
)

parser.add_argument("-V", "--version", action="version", version=f"%(prog)s {VERSION}")
parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
parser.add_argument("-u", "--url", help="URL to open on startup")
parser.add_argument("-t", "--theme", help="Path to the theme file")
parser.add_argument("-c", "--config", help="Path to the configuration file")

args = parser.parse_args()

### FUNCTIONS ###
def read_key():
    with tb_display.term.cbreak():
        inkey = tb_display.term.inkey(timeout=100)
        if not inkey: return None
        elif inkey.is_sequence: key = str(inkey.name)
        else: key = str(inkey)
    return key  
def process_input():
    key = read_key()
    if key.lower() == "q": exit()

    shortcut_cache.append(key)
    current_menu = keyboard_shortcuts.copy()

    print("Cache:", shortcut_cache)
    for key in shortcut_cache:
        if key not in current_menu: # Invalid key
            shortcut_cache.clear()
            break
        if type(current_menu[key]) == str: # Take action
            take_action(current_menu[key])
            shortcut_cache.clear()
            break
        current_menu = current_menu[key].copy() # Go deeper
def take_action(action):
    splitted = action.split("/")
    if len(splitted) == 1: parameter = None
    elif len(splitted) == 2: parameter = splitted[1]
    else: raise ValueError("More than one '/' in action string")

    try: globals()[splitted[0]](parameter) # Call the function
    except KeyError: print("Invalid function name")

### MAIN ###
if __name__ == "__main__":
    if args.url:
        startup_url = args.url
    if args.verbose:
        print("Verbose: Startup URL:", startup_url)
        print("Verbose: Theme File Loaded:", args.theme)
        print("Verbose: Configuration File Loaded:", args.config)

        print("Verbose: Press any key to continue...")
        read_key()

    with tb_display.term.fullscreen(), tb_display.term.hidden_cursor():
        tabs.tab_new_with_url(startup_url)
        while True:
            tb_display.draw_title_bar()
            print("Tabs:", tabs.get_tab_titles())
            process_input()