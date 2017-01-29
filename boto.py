"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json

# curse words that Botto will reject
curse_words=["fuck","shit","cunt","bitch","baby girl","mother fucking cocksucker","cock","fucking"]

#serves the HTML FIle-
@route('/', method='GET')
def index():
    return template("chatbot.html")

#handles the local host specifically the chat
@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    robot_answer=evaluate_robot_answer(user_message)
    return json.dumps(robot_answer)

#handler called from chat function
def evaluate_robot_answer(msg):


    #handle name
    if msg.find("name")!=-1:
        new_msg = msg.split()
        name = new_msg[-1]
        hello_name="hello "+name+" nice to meet you"
        greeting={"animation":"excited","msg":hello_name}
        return greeting


    if msg.find("gilad") != -1:
        result = {"animation": "inlove", "msg": "is that you"}
        return result

    if msg.find("scary") != -1:
        result = {"animation": "afraid", "msg": "I'm afraid!"}
        return result

    if msg.find("bored") != -1:
        result = {"animation": "bored", "msg": "I'm bored too"}
        return result

    if msg.find("confused") != -1:
        result = {"animation": "confused", "msg": "you confuse me"}
        return result

    if msg.find("heartbroken") != -1:
        result = {"animation": "heartbroken", "msg": "You broke my heart"}
        return result

    if msg.find("money") != -1:
        result = {"animation": "money", "msg": "CASH MONEY!!!!"}
        return result

    if msg.find("ok") != -1:
        result = {"animation": "ok", "msg": "ok"}
        return result

    if msg.find("space" or "nasa") != -1:
        result = {"animation": "takeoff", "msg": "To infinity and beyond"}
        return result

    if msg.find("funny") != -1:
        result = {"animation": "giggling", "msg": "You're so funny"}
        return result

    if msg.find("dancing") != -1:
        result = {"animation": "dancing", "msg": "let's dance :D"}
        return result

    #find all curse words
    if any(words in msg for words in curse_words):
        result="I don't respond to curse words"
        return result

    # default result
    result = {"animation": "no", "msg": "I don't understand..."}
    return result

#example for ajax
@route("/test", method='POST')
def chat():
    #returns the value from the msg key
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})

#connects the JS
@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')

#connect the CSS
@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')

#connect the images
@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
