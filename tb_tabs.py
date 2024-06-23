class Tab:
    url = None
    def __init__(self, url=None):
        self.url = url
        print("Tab created with URL:", url)

    def reload(self, hard=False):
        print("Reloading tab with URL:", self.url)

### VARIABLES ###
tabs = []
current_tab = None

quit_if_no_tabs = True

### SHORTCUTS ###
# Parameter: empty
def tab_new(parameter):
    global current_tab, tabs
    tabs.append(Tab(url=None))
    current_tab = len(tabs) - 1

# Parameter: "current", "next", "prev", "other" or "all"
def tab_close(parameter):
    global current_tab, tabs
    print("Close tab called with parameter:", parameter)
    if parameter == "next":
        tabs.pop(current_tab + 1)
    elif parameter == "prev":
        tabs.pop(current_tab - 1)
    elif parameter == "other":
        for i in range(len(tabs)):
            if i != current_tab:
                tabs.pop(i)
    elif parameter == "all":
        tabs.clear()
    else:
        tabs.pop(current_tab)

    # Check if current_tab is out of bounds
    if current_tab >= len(tabs):
        current_tab = len(tabs) - 1 # last tab
    # Check if all tabs are closed
    if len(tabs) == 0:
        if quit_if_no_tabs:
            exit()
        else:
            tab_new_with_url(None)
            current_tab = None

# Parameter: "hard", "all" or empty
def tab_reload(parameter):
    global current_tab, tabs
    if parameter == "hard":
        tabs[current_tab].reload(hard=True)
    elif parameter == "all":
        for tab in tabs:
            tab.reload(hard=False)
    else:
        tabs[current_tab].reload(hard=False)

    

### FUNCTIONS ###
# Not supposed to be used with shortcuts
def tab_new_with_url(url):
    global current_tab, tabs
    print("New tab called with URL:", url)
    tabs.append(Tab(url=url))
    current_tab = len(tabs) - 1

def get_tabs():
    return tabs

def get_tab_titles():
    global current_tab, tabs
    titles = []
    for tab in tabs:
        if tab.url:
            titles.append(tab.url)
        else:
            titles.append("None")
    return titles

def get_current_tab():
    global current_tab, tabs
    return tabs[current_tab]

def get_current_tab_index():
    global current_tab, tabs
    return current_tab