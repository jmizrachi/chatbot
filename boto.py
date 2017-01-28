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
    print(user_message)
    return json.dumps({"animation":"inlove","msg":robot_answer})

#handler called from chat function
def evaluate_robot_answer(msg):
    result = {"animation": "no", "msg": "I don't understand..."}
    if msg.find("gilad") != -1:
        result = {"animation": "inlove", "msg": "is that you"}
        return result

    #find all curse words
    if any(words in msg for words in curse_words):
        result="I don't respond to curse words"
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
