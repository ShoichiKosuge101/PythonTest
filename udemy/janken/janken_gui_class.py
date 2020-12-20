import random
import tkinter as tk
from PIL import Image, ImageTk # pngの利用

GU, CHOKI, PA = 'グー','チョキ','パー'
hands = [GU,CHOKI,PA]
WIN,DRAW,LOSE = '勝ち','あいこ','負け'
rules={
    (0,0): DRAW, (0,1): WIN, (0,2): LOSE,
    (1,0): LOSE, (1,1): DRAW, (1,2): WIN,
    (2,0): WIN, (2,1): LOSE, (2,2): DRAW,
}

class View:
    
    def __init__(self):
        self.gu_image = Image.open('img/gu.png').convert('RGB').resize((100,100))
        self.gu_image = ImageTk.PhotoImage(self.gu_image)

        self.choki_image = Image.open('img/choki.png').convert('RGB').resize((100,100))
        self.choki_image = ImageTk.PhotoImage(self.choki_image)

        self.pa_image = Image.open('img/pa.png').convert('RGB').resize((100,100))
        self.pa_image = ImageTk.PhotoImage(self.pa_image)

        self.images=[self.gu_image, self.choki_image, self.pa_image]

        self.gu_label = tk.Label(root, image=self.gu_image)
        self.gu_label.place(x=20, y=200)

        self.choki_label = tk.Label(root, image=self.choki_image)
        self.choki_label.place(x=160, y=200)

        self.pa_label = tk.Label(root, image=self.pa_image)
        self.pa_label.place(x=300, y=200)

        self.gu_button = tk.Button(root, text='グー')
        self.gu_button.place(x=50, y=320)

        self.choki_button = tk.Button(root, text='チョキ')
        self.choki_button.place(x=190, y=320)

        self.pa_button =tk.Button(root, text='パー')
        self.pa_button.place(x=335, y=320)

        self.enemy_label = tk.Label(root, image = self.gu_image)
        self.enemy_label.place(x=160,y=20)

        self.text_label = tk.Label(root, text='最初はグー！じゃんけん！')
        self.text_label.place(x=140,y=140)

        self.retry_button = tk.Button(root, text='リトライ')
        

    def reset(self):
        self.retry_button.place_forget()
        self.gu_button['state'] = tk.ACTIVE
        self.choki_button['state'] = tk.ACTIVE
        self.pa_button['state'] = tk.ACTIVE       

        self.enemy_label.configure(image=self.images[0])
        self.text_label.configure(text='最初はグー！じゃんけん！')

    def display(self,enemy, result):
        self.enemy_label.configure(image=self.images[enemy])
        if result == DRAW:
            self.text_label.configure(text='あいこ')
        elif result == WIN:
            self.text_label.configure(text='勝ち')
        else:
            self.text_label.configure(text='負け')

    def show_retry(self):
        self.retry_button.place(x=185, y=360)
        self.gu_button['state'] = tk.DISABLED
        self.choki_button['state'] = tk.DISABLED
        self.pa_button['state'] = tk.DISABLED

class Application(tk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        master.geometry('420x400')
        master.title('じゃんけんゲーム')

        self.view = View()

        #def hoge():
        #   self.judge(0)

        self.view.gu_button['command'] = lambda: self.judge(0)
        self.view.choki_button['command'] = lambda: self.judge(1)
        self.view.pa_button['command'] = lambda: self.judge(2)

        self.view.retry_button['command'] = self.retry

    def judge(self, my_hand):
        enemy = random.randint(0,2)
        result = rules[(my_hand, enemy)]
        self.view.display(enemy, result)
        if result != DRAW:
            self.view.show_retry()

    def retry(self):
        self.view.reset()

root = tk.Tk()
app = Application(master=root)
app.mainloop()