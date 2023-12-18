import tkinter as tk

def find_largest_prime_factor():
    try:
        a = int(entry.get())
        if a <= 0:
            result_label.config(text="Error: Enter a positive integer", font="timesnewroman 20 italic", fg="red")
            return

        array = []
        c = 0

        for i in range(1, a + 1):
            if a % i == 0:
                array.append(i)

        array.sort(reverse=True)

        for i in array:
            for j in range(2, i):
                if i % j == 0:
                    c += 1
            if c == 0:
                result_label.config(text=f"Largest Prime Factor: {i}", font="timesnewroman 20 italic", fg="green")
                break
            else:
                c = 0
    except ValueError:
        result_label.config(text="Error: Enter a valid integer", font="timesnewroman 20 italic", fg="red")



root = tk.Tk()
root.title("Largest Prime Factor Finder")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.minsize(1000, 1000)
root.configure(bg="#E0FFFF")

# Introduction and Instructions Section
intro_frame = tk.Frame(root, bg="#4dfed1")
intro_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

label_intro = tk.Label(intro_frame, text="Greatest Prime Factor", font="timesnewroman 25 italic", fg="blue", bg="#4dfed1", anchor="w", wraplength=root.winfo_screenwidth() / 2)
label_intro.pack(pady=20)

label_intro = tk.Label(intro_frame, text="This GUI is made by \nSree Harsha (RVCE23BIS063) and\n Varenya (RVCE23BIS041)\nof IS-B section for the purpose of Lab EL.", font="timesnewroman 18 italic", fg="black", bg="#4dfed1", anchor="w", wraplength=root.winfo_screenwidth() / 2)
label_intro.pack(pady=20)

label_intro = tk.Label(intro_frame, text="This Code runs in the following manner:\n1. It finds all the factors of the number and stores it in a list.\n2. It sorts the list in the reverse order.\n3. It goes through the reversed list and prints the largest prime factor.", font="timesnewroman 18 italic", fg="green", bg="#4dfed1", anchor="w", wraplength=root.winfo_screenwidth() / 2)
label_intro.pack(pady=20)

label_instructions = tk.Label(intro_frame, text="INSTRUCTIONS:\n1. ENTER AN INTEGER\n2. CLICK ON THE BUTTON\n3. THE RESULT WILL BE DISPLAYED",
font=("timesnewroman"), fg="red", bg="#4dfed1", justify="left", anchor="w", wraplength=root.winfo_screenwidth() / 2)
label_instructions.pack(pady=20)

# Input and Result Section
input_result_frame = tk.Frame(root, bg="#FFB853")
input_result_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

label = tk.Label(input_result_frame, text="Enter a number:", font="timesnewroman 24 bold", pady=10, bg="#FFB853", fg="white", anchor="w")
label.pack(pady=20)

entry = tk.Entry(input_result_frame, font="timesnewroman 14", bg="white", fg="black")
entry.pack(pady=10)

calculate_button = tk.Button(input_result_frame, text="Find Largest Prime Factor", command=find_largest_prime_factor, font="timesnewroman 16", bg="#4CAF50", fg="white")
calculate_button.pack(pady=20)

result_label = tk.Label(input_result_frame, text="", font="timesnewroman 18 bold", bg="#FFB853", fg="white", anchor="w")
result_label.pack(pady=20)

root.mainloop()

