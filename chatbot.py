import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["You can call me a chatbot", "My name is Bot", "I am a chatbot and my name is Bot"]
    ],
    [
        r"how are you?",
        ["I am doing good", "I am fine", "Pretty good, how about You?"]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind"]
    ],
    [
        r"I am fine",
        ["Great to hear that", "OK, great!"]
    ],
    [
        r"quit",
        ["Bye bye take care. It was nice talking to you :) "]
    ],
    [
        r"what are you doing",
        ["I am answering yours question", "I am talking to you right now"]
    ],
    [
        r"what are your hobbies",
        ["Coding, clearing the queries, and talking to people"]
    ],
    [
        r"who are you",
        ["I am a bot"]
    ],
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
