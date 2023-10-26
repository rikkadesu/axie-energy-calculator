import sys
import tkinter as tk
import os.path
from time import time

import processes
from processed_icons import Icons

_script = sys.argv[0]
_location = os.path.dirname(_script)

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40'  # X11 color: #666666
_ana1color = '#c3c3c3'  # Closest X11 color: 'gray76'
_ana2color = 'beige'  # X11 color: #f5f5dc
_tabfg1 = 'black'
_tabfg2 = 'black'
_tabbg1 = 'grey75'
_tabbg2 = 'grey89'
_bgmode = 'light'


class MainInterface:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""

        top.geometry("446x616+710+191")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("Axie Energy Counter")
        top.configure(background="#0080c0")
        self.top = top
        self.process = processes.Process()

        # Current Round
        self.round_label = tk.Label(self.top)
        self.round_label.place(relx=0.247, rely=0.032, height=41, width=234)
        self.round_label.configure(background="#0080c0")
        self.round_label.configure(compound='left')
        self.round_label.configure(disabledforeground="#a3a3a3")
        self.round_label.configure(font="-family {Comic Sans MS} -size 30 -weight bold")
        self.round_label.configure(foreground="#000000")
        self.round_label.configure(text='''Round 1''')
        self.round_label_tooltip = \
            ToolTip(self.round_label, '''Current round.''')

        # Enemy Energy Frame
        self.energy_labelframe = tk.LabelFrame(self.top)
        self.energy_labelframe.place(relx=0.291, rely=0.13, relheight=0.153, relwidth=0.399)
        self.energy_labelframe.configure(relief='ridge')
        self.energy_labelframe.configure(borderwidth="3")
        self.energy_labelframe.configure(font="-family {Comic Sans MS} -size 14 -weight bold")
        self.energy_labelframe.configure(foreground="#000000")
        self.energy_labelframe.configure(relief="ridge")
        self.energy_labelframe.configure(text='''Enemy Energy''')
        self.energy_labelframe.configure(background="#0080c0")

        # Enemy Energy Counter
        self.energy_label = tk.Label(self.energy_labelframe)
        self.energy_label.place(relx=0.084, rely=0.319, height=50, width=149, bordermode='ignore')
        self.energy_label.configure(background="#0080c0")
        self.energy_label.configure(compound='left')
        self.energy_label.configure(disabledforeground="#a3a3a3")
        self.energy_label.configure(font="-family {Comic Sans MS} -size 28 -weight bold")
        self.energy_label.configure(foreground="#ffffff")
        self.energy_label.configure(text='''0''')
        self.energy_label_tooltip = \
            ToolTip(self.energy_label, '''This is the enemy's predicted energy.''')

        # Energy Used
        self.energy_used_label = tk.Label(self.top)
        self.energy_used_label.place(relx=0.043, rely=0.292, height=51, width=408)
        self.energy_used_label.configure(background="#0080c0")
        self.energy_used_label.configure(compound='left')
        self.energy_used_label.configure(disabledforeground="#a3a3a3")
        self.energy_used_label.configure(font="-family {Comic Sans MS} -size 14 -weight bold")
        self.energy_used_label.configure(foreground="#000000")
        self.energy_used_label.configure(text='''Energy Used''')

        self.energy_used_counter = tk.Label(self.top)
        self.energy_used_counter.place(relx=0.408, rely=0.373, height=51, width=81)
        self.energy_used_counter.configure(background="#808000")
        self.energy_used_counter.configure(borderwidth="5")
        self.energy_used_counter.configure(compound='left')
        self.energy_used_counter.configure(disabledforeground="#a3a3a3")
        self.energy_used_counter.configure(font="-family {Comic Sans MS} -size 24")
        self.energy_used_counter.configure(foreground="#ffffff")
        self.energy_used_counter.configure(relief="raised")
        self.energy_used_counter.configure(text='''0''')
        self.energy_used_counter_tooltip = \
            ToolTip(self.energy_used_counter, '''Add or reduce: Energies used by your enemy.''')

        # Energy Gained
        self.energy_gained_label = tk.Label(self.top)
        self.energy_gained_label.place(relx=0.043, rely=0.471, height=51, width=408)
        self.energy_gained_label.configure(activebackground="#f9f9f9")
        self.energy_gained_label.configure(background="#0080c0")
        self.energy_gained_label.configure(compound='left')
        self.energy_gained_label.configure(disabledforeground="#a3a3a3")
        self.energy_gained_label.configure(font="-family {Comic Sans MS} -size 14 -weight bold")
        self.energy_gained_label.configure(foreground="#000000")
        self.energy_gained_label.configure(highlightbackground="#d9d9d9")
        self.energy_gained_label.configure(highlightcolor="black")
        self.energy_gained_label.configure(text='''Energy Gained''')

        self.energy_gained_counter = tk.Label(self.top)
        self.energy_gained_counter.place(relx=0.408, rely=0.552, height=51, width=81)
        self.energy_gained_counter.configure(activebackground="#f9f9f9")
        self.energy_gained_counter.configure(background="#808000")
        self.energy_gained_counter.configure(borderwidth="5")
        self.energy_gained_counter.configure(compound='left')
        self.energy_gained_counter.configure(disabledforeground="#a3a3a3")
        self.energy_gained_counter.configure(font="-family {Comic Sans MS} -size 24")
        self.energy_gained_counter.configure(foreground="#ffffff")
        self.energy_gained_counter.configure(highlightbackground="#d9d9d9")
        self.energy_gained_counter.configure(highlightcolor="black")
        self.energy_gained_counter.configure(relief="raised")
        self.energy_gained_counter.configure(text='''0''')
        self.energy_gained_counter_tooltip = \
            ToolTip(self.energy_gained_counter, '''Add or reduce: Energies gained by your enemy.''')

        # Energy Destroyed
        self.energy_destroyed_label = tk.Label(self.top)
        self.energy_destroyed_label.place(relx=0.043, rely=0.649, height=51, width=408)
        self.energy_destroyed_label.configure(activebackground="#f9f9f9")
        self.energy_destroyed_label.configure(background="#0080c0")
        self.energy_destroyed_label.configure(compound='left')
        self.energy_destroyed_label.configure(disabledforeground="#a3a3a3")
        self.energy_destroyed_label.configure(font="-family {Comic Sans MS} -size 14 -weight bold")
        self.energy_destroyed_label.configure(foreground="#000000")
        self.energy_destroyed_label.configure(highlightbackground="#d9d9d9")
        self.energy_destroyed_label.configure(highlightcolor="black")
        self.energy_destroyed_label.configure(text='''Energy Destroyed''')

        self.energy_destroyed_counter = tk.Label(self.top)
        self.energy_destroyed_counter.place(relx=0.408, rely=0.731, height=51, width=81)
        self.energy_destroyed_counter.configure(activebackground="#f9f9f9")
        self.energy_destroyed_counter.configure(background="#808000")
        self.energy_destroyed_counter.configure(borderwidth="5")
        self.energy_destroyed_counter.configure(compound='left')
        self.energy_destroyed_counter.configure(disabledforeground="#a3a3a3")
        self.energy_destroyed_counter.configure(font="-family {Comic Sans MS} -size 24")
        self.energy_destroyed_counter.configure(foreground="#ffffff")
        self.energy_destroyed_counter.configure(highlightbackground="#d9d9d9")
        self.energy_destroyed_counter.configure(highlightcolor="black")
        self.energy_destroyed_counter.configure(relief="raised")
        self.energy_destroyed_counter.configure(text='''0''')
        self.energy_destroyed_counter_tooltip = \
            ToolTip(self.energy_destroyed_counter, '''Add or reduce: Energies you destroyed from the enemy.''')

        # Next Turn Button
        self.next_turn_button = tk.Button(self.top)
        self.next_turn_button.place(relx=0.085, rely=0.86, height=44, width=387)
        self.next_turn_button.configure(activebackground="beige")
        self.next_turn_button.configure(activeforeground="black")
        self.next_turn_button.configure(background="#d9d9d9")
        self.next_turn_button.configure(borderwidth="3")
        self.next_turn_button.configure(compound='left')
        self.next_turn_button.configure(disabledforeground="#a3a3a3")
        self.next_turn_button.configure(font="-family {Comic Sans MS} -size 14 -weight bold")
        self.next_turn_button.configure(foreground="#000000")
        self.next_turn_button.configure(highlightbackground="#d9d9d9")
        self.next_turn_button.configure(highlightcolor="black")
        self.next_turn_button.configure(pady="0")
        self.next_turn_button.configure(text='''Next Turn''')
        self.next_turn_button_tooltip = \
            ToolTip(self.next_turn_button, '''Prepare for next turn.''')
        self.next_turn_button.configure(command=self.next_turn)

        # Last Turn Button
        self.last_turn_button = tk.Button(self.top)
        self.last_turn_button.place(relx=0.022, rely=0.016, height=24, width=77)
        self.last_turn_button.configure(activebackground="beige")
        self.last_turn_button.configure(activeforeground="black")
        self.last_turn_button.configure(background="#d9d9d9")
        self.last_turn_button.configure(borderwidth="3")
        self.last_turn_button.configure(compound='left')
        self.last_turn_button.configure(disabledforeground="#a3a3a3")
        self.last_turn_button.configure(font="-family {Comic Sans MS} -size 10")
        self.last_turn_button.configure(foreground="#000000")
        self.last_turn_button.configure(highlightbackground="#d9d9d9")
        self.last_turn_button.configure(highlightcolor="black")
        self.last_turn_button.configure(pady="0")
        self.last_turn_button.configure(text='''Last Turn''')
        self.last_turn_button_tooltip = \
            ToolTip(self.last_turn_button, '''Go back from previous round.''')
        self.last_turn_button.configure(command=self.last_turn)

        # Restart Button
        self.restart_button = tk.Button(self.top)
        self.restart_button.place(relx=0.818, rely=0.016, height=24, width=77)
        self.restart_button.configure(activebackground="beige")
        self.restart_button.configure(activeforeground="black")
        self.restart_button.configure(background="#d9d9d9")
        self.restart_button.configure(borderwidth="3")
        self.restart_button.configure(compound='left')
        self.restart_button.configure(disabledforeground="#a3a3a3")
        self.restart_button.configure(font="-family {Comic Sans MS} -size 10")
        self.restart_button.configure(foreground="#000000")
        self.restart_button.configure(highlightbackground="#d9d9d9")
        self.restart_button.configure(highlightcolor="black")
        self.restart_button.configure(pady="0")
        self.restart_button.configure(text='''Restart''')
        self.restart_button_tooltip = \
            ToolTip(self.restart_button, '''Restart counter.''')
        self.restart_button.configure(command=self.restart)

        # Energy Used - Increment and Decrement
        self.energy_used_plus_button = tk.Button(self.top)
        self.energy_used_plus_button.place(relx=0.612, rely=0.39, height=34, width=37)
        self.energy_used_plus_button.configure(activebackground="beige")
        self.energy_used_plus_button.configure(activeforeground="black")
        self.energy_used_plus_button.configure(background="#00ff00")
        self.energy_used_plus_button.configure(borderwidth="3")
        self.energy_used_plus_button.configure(compound='left')
        self.energy_used_plus_button.configure(disabledforeground="#a3a3a3")
        self.energy_used_plus_button.configure(font="-family {Comic Sans MS} -size 22")
        self.energy_used_plus_button.configure(foreground="#000000")
        self.energy_used_plus_button.configure(highlightbackground="#d9d9d9")
        self.energy_used_plus_button.configure(highlightcolor="black")
        self.energy_used_plus_button.configure(pady="0")
        self.energy_used_plus_button.configure(text='''+''')
        self.energy_used_plus_button.configure(command=self.add_energy_used)

        self.energy_used_minus_button = tk.Button(self.top)
        self.energy_used_minus_button.place(relx=0.303, rely=0.39, height=34, width=37)
        self.energy_used_minus_button.configure(activebackground="beige")
        self.energy_used_minus_button.configure(activeforeground="black")
        self.energy_used_minus_button.configure(background="#ff0000")
        self.energy_used_minus_button.configure(borderwidth="3")
        self.energy_used_minus_button.configure(compound='left')
        self.energy_used_minus_button.configure(disabledforeground="#a3a3a3")
        self.energy_used_minus_button.configure(font="-family {Comic Sans MS} -size 22")
        self.energy_used_minus_button.configure(foreground="#000000")
        self.energy_used_minus_button.configure(highlightbackground="#d9d9d9")
        self.energy_used_minus_button.configure(highlightcolor="black")
        self.energy_used_minus_button.configure(pady="0")
        self.energy_used_minus_button.configure(text='''-''')
        self.energy_used_minus_button.configure(command=self.subtract_energy_used)

        # Energy Gained - Increment and Decrement
        self.energy_gained_minus_button = tk.Button(self.top)
        self.energy_gained_minus_button.place(relx=0.303, rely=0.568, height=34, width=37)
        self.energy_gained_minus_button.configure(activebackground="beige")
        self.energy_gained_minus_button.configure(activeforeground="black")
        self.energy_gained_minus_button.configure(background="#ff0000")
        self.energy_gained_minus_button.configure(borderwidth="3")
        self.energy_gained_minus_button.configure(compound='left')
        self.energy_gained_minus_button.configure(disabledforeground="#a3a3a3")
        self.energy_gained_minus_button.configure(font="-family {Comic Sans MS} -size 22")
        self.energy_gained_minus_button.configure(foreground="#000000")
        self.energy_gained_minus_button.configure(highlightbackground="#d9d9d9")
        self.energy_gained_minus_button.configure(highlightcolor="black")
        self.energy_gained_minus_button.configure(pady="0")
        self.energy_gained_minus_button.configure(text='''-''')
        self.energy_gained_minus_button.configure(command=self.subtract_energy_gained)

        self.energy_gained_plus_button = tk.Button(self.top)
        self.energy_gained_plus_button.place(relx=0.612, rely=0.568, height=34, width=37)
        self.energy_gained_plus_button.configure(activebackground="beige")
        self.energy_gained_plus_button.configure(activeforeground="black")
        self.energy_gained_plus_button.configure(background="#00ff00")
        self.energy_gained_plus_button.configure(borderwidth="3")
        self.energy_gained_plus_button.configure(compound='left')
        self.energy_gained_plus_button.configure(disabledforeground="#a3a3a3")
        self.energy_gained_plus_button.configure(font="-family {Comic Sans MS} -size 22")
        self.energy_gained_plus_button.configure(foreground="#000000")
        self.energy_gained_plus_button.configure(highlightbackground="#d9d9d9")
        self.energy_gained_plus_button.configure(highlightcolor="black")
        self.energy_gained_plus_button.configure(pady="0")
        self.energy_gained_plus_button.configure(text='''+''')
        self.energy_gained_plus_button.configure(command=self.add_energy_gained)

        # Energy Destroyed - Increment and Decrement
        self.energy_destroyed_plus_button = tk.Button(self.top)
        self.energy_destroyed_plus_button.place(relx=0.612, rely=0.747, height=34, width=37)
        self.energy_destroyed_plus_button.configure(activebackground="beige")
        self.energy_destroyed_plus_button.configure(activeforeground="black")
        self.energy_destroyed_plus_button.configure(background="#00ff00")
        self.energy_destroyed_plus_button.configure(borderwidth="3")
        self.energy_destroyed_plus_button.configure(compound='left')
        self.energy_destroyed_plus_button.configure(disabledforeground="#a3a3a3")
        self.energy_destroyed_plus_button.configure(font="-family {Comic Sans MS} -size 22")
        self.energy_destroyed_plus_button.configure(foreground="#000000")
        self.energy_destroyed_plus_button.configure(highlightbackground="#d9d9d9")
        self.energy_destroyed_plus_button.configure(highlightcolor="black")
        self.energy_destroyed_plus_button.configure(pady="0")
        self.energy_destroyed_plus_button.configure(text='''+''')
        self.energy_destroyed_plus_button.configure(command=self.add_energy_destroyed)

        self.energy_destroyed_minus_button = tk.Button(self.top)
        self.energy_destroyed_minus_button.place(relx=0.303, rely=0.747, height=34, width=37)
        self.energy_destroyed_minus_button.configure(activebackground="beige")
        self.energy_destroyed_minus_button.configure(activeforeground="black")
        self.energy_destroyed_minus_button.configure(background="#ff0000")
        self.energy_destroyed_minus_button.configure(borderwidth="3")
        self.energy_destroyed_minus_button.configure(compound='left')
        self.energy_destroyed_minus_button.configure(disabledforeground="#a3a3a3")
        self.energy_destroyed_minus_button.configure(font="-family {Comic Sans MS} -size 22")
        self.energy_destroyed_minus_button.configure(foreground="#000000")
        self.energy_destroyed_minus_button.configure(highlightbackground="#d9d9d9")
        self.energy_destroyed_minus_button.configure(highlightcolor="black")
        self.energy_destroyed_minus_button.configure(pady="0")
        self.energy_destroyed_minus_button.configure(text='''-''')
        self.energy_destroyed_minus_button.configure(command=self.subtract_energy_destroyed)

        # Bloodmoon
        self.bloodmoon_label = tk.Label(self.top)
        self.bloodmoon_label.configure(anchor='s')
        self.bloodmoon_label.configure(background="#9b2424")
        self.bloodmoon_label.configure(borderwidth="3")
        self.bloodmoon_label.configure(compound='left')
        self.bloodmoon_label.configure(disabledforeground="#a3a3a3")
        self.bloodmoon_label.configure(font="-family {Comic Sans MS} -size 14")
        self.bloodmoon_label.configure(foreground="#ffffff")
        self.bloodmoon_label.configure(relief="solid")
        self.bloodmoon_label.configure(text=self.process.current_bloodmoon_damage,
                                       image=Icons.get_bloodmoon_icon_30x30(self), padx=5)
        self.bloodmoon_label_tooltip = ToolTip(self.bloodmoon_label, '''Bloodmoon Damage''')

        # Footer
        self.dev_footer = tk.Label(self.top)
        self.dev_footer.place(relx=0.022, rely=0.958, height=21, width=214)
        self.dev_footer.configure(anchor='w')
        self.dev_footer.configure(background="#0080c0")
        self.dev_footer.configure(compound='left')
        self.dev_footer.configure(disabledforeground="#a3a3a3")
        self.dev_footer.configure(foreground="#000000")
        self.dev_footer.configure(text='''rikkadesu ©2023''')
        self.dev_footer_tooltip = ToolTip(self.dev_footer, '''hi :3''')

        self.widgets = [self.top, self.round_label, self.energy_labelframe, self.energy_label, self.energy_used_label,
                        self.energy_gained_label, self.energy_destroyed_label, self.dev_footer]

        self.update_energy_main()

    def update_energy_main(self):
        self.energy_label.configure(text=self.process.current_energy)
        self.round_label.configure(text=self.process.current_round)
        self.start_bloodmoon() if self.process.round_counter > 9 else self.stop_bloodmoon()

    def add_energy_used(self):
        self.process.increment_energy_used()
        self.energy_used_counter.configure(text=self.process.energy_used)
        self.update_energy_main()

    def subtract_energy_used(self):
        self.process.decrement_energy_used()
        self.energy_used_counter.configure(text=self.process.energy_used)
        self.update_energy_main()

    def add_energy_gained(self):
        self.process.increment_energy_gained()
        self.energy_gained_counter.configure(text=self.process.energy_gained)
        self.update_energy_main()

    def subtract_energy_gained(self):
        self.process.decrement_energy_gained()
        self.energy_gained_counter.configure(text=self.process.energy_gained)
        self.update_energy_main()

    def add_energy_destroyed(self):
        self.process.increment_energy_destroyed()
        self.energy_destroyed_counter.configure(text=self.process.energy_destroyed)
        self.update_energy_main()

    def subtract_energy_destroyed(self):
        self.process.decrement_energy_destroyed()
        self.energy_destroyed_counter.configure(text=self.process.energy_destroyed)
        self.update_energy_main()

    def next_turn(self):
        self.process.go_next_turn()
        self.energy_used_counter.configure(text=self.process.energy_used)
        self.energy_gained_counter.configure(text=self.process.energy_gained)
        self.energy_destroyed_counter.configure(text=self.process.energy_destroyed)
        self.round_label.configure(text=self.process.current_round)
        self.update_energy_main()

    def last_turn(self):
        self.process.go_last_turn()
        self.update_energy_main()

    def restart(self):
        self.process.go_restart()
        self.update_energy_main()

    def start_bloodmoon(self):
        self.bloodmoon_label.place(relx=0.0, rely=0.211, height=41, width=80)
        self.bloodmoon_label.configure(text=self.process.current_bloodmoon_damage)
        for widget in self.widgets:
            widget.configure(bg="#c3063c")

    def stop_bloodmoon(self):
        self.bloodmoon_label.place_forget()
        for widget in self.widgets:
            widget.configure(bg="#0080c0")


