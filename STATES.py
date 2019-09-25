'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Elijah R McCutchan
StatesTk V1.0
'''


from tkinter import *
from tkinter import ttk

root=Tk()
root.title("50 States")

def clear():
    label.set("")

label=StringVar()

abbreviation=["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
states=["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho",
        "Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi",
        "Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio",
        "Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","SouthDakota","Tennessee","Texas","Utah","Vermont","Virginia",
        "Washington","West Virginia","Wisconsin","Wyoming"]
mainframe = Frame(root,borderwidth=0,height=1500,width=1500)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.anchor(CENTER)

def selection(event):
    temp_var = listbox.get(listbox.curselection())
    for value in states:
        if temp_var == value:
            temp_index = states.index(value)
            label.set(abbreviation[temp_index+1])

listbox = Listbox(mainframe,height=10,selectmode=SINGLE,listvariable=states)
listbox.bind('<<ListboxSelect>>',selection)

for value in states:
    listbox.insert(END, value)

listbox.grid(row=0,column=0)

B1 = Button(
    mainframe,command=clear,height=1,width=7,text="Clear"
    ).grid(column=2, row=1, padx=100, pady=0)

L1=Label(
    mainframe, textvariable=label
    ).grid(column=2, row=0)

root.mainloop()
