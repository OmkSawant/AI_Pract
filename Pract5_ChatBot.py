from tkinter import *

chat = Tk()
chat.title("ADMISSION")

def send():
    message = "You: " + e.get()
    txt.insert(END, message + "\n")  # Added \n for better formatting
    user = e.get().lower()

    if user in ["hello", "hi", "hii", "hiiii"]:
        txt.insert(END, "Bot: Welcome to MET\n 1) Branch Available\n 2) Fee Structure\n 3) Available Seats\n\n")

    elif user == "1":
        txt.insert(END, "Bot: Branches:\n 1) Computer Science\n 2) Information Technology\n 3) Artificial Intelligence\n 4) Mechanical\n 5) Civil\n\n")

    elif user == "2":
        txt.insert(END, "Bot: Fee Structure:\n Admission Fee: Rs.1200/-\n Sport Fee: Rs.1600/-\n Stationery Fee: Rs.2000/-\n Tuition Fee: Rs.80000/-\n\n")

    elif user == "3":
        txt.insert(END, "Bot: Available Seats:\n 1) Computer Science = 60\n 2) Information Technology = 30\n 3) Artificial Intelligence = 20\n 4) Mechanical = 50\n 5) Civil = 40\n\n")

    else:
        txt.insert(END, "Bot: Sorry, I didn't get you.\n\n")

    e.delete(0, END)  # Clear the entry after sending

# GUI Setup
txt = Text(chat, width=100, height=20)
txt.grid(row=0, column=0, columnspan=2)

e = Entry(chat, width=80)
e.grid(row=1, column=0)

send_button = Button(chat, text="Send", command=send)
send_button.grid(row=1, column=1)

chat.mainloop()
