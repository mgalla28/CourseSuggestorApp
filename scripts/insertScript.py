from pymongo import MongoClient

import tkinter as tk

master = tk.Tk()
tk.Label(master, text="designation").grid(row=0)
tk.Label(master, text="out_edges").grid(row=1)
tk.Label(master, text="credit_hours").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

def submit_class():
    print(e1.get(), e2.get(), e3.get())

    conn = MongoClient()
    db = conn.ClassGraphs
    coll = db.CsClasses
    coll.insert_one({
                 "designation": e1.get(),
                 "out_edges": e2.get(),
                 "credit_hours": e3.get()
                })



e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

tk.Button(master, text='Submit', command=submit_class).grid(row=3)

master.mainloop()
