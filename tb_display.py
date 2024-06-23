from blessed import Terminal

term = Terminal()
menu = 0
"""
Title bar is always shown at the top.
Tabs are always shown at the top.

0 -> Home Screen
1 -> Search Bar
2 -> Web View
3 -> Developer Tools
"""
def draw_title_bar():
    with term.location(0, 0):
        print(term.black_on_white("Terminal Browser".center(term.width)))