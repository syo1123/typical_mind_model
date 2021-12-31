import json

from flask import Flask, render_template, request


app = Flask(__name__)

tourist_number = None
current_place = None
num_int = 0
personal = None

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html", message = '')


@app.route("/main_building", methods=['POST', 'GET'])
def main_building():
    global tourist_number, current_place, personal
    current_place = "本館"
    if request.method == 'POST':
        if tourist_number is  None:
            personal = request.form.get('ceo-select')
        tourist_number=personal[num_int]
        if tourist_number =="1":
            text = "ここは本館です"
            return render_template("main_building.html", title = '本館', message = text, tourlist=tourist_number)
        elif tourist_number == "2":
            text = "ここは本館ですわ"
            return render_template("main_building.html", title = '本館', message = text, tourlist=tourist_number)
        elif tourist_number == "3":
            text = "ここは本館なんだな"
            return render_template("main_building.html", title = '本館', message = text, tourlist=tourist_number)
        elif tourist_number == "4":
            text = "ここは本館なのよ"
            return render_template("main_building.html", title = '本館', message = text, tourlist=tourist_number)
        else:
            return render_template("index.html")


@app.route("/building_1", methods=['POST', 'GET'])
def building_1():
    global current_place
    current_place = "一号館"
    if tourist_number == "1":
        text = "ここは一号館です"
        return render_template("building_1.html", title = '一号館', message = text, tourlist=tourist_number)
    elif tourist_number == "2":
        text = "ここは一号館ですわ"
        return render_template("building_1.html", title = '一号館', message = text, tourlist=tourist_number)
    elif tourist_number == "3":
        text = "ここは一号館なんだな"
        return render_template("building_1.html", title = '一号館', message = text, tourlist=tourist_number)
    elif tourist_number == "4":
        text = "ここは一号館なのよ"
        return render_template("building_1.html", title = '一号館', message = text, tourlist=tourist_number)
    else:
        return render_template("index.html")


@app.route("/building_2", methods=['POST', 'GET'])
def building_2():
    global current_place
    current_place = "二号館"
    if tourist_number == "1":
        text = "ここは二号館です"
        return render_template("building_2.html", title = '二号館', message = text, tourlist=tourist_number)
    elif tourist_number == "2":
        text = "ここは二号館ですわ"
        return render_template("building_2.html", title = '二号館', message = text, tourlist=tourist_number)
    elif tourist_number == "3":
        text = "ここは二号館なんだな"
        return render_template("building_2.html", title = '二号館', message = text, tourlist=tourist_number)
    elif tourist_number == "4":
        text = "ここは二号館なのよ"
        return render_template("building_2.html", title = '二号館', message = text, tourlist=tourist_number)
    else:
        return render_template("index.html")


@app.route("/building_3", methods=['POST', 'GET'])
def building_3():
    global current_place
    current_place = "三号館"
    if tourist_number == "1":
        text = "ここは三号館です"
        return render_template("building_3.html", title = '三号館', message = text, tourlist=tourist_number)
    elif tourist_number == "2":
        text = "ここは三号館ですわ"
        return render_template("building_3.html", title = '三号館', message = text, tourlist=tourist_number)
    elif tourist_number == "3":
        text = "ここは三号館なんだな"
        return render_template("building_3.html", title = '三号館', message = text, tourlist=tourist_number)
    elif tourist_number == "4":
        text = "ここは三号館なのよ"
        return render_template("building_3.html", title = '三号館', message = text, tourlist=tourist_number)
    else:
        return render_template("index.html")


@app.route("/library", methods=['POST', 'GET'])
def library():
    global current_place
    current_place = "図書館"
    if tourist_number == "1":
        text = "ここは図書館です"
        return render_template("library.html", title = '図書館', message = text, tourlist=tourist_number)
    elif tourist_number == "2":
        text = "ここは図書館ですわ"
        return render_template("library.html", title = '図書館', message = text, tourlist=tourist_number)
    elif tourist_number == "3":
        text = "ここは図書館なんだな"
        return render_template("library.html", title = '図書館', message = text, tourlist=tourist_number)
    elif tourist_number == "4":
        text = "ここは図書館なのよ"
        return render_template("library.html", title = '図書館', message = text, tourlist=tourist_number)
    else:
        return render_template("index.html")


@app.route("/final", methods=['POST', 'GET'])
def final():
    global current_place
    current_place = "最終広場"
    if tourist_number == "1":
        text = "ツアーに参加して頂きありがとうございました。フォームの次のページに進み、アンケートにお答えください"
        return render_template("final.html", title = '最終広場', message = text, tourlist=tourist_number)
    elif tourist_number == "2":
        text = "ツアーに参加して頂き、ありがとうですわ"
        return render_template("final.html", title = '最終広場', message = text, tourlist=tourist_number)
    elif tourist_number == "3":
        text = "ツアーに参加して頂き、ありがとうなんだな"
        return render_template("final.html", title = '最終広場', message = text, tourlist=tourist_number)
    elif tourist_number == "4":
        text = "ツアーに参加して頂き、ありがとうなのよ"
        return render_template("final.html", title = '最終広場', message = text, tourlist=tourist_number)
    else:
        return render_template("index.html")


@app.route("/text_return", methods=['POST', 'GET'])
def text_return():
    if request.method == 'POST':
        emotion = request.form.get('emotion')
        json_file = open('./app/data/data.json', 'r')
        json_object = json.load(json_file)
        text = json_object[tourist_number][current_place][emotion]
        if current_place == "本館":
            return render_template("main_building.html", title = '本館', message = text, triger="on", tourlist=tourist_number)
        elif current_place == "一号館":
            return render_template("building_1.html", title = '一号館', message = text, triger="on", tourlist=tourist_number)
        elif current_place == "二号館":
            return render_template("building_2.html", title = '二号館', message = text, triger="on", tourlist=tourist_number)
        elif current_place == "三号館":
            return render_template("building_3.html", title = '三号館', message = text, triger="on", tourlist=tourist_number)
        elif current_place == "図書館":
            return render_template("library.html", title = '図書館', message = text, triger="on", tourlist=tourist_number)
        else:
            return render_template("index.html")


@app.route("/turn_opening")
def turn_opening():
    global tourist_number, current_place, num_int
    current_place = None
    num_int += 1
    return render_template("index_second.html")


if __name__ == "__main__":
    app.run(debug=True)
