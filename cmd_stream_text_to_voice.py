import curses
from elevenlabs import generate, stream

def main(stdscr):
    buffer = ""
    stdscr.clear()
    stdscr.addstr("Start typing to generate and play voice using Eleven Labs. Press Esc to exit.\n")

    while True:
        c = stdscr.getch()
        if c == ord(' '):
            buffer += " "
            audio_stream = generate(
                text=buffer,
                voice="SzymonK voice",
                model="eleven_monolingual_v1",
                stream=True
            )
            stream(audio_stream)
            buffer = " "
            stdscr.addch(" ")
        elif c == 27:  # Escape key
            break
        else:
            buffer += chr(c)
            stdscr.addch(c)

curses.wrapper(main)

