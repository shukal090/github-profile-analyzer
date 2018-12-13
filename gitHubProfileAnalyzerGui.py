import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk as ttk
from tkinter.messagebox import showerror

class gitHubProfileAnalyzerGui:

    def __init__(self, Obj):
        self.gitGui = tk.Tk()
        self.gitGui.title("GitHub Profile Analyzer")

        inp = tk.Frame(master=self.gitGui, highlightbackground="black", highlightthickness=2)
        label_usr = tk.Label(master=inp, text="Enter the GitHub User Name").grid(row=0, column=0)
        self.entry_usr = tk.Entry(master=inp, width=36)
        self.entry_usr.grid(row=0, column=1)
        button_usr = tk.Button(master=inp, bg="Black", fg="white", width=10, bd=0, text="Git It", command=lambda:self.set_user(Obj)).grid(row=0, column=2)
        inp.pack()

        self.notebook = ttk.Notebook(master=self.gitGui, height=600)
        self.tab_basic = tk.Frame(master=self.notebook)
        self.tab_repos = tk.Frame(master=self.notebook)
        self.tab_starred = tk.Frame(master=self.notebook)
        self.tab_followers = tk.Frame(master=self.notebook)
        self.tab_following = tk.Frame(master=self.notebook)
        self.tab_repos = tk.Frame(master=self.notebook)
        self.tab_starred = tk.Frame(master=self.notebook)
        self.tab_lang = tk.Frame(master=self.notebook)

        self.notebook.add(self.tab_basic, text="Basic Info")
        self.notebook.add(self.tab_repos, text="Repositories")
        self.notebook.add(self.tab_starred, text="Starred")
        self.notebook.add(self.tab_followers, text="Followers")
        self.notebook.add(self.tab_following, text="Following")
        
        self.avt = ""   # avatar

        self.makeGui()
       
    def set_user(self, Obj):
        Obj.user_name = str(self.entry_usr.get())
        Obj.main(Obj=self)

    def user_info(self, login, iid, name, url, company, repos, followers, following, date,languages):
        info_frame = tk.Frame(master=self.tab_basic)
        tk.Label(master=info_frame, text="Username\t\t: "+login, anchor="w", width=50, padx=10, pady=10).grid(row=2, column=0)
        tk.Label(master=info_frame, text="ID\t\t\t: "+iid, anchor="w", width=50, padx=10, pady=10).grid(row=3, column=0)
        tk.Label(master=info_frame, text="Name\t\t\t: "+name, anchor="w", width=50, padx=10, pady=10).grid(row=4, column=0)
        tk.Label(master=info_frame, text="GitHub URL\t\t: "+url, font="Gabriola", anchor="w", width=50, padx=10, pady=10).grid(row=5, column=0)
        tk.Label(master=info_frame, text="Company\t\t: "+company, anchor="w", width=50, padx=10, pady=10).grid(row=6, column=0)
        tk.Label(master=info_frame, text="Public Repositories\t: "+repos, anchor="w", width=50, padx=10, pady=10).grid(row=7, column=0)
        tk.Label(master=info_frame, text="Followers\t\t: "+followers, anchor="w", width=50, padx=10, pady=10).grid(row=8, column=0)
        tk.Label(master=info_frame, text="Following\t\t: "+following, anchor="w", width=50, padx=10, pady=10).grid(row=9, column=0)
        tk.Label(master=info_frame, text="Contributing since\t: "+date, anchor="w", width=50, padx=10, pady=10).grid(row=11, column=0)
        lang_used = ""
        for lang in languages:
            lang_used += lang+" : "+str(languages[lang])+"\n"
        tk.Label(master=info_frame, text="Languages Used\t\t:\n"+lang_used,anchor="w", justify="left", width=50, padx=10, pady=10).grid(row=12, column=0)
        info_frame.grid(row=0,column=0)
        avt_frame = tk.Frame(master=self.tab_basic)
        avt = Image.open("avatar.jpg").resize((450,550))
        self.avt = ImageTk.PhotoImage(avt)
        tk.Label(master=avt_frame, image=self.avt).pack()
        avt_frame.grid(row=0, column=1)

    
    def user_followers(self, name, url, align):
        fr = tk.Frame(master=self.tab_followers, highlightbackground="black", highlightthickness=2)
        tk.Label(master=fr, text=name, font="Ravie", width=30, padx=10, pady=5).grid()
        tk.Label(master=fr, text="GitHub URL : "+url, font="Gabriola", padx=10, pady=5).grid()
        fr.grid(row=(int)(align/2), column=align%2)
    
    def user_following(self, name, url, align):
        fr = tk.Frame(master=self.tab_following, highlightbackground="black", highlightthickness=2)
        tk.Label(master=fr, text=name, font="Ravie", width=30, padx=10, pady=5).grid()
        tk.Label(master=fr, text="GitHub URL : "+url, font="Gabriola", padx=10, pady=5).grid()
        fr.grid(row=(int)(align/2), column=align%2)

    def user_repos(self, name, url, lang, stargazers, forks, align):
        fr = tk.Frame(master=self.tab_repos, highlightbackground="black", highlightthickness=2)
        tk.Label(master=fr, text=name, font="Ravie", width=30, padx=10, pady=5).grid()
        tk.Label(master=fr, text="URL : "+url, font="Gabriola", padx=10, pady=5).grid()
        tk.Label(master=fr, text="Language : "+lang, font="Century", width=20, padx=10, pady=5).grid()
        tk.Label(master=fr, text="Stargazers : "+stargazers, font="Century", width=20, padx=10, pady=5).grid()
        tk.Label(master=fr, text="Forks : "+forks, font="Century", width=20, padx=10, pady=5).grid()
        fr.grid(row=(int)(align/2), column=align%2)
    
    def user_starred(self, name, owner,url, align):
        fr = tk.Frame(master=self.tab_starred, highlightbackground="black", highlightthickness=2)
        tk.Label(master=fr, text=name, font="Ravie", width=30, padx=10, pady=5).grid()
        tk.Label(master=fr, text="Owner : "+owner, font="Constantia", width=30, padx=10, pady=5).grid()
        tk.Label(master=fr, text="URL : "+url, font="Gabriola", padx=10, pady=5).grid()
        fr.grid(row=(int)(align/2), column=align%2)

    def makeGui(self):
        self.notebook.pack()
        self.gitGui.mainloop()
    
    def error_msg(self, msg):
        showerror(title="GitHub Profile Analyzer", message=msg)
        self.gitGui.destroy()
    
    def destroy_children(self,tab_name):
        for child in tab_name.winfo_children():
            child.destroy()