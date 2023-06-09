import turtle
import pandas

screen = turtle.Screen()
screen.title('Pakistan Province Game')
image = 'Pakistan.gif'
screen.addshape(image)
turtle.shape(image)

provinces = pandas.read_csv("provinces.csv")
all_prov = provinces.province.to_list()
answered_provinces = []

while len(answered_provinces) <= 6:
    ans = screen.textinput(title=f'{len(answered_provinces)}/5', prompt="What's another province's name?")
    if ans == 'Exit':
        break
    if ans in all_prov:
        answered_provinces.append(ans)
        prov = provinces[provinces.province == ans]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(prov.x), int(prov.y))
        t.write(ans.upper())



# used this to get coordinates of all provinces
# def location(x,y):
#     print(x,y)
#
# screen.onscreenclick(location)
#
# data = {
#     "province" : ["sindh","balochistan","punjab","kpk","gilgit","kashmir"],
#     'x' : ['53','-118','202','120','224','336'],
#     'y': ['-192', '-107', '25', '106', '218', '249']
# }
#
# new_data = pandas.DataFrame(data)
# new_data.to_csv("Provinces")

turtle.mainloop()