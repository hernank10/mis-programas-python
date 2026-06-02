import curses

def main(stdscr):
    curses.curs_set(0)  # Ocultar el cursor
    stdscr.clear()
    stdscr.addstr(0, 0, "Bienvenido a la aventura con curses!")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
