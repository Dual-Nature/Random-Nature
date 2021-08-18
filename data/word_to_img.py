"""
code for converting words into image on the basis of their emotions.

 love     | courage | anger   |
 laughter | peace   | sorrow  |
 surprise | fear    | disgust |

"""

from PIL import Image, ImageDraw
import pandas as pd

def give_color(n):
    colors = [
        '#000', '#222', '#333', '#555', '#666', '#777', '#999', '#aaa', '#ccc', '#ddd', '#fff'
    ]
    print(n)
    return colors[int(n*10)]

def draw_img(data, i):
    img = Image.new('L', (300,300))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0,0,100,100), fill=give_color(data[0]))
    draw.rectangle((200,200,300,300), fill=give_color(data[1]))
    draw.rectangle((100,0,200,100), fill=give_color(data[2]))
    draw.rectangle((100,200,200,300), fill=give_color(data[3]))
    draw.rectangle((200,0,300,100), fill=give_color(data[4]))
    draw.rectangle((0,100,100,200), fill=give_color(data[5]))
    draw.rectangle((0,200,100,300), fill=give_color(data[6]))
    draw.rectangle((200,100,300,200), fill=give_color(data[7]))
    draw.rectangle((100,100,200,200), fill=give_color(data[8]))
    img.save('./images/img'+ str(i).rjust(5, '0')+ '.jpg')


data = pd.read_csv('./word_list.csv')
for i in range(len(data['words'].tolist())):
    row = data.iloc[i].tolist()[1:]    
    draw_img(row, i)