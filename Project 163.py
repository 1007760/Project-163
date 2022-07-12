from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x500")
root.title("Project 163")
q1_btn = StringVar(value = 0)
q1 = Label(root, text = "Do you experience shortness of breath during routine activities?")
q1.pack()
q1_r1 = Radiobutton(root, text = "Yes", variable = q1_btn, value = "Yes")
q1_r1.pack()
q1_r2 = Radiobutton(root, text = "No", variable = q1_btn, value = "No")
q1_r2.pack()

q2_btn = StringVar(value = 0)
q2 = Label(root, text = "Do you experience shortness of breath while at rest or lying down?")
q2.pack()
q2_r1 = Radiobutton(root, text = "Yes", variable = q2_btn, value = "Yes")
q2_r2 = Radiobutton(root, text = "No", variable = q2_btn, value = "No")
q2_r1.pack()
q2_r2.pack()

q3_btn = StringVar(value = 0)
q3 = Label(root, text = "Do you feel short of breath while lying flat and feel the need to stack multiple pillows to sleeps well?")
q3.pack()
q3_r1 = Radiobutton(root, text = "Yes", variable = q3_btn, value = "Yes")
q3_r1.pack()
q3_r2 = Radiobutton(root, text = "No", variable = q3_btn, value = "No")
q3_r2.pack()

q4_btn = StringVar(value = 0)
q4 = Label(root, text = "Do you experience persistent wheezing/coughing that produces white or pink tinged mucus?")
q4.pack()
q4_r1 = Radiobutton(root, text = "Yes", variable = q4_btn, value = "Yes")
q4_r1.pack()
q4_r2 = Radiobutton(root, text = "No", variable = q4_btn, value = "No")
q4_r2.pack()

q5_btn = StringVar(value = 0)
q5 = Label(root, text = "Do you have swelling in the feet/ankles/legs(shoes feel tighter) or abdomen?")
q5.pack()
q5_r1 = Radiobutton(root, text = "Yes", variable = q5_btn, value = "Yes")
q5_r2 = Radiobutton(root, text = "No", variable = q5_btn, value = "No")
q5_r1.pack()
q5_r2.pack()

q6_btn = StringVar(value = 0)
q6 = Label(root, text = "Do you feel tired while doing routine activities such as shopping, climbing stairs, carrying groceries or walking?")
q6.pack()
q6_r1 = Radiobutton(root, text = "Yes", variable = q6_btn, value = "Yes")
q6_r1.pack()
q6_r2 = Radiobutton(root, text = "No", variable = q6_btn, value = "No")
q6_r2.pack()

q7_btn = StringVar(value = 0)
q7 = Label(root, text = "Have you experieced loss of appetite(frequent feeling of being full) or nausea recently?")
q7.pack()
q7_r1 = Radiobutton(root, text = "Yes", variable = q7_btn, value = "Yes")
q7_r1.pack()
q7_r2 = Radiobutton(root, text = "No", variable = q7_btn, value = "No")
q7_r2.pack()

q8_btn = StringVar(value = 0)
q8 = Label(root, text = "Do you fell any of these symptoms - confusion, disorientation or loss of memory?")
q8.pack()
q8_r1 = Radiobutton(root, text = "Yes", variable = q8_btn, value = "No")
q8_r1.pack()
q8_r2 = Radiobutton(root, text = "No", variable = q8_btn, value = "No")
q8_r2.pack()

q9_btn = StringVar(value = 0)
q9 = Label(root, text = "Do you often feel that you are having a racing heartbeat and experience palpitations?")
q9.pack()
q9_r1 = Radiobutton(root, text = "Yes", variable = q9_btn, value = "Yes")
q9_r1.pack()
q9_r2 = Radiobutton(root, text = "No", variable = q9_btn, value = "No")
q9_r2.pack()

def calculate() :
    score = 0
    
    if q1_btn.get() == "Yes" :
        score = score + 10
        print(score)
    
    if q2_btn.get() == "Yes" :
        score = score + 10
        print(score)
        
    if q3_btn.get() == "Yes" :
        score = score + 10
        print(score)
        
    if q4_btn.get() == "Yes" :
        score = score + 10
        print(score)
        
    if q5_btn.get() == "Yes" :
        score = score + 10
        print(score)
        
    if q6_btn.get() == "Yes" :
        score = score + 10
        print(score)
        
    if q7_btn.get() == "Yes" :
        score = score + 10
        print(score)
        
    if q8_btn.get() == "Yes" :
        score = score + 10
        print(score)
        
    if q9_btn.get() == "Yes" :
        score = score + 10
        print(score)
        
    if score <= 10 :
        messagebox.showinfo("You don't need to visit a doctor.")
        
    elif score > 10 and score <= 30 :
        messagebox.showinfo("You might need to visit a doctor.")
    
    else :
        messagebox.showinfo("I strongly advise you to visit a doctor about your health.")

btn = Button(root, text = "Score", command = calculate)
btn.pack()
root.mainloop()