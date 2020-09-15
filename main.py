from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('weather.db')


def populate_list():
    weather_list.delete(0, END)
    for row in db.fetch():
        weather_list.insert(END, row)


def add_item():
    if code_text.get() == '' or city_text.get() == '' or temp_text.get() == '' or speed_text.get() == '' or date_text.get() == '' or wet_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(code_text.get(), city_text.get(), temp_text.get(), speed_text.get(), date_text.get(), wet_text.get())
    weather_list.delete(0, END)
    weather_list.insert(END, (code_text.get(), city_text.get(),
                            temp_text.get(), speed_text.get(), date_text.get(), wet_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = weather_list.curselection()[0]
        selected_item = weather_list.get(index)

        code_entry.delete(0, END)
        code_entry.insert(END, selected_item[1])
        city_entry.delete(0, END)
        city_entry.insert(END, selected_item[2])
        temp_entry.delete(0, END)
        temp_entry.insert(END, selected_item[3])
        speed_entry.delete(0, END)
        speed_entry.insert(END, selected_item[4])
        date_entry.delete(0,END)
        date_entry .insert(END, selected_item[5])
        wet_entry.delete(0, END)
        wet_entry.insert(END, selected_item[6])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], code_text.get(), city_text.get(),
              temp_text.get(), speed_text.get(), date_text.get(), wet_text.get())
    populate_list()


def clear_text():
    code_entry.delete(0, END)
    city_entry.delete(0, END)
    temp_entry.delete(0, END)
    speed_entry.delete(0, END)
    date_entry.delete(0,END)
    wet_entry.delete(0,END)


# Create window object
app = Tk()

# Code station
code_text = StringVar()
code_label = Label(app, text='Код станции', font=('bold', 14))
code_label.grid(row=0, column=0, sticky=W)
code_entry = Entry(app, textvariable=code_text)
code_entry.grid(row=0, column=1)
# city
city_text = StringVar()
city_label = Label(app, text='Місто', font=('bold', 14))
city_label.grid(row=0, column=2, sticky=W)
city_entry = Entry(app, textvariable=city_text)
city_entry.grid(row=0, column=3)
# avg temp
temp_text = StringVar()
temp_label = Label(app, text='Середня добова температура', font=('bold', 14))
temp_label.grid(row=1, column=0, sticky=W)
temp_entry = Entry(app, textvariable=temp_text)
temp_entry.grid(row=1, column=1)
# avg speed
speed_text = StringVar()
speed_label = Label(app, text='Середня швидкість вітру', font=('bold', 14))
speed_label.grid(row=1, column=2, sticky=W)
speed_entry = Entry(app, textvariable=speed_text)
speed_entry.grid(row=1, column=3)
# Date
date_text = StringVar()
date_label = Label(app, text='Дата', font=('bold', 14))
date_label.grid(row=2, column=0, sticky=W)
date_entry = Entry(app, textvariable=date_text)
date_entry.grid(row=2, column=1)
# Avg wet
wet_text = StringVar()
wet_label = Label(app, text='Відносна вологість', font=('bold', 14))
wet_label.grid(row=2, column=2, sticky=W)
wet_entry = Entry(app, textvariable=wet_text)
wet_entry.grid(row=2, column=3)
# Weather List (Listbox)
weather_list = Listbox(app, height=8, width=50, border=0)
weather_list.grid(row=4, column=0, columnspan=3, rowspan=8, pady=20, padx=20)
# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=4, column=3)
# Set scroll to listbox
weather_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=weather_list.yview)
# Bind select
weather_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Додати', width=12, command=add_item)
add_btn.grid(row=3, column=0, pady=20)

remove_btn = Button(app, text='Вилучити', width=12, command=remove_item)
remove_btn.grid(row=3, column=1)

"""update_btn = Button(app, text='Оновити', width=12, command=update_item)
update_btn.grid(row=3, column=2)"""

clear_btn = Button(app, text='Очистити ввід', width=12, command=clear_text)
clear_btn.grid(row=3, column=3)

app.title('Погода')
app.geometry('1000x900')

# Populate data
populate_list()

# Start program
app.mainloop()
