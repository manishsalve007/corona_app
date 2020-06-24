import requests
import bs4
import tkinter as tk
import plyer
#import datetime
import time
import threading 


def get_html_data(url) :
    data = requests.get(url)
    return data
def get_corona_details() :
    url = "https://www.mohfw.gov.in/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    div_info = bs.find("div", class_= "site-stats-count").find_all("li")

    all_data = ""


    for block in range(4):
        count = div_info[block].find("strong").get_text()
        text = div_info[block].find("span").get_text()

        #print(text + " : " + count)
        all_data = all_data + text + " : " + count + "\n"
    
    return all_data


def refresh():
    new_data = get_corona_details()
    print("Refreshing..")
    mainLabel['text'] = new_data
    return

def notify_me():
    while True:
        plyer.notification.notify(
            title = "Covid-19 cases in INDIA",
            message = get_corona_details(),
            timeout = 10,
            app_icon = 'corona.ico'
        )
        time.sleep(300)


#get_corona_details()

#creating gui

root = tk.Tk()
root.geometry("900x800")
root.title("Corona Stats")
root.configure(background = 'white')
f = ("", 35, "bold")
image = tk.PhotoImage(file = "corona.png")
bannerLabel = tk.Label(root, image = image)
bannerLabel.pack()

mainLabel = tk.Label(root, text = get_corona_details(), font = f, bg = 'white')
mainLabel.pack()

button = tk.Button(root, text = "REFRESH", font = f, relief = 'solid', command = refresh)
button.pack()

thread1 = threading.Thread(target = notify_me)
thread1.setDaemon(True)
thread1.start()




root.mainloop()