class ToolTip(tk.Toplevel):
    """ Provides a ToolTip widget for Tkinter. """

    def __init__(self, wdgt, msg=None, msgFunc=None, delay=0.05,
                 follow=True):
        self.wdgt = wdgt
        self.parent = self.wdgt.master
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        self.withdraw()
        self.overrideredirect(True)
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        self.msg = tk.Message(self, textvariable=self.msgVar, bg=_bgcolor, fg=_fgcolor,
                              font="-family {Comic Sans MS} -size 10", aspect=1000)
        self.msg.grid()
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')

    def spawn(self, event=None):
        self.visible = 1
        self.after(int(self.delay * 1000), self.show)

    def show(self):
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()

    def move(self, event):
        self.lastMotion = time()
        if self.follow is False:
            self.withdraw()
            self.visible = 1
        self.geometry('+%i+%i' % (event.x_root + 20, event.y_root - 10))
        try:
            self.msgVar.set(self.msgFunc())
        except Exception:
            pass
        self.after(int(self.delay * 1000), self.show)

    def hide(self, event=None):
        self.visible = 0
        self.withdraw()

    def configure(self, **kwargs):
        background = '#d9d9d9'
        foreground = '#000000'
        backgroundset = False
        foregroundset = False
        # Get the current tooltip text just in case the user doesn't provide any.
        current_text = self.msgVar.get()
        # to clear the tooltip text, use the .update method
        if 'debug' in kwargs.keys():
            debug = kwargs.pop('debug', False)
            if debug:
                for key, value in kwargs.items():
                    print(f'key: {key} - value: {value}')
        if 'background' in kwargs.keys():
            background = kwargs.pop('background')
            backgroundset = True
        if 'bg' in kwargs.keys():
            background = kwargs.pop('bg')
            backgroundset = True
        if 'foreground' in kwargs.keys():
            foreground = kwargs.pop('foreground')
            foregroundset = True
        if 'fg' in kwargs.keys():
            foreground = kwargs.pop('fg')
            foregroundset = True

        fontd = kwargs.pop('font', None)
        if 'text' in kwargs.keys():
            text = kwargs.pop('text')
            if (text == '') or (text == "\n"):
                text = current_text
            else:
                self.msgVar.set(text)
        reliefd = kwargs.pop('relief', 'flat')
        justifyd = kwargs.pop('justify', 'left')
        padxd = kwargs.pop('padx', 1)
        padyd = kwargs.pop('pady', 1)
        borderwidthd = kwargs.pop('borderwidth', 2)
        wid = self.msg  # The message widget which is the actual tooltip
        if backgroundset:
            wid.config(bg=background)
        if foregroundset:
            wid.config(fg=foreground)
        wid.config(font=fontd)
        wid.config(borderwidth=borderwidthd)
        wid.config(relief=reliefd)
        wid.config(justify=justifyd)
        wid.config(padx=padxd)
        wid.config(pady=padyd)
#                   End of Class ToolTip


if __name__ == '__main__':
    main_window = tk.Tk()
    MainInterface(top=main_window)
    main_window.mainloop()
