import random,time, secrets
import pyttsx3
import json,sys,argparse, emoji
engine = pyttsx3.init('sapi5')
engine.setProperty('gender', 'male')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
parser = argparse.ArgumentParser()
engine.say('we are analysing you. Please wait')
for voice in voices:
    engine.setProperty('voice', voice.id)
engine.setProperty('voice', voices[0])
engine.say('we are analysing you. Please wait')

parser.add_argument(
    '-n',
    '--name',
    required=False,
    action='store',
    help='please enter your name')
parser.add_argument(
    '-d',
    '--num',
    required=False,
    action='store',
    help='please enter your name')
args=parser.parse_args()
name=args.name
dob=args.num
team,facts,questions=[],[],[]
#print(emoji.emojize(":grinning_face_with_big_eyes:"))
with open('meta.json') as in_f:
    data1 = json.load(in_f)
    #print(data1.keys())
    team.append(data1['team']), facts.extend(data1["facts"]), questions.extend(data1["questions"])

#print(len(questions))
def generate_random_number(name=None, start=None,stop=None):
    start, stop = 0,5
    result = random.randint(start, stop)
    print('we are analysing you. Please wait') 
    engine.say('hmmmmmm. Analysis almost complete. Get ready to hear ')
    engine.runAndWait()
    time.sleep(3)
    print('analysing your brain to get you the right question')
    engine.say('analysing your brain to get you the right question')
    time.sleep(3)
    print('ahhhaa...got your mindset....finding the dark secrets of your life please wait')
    engine.say('ahhhaa...got your mindset....finding the dark secrets of your life please wait')
    time.sleep(3)
    engine.runAndWait()
    print('this is what THE WIZARD HARRY understood about you')
    engine.say('this is what THE WIZARD HARRY understood about you')
    time.sleep(3)
    print(secrets.choice(facts))
    # if name == 'sateesh':
    #     print('I got to know three of your major checkpoints in your life sateesh. Please feel free to share them along with your answer')
    # elif name == 'madhuri':
    #     print('looks like you are a walking web series. There is a lot that ')
    time.sleep(3)
    print('brace yourself and wait to answer')
    time.sleep(3)
    
    #print(result)
    return 'hey {} : here is the best I can ask -- {}'.format(name, questions[result])
selected = generate_random_number(name,start=0,stop=5)
print(selected)
import timer

