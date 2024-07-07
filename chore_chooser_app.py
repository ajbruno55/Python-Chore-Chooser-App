import tkinter as tk
import random
from datetime import datetime
from pathlib import Path


class ChoreChooser():

    def __init__(self):

        # Defining specifications of the app
        self.root = tk.Tk()
        self.root.title("Chore Chooser")
        self.root.geometry("500x500+500+200")

        # Main screen widgets
        self.instructions_label = tk.Label(self.root,
                                text="Enter chores individually",
                                font=("Arial", 20, "underline"))
        self.main_label = tk.Label(self.root, text="Main chores:", font=("Arial", 16))
        self.side_label = tk.Label(self.root, text="Side chores:", font=("Arial", 16))
        # Button to check if default chore status should be set
        self.default_status = tk.IntVar()
        self.default_button= tk.Checkbutton(self.root, text="default",
                                             variable=self.default_status,
                                              onvalue=1, offvalue=0)
        # entries and buttons for user to enter main and side chores
        self.main_variable = tk.StringVar()
        self.side_variable = tk.StringVar()
        self.main_entry = tk.Entry(self.root, textvariable=self.main_variable)
        self.side_entry = tk.Entry(self.root, textvariable=self.side_variable)
        self.main_button = tk.Button(self.root, text="Enter", command=self.add_main_chores)
        self.side_button = tk.Button(self.root, text="Enter", command=self.add_side_chores)
        # Label that just says "Final Results"
        self.results_display = tk.Label(self.root, text="-- Final Results --", font=("Arial", 16))

        # Main button that will generate lists
        # And button to clear results/lists
        # And button to save results
        self.generate_button = tk.Button(self.root, text="Generate", command=self.choose_chore, height=2, width=15)
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_results, height=1, width=7)
        self.save_button = tk.Button(self.root, text="Save Results", command=self.save_results, height=2, width=10)


        # Empty lists to store and distribute chores
        self.main_chores = []
        self.side_chores = []
        self.alex_main = []
        self.alex_side = []
        self.laura_main = []
        self.laura_side = []


        # Defining grid layout
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=20)
        self.root.rowconfigure((0,1,2,3,4,5,6,7), weight=1)


        # Placing main screen widgets
        self.instructions_label.grid(row=0, column=0)
        self.main_label.grid(row=0, column=0, sticky="se")
        self.side_label.grid(row=1, column=0, sticky="ne")
        self.main_entry.grid(row=0, column=1, sticky="sw")
        self.side_entry.grid(row=1, column=1, sticky="nw")
        self.main_button.grid(row=0, column=1, sticky="se")
        self.side_button.grid(row=1, column=1, sticky="ne")
        self.default_button.grid(row=1, column=1, sticky='w')
        self.generate_button.grid(row=1, column=0, sticky='e')
        self.clear_button.grid(row=1, column=1, sticky='e')
        self.results_display.grid(row=2, column=0, sticky='se')
        self.save_button.grid(row=6, column=0, sticky='se')


        # Frame with relief to organize the chore distribution results
        self.frame = tk.Frame(self.root, height=150, width=300, borderwidth=2, relief=tk.RAISED)
        self.frame.place(x=75, y=235)


        # Setting active status to limit generate button clicks
        self.active = True

        # Start application
        self.root.mainloop()

    
    def add_main_chores(self):
        """defines button press and enters chores into main chore list
        for distribution"""
        chore = self.main_variable.get().strip()
        if chore not in self.main_chores:
            self.main_chores.append(chore)
        self.main_entry.delete(0, tk.END)

    def add_side_chores(self):
        """Same as above but adds to side chore list pre-distribution"""
        chore = self.side_variable.get().strip()
        if chore not in self.side_chores:
            self.side_chores.append(chore)
        self.side_entry.delete(0, tk.END)

    # This will be the generate button's main command function
    def choose_chore(self):
        """If default button clicked then defaults chores are added.
            Then chore lists are randomly shuffled then distributed to each 
            person's assignment"""
        
        if self.active:

            if self.default_status.get() == 1:
                self.main_chores.append("Kitchen")
                self.main_chores.append("Bathrooms")
                self.side_chores.append("Floors")
                self.side_chores.append("Toy Room")

            random.shuffle(self.main_chores)
            random.shuffle(self.side_chores)

            self.assign_chores(self.main_chores, self.laura_main, self.alex_main)
            self.assign_chores(self.side_chores, self.laura_side, self.alex_side)

            self.show_results()

            # Caps the generate button to only allow for once 
            # unless the clear button is pressed
            self.active = False
        

    def assign_chores(self, list1, list2, list3):
        """Algorithm to take in list items and separate them to each individual's assignment"""

        while list1:

            laura_pull = list1.pop()
            list2.append(laura_pull)

            if list1:
                alex_pull = list1.pop()
                list3.append(alex_pull)

    def show_results(self):
        """Labels to show final results from generate button press"""
        
        # Laura's results display
        laura_main_text = "Laura's main chore(s): " + ", ".join(self.laura_main)
        self.laura_main_results =tk.Label(self.frame, text=laura_main_text, font=("Arial", 16))
        laura_side_text = "Laura's side chore(s): " + ", ".join(self.laura_side)
        self.laura_side_results =tk.Label(self.frame, text=laura_side_text, font=("Arial", 16))
        self.laura_main_results.pack()
        self.laura_side_results.pack()

        # Alex's results display
        alex_main_text = "Alex's main chore(s): " + ", ".join(self.alex_main)
        self.alex_main_results =tk.Label(self.frame, text=alex_main_text, font=("Arial", 16))
        alex_side_text = "Alex's side chore(s): " + ", ".join(self.alex_side)
        self.alex_side_results =tk.Label(self.frame, text=alex_side_text, font=("Arial", 16))
        self.alex_main_results.pack()
        self.alex_side_results.pack()

    def clear_results(self):
        """Button to clear lists and clear results to allow recalculations"""

        # Empty all lists
        self.main_chores.clear()
        self.side_chores.clear()
        self.alex_main.clear()
        self.alex_side.clear()
        self.laura_main.clear()
        self.laura_side.clear()

        # Empty all results displays
        self.laura_main_results.destroy()
        self.laura_side_results.destroy()
        self.alex_main_results.destroy()
        self.alex_side_results.destroy()

        # Resetting active flag so that the generate button works again
        self.active = True

    def save_results(self):
        """Saves results in a separate text file to reference"""

        path = Path('/Users/alexbruno/Desktop/TKinter/chore_log.txt')

        with open(path, 'a') as f:
            dt = datetime.now()
            text = f"*{dt}*  |  Laura's: {", ".join(self.laura_main)}, {", ".join(self.laura_side)}. Alex's: {", ".join(self.alex_main)}, {", ".join(self.alex_side)}."
            f.write(text + '\n')

        

ChoreChooser()
