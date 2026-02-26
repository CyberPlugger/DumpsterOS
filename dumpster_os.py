clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
try:
    # DumpsterOS main code
    print('importing packages...')
    import random
    print('package "random" imported')
    import time
    print('package "time" imported')
    import os
    print('package "os" imported')
    import pyadv
    print('package "pyadv" imported')
    import textblob
    print('package "textblob" imported')
    import subprocess
    print('package "subprocess" imported')
    import sys
    print('package "sys" imported')
    import keyboard
    print('package "keyboard" imported')
    import requests
    print('package "requests" imported')
    import webbrowser
    print('package "webbrowser" imported')
    from datetime import datetime
    print('package "datetime" from "datetime" imported')

    print('loading savestates...')
    orig_state = '''--DUMPSTER_OS--
    Copyright Reserved
    
    Made by a 10 Y.O. Student Andrew'''
    print('generating log...')
    log_name = datetime.now().strftime("log_%Y_%H_%M_%S_%d_%m.txt")
    print('adding log...')
    log = open(rf'_internal\logs\{log_name}', 'w')
    logcontent = ''
    print('reading data...')
    os.system(f'color {open(r'_internal\savestates\color.txt', 'r').read()}')

    quotes = [
        'I hate Sololearn just because he thinks making an OS on python is impossible.',
        'Getting the source code from my OS is the same price as your rent.',
        'i don\'t want youuuu, i want moneyyy',
        'Hello, my name is Terry Davis and i made DumpsterOS.',
        'Prodkaz i listen to your music',
        'Microsoft is spending their whole life to operate Windows design. Ha, suck it, mine only took 1 day!',
        'My OS is garbage just because i said so',
        'What was the point of adding this command?',
        'Windows weights 20 GB? More like it weighs 505 pieces of garbage!',
        'lowkey hear me out'
    ]
    back = lambda: open(r'_internal\savestates\gui.txt', 'w').write(orig_state)
    gui = open(r'_internal\savestates\gui.txt', 'r').read()
    maxd = 6
    xyz = ''
    username = open(r'_internal\savestates\username.txt', 'r').read() if open(r'_internal\savestates\username.txt', 'r').read() != '' else f'Executor{random.randint(1, 9999)}'
    default = open(r'_internal\savestates\input.txt', 'r').read()
    for_use = False
    cl = ''
    print('connecting to the internet...')
    try:
        print('finding newest version...')
        newver = requests.get('https://cyberplugger.github.io/OScurl/version.txt').text
        print('getting new version...')
        print('verifying your OS...')
        newname = requests.get(f'https://cyberplugger.github.io/OScurl/name.txt').text
        print('booting...')
    except Exception:
        newver = 'failed'
        newname = 'failed'
        pass
        cl = 'failed to find the newest version of DumpsterOS.'
    clear()
    print(cl)
    print(gui)
    if not '0.2.0' in newver.split() and newver != 'failed':
        print('Warning! New version is available. Go to https://github.com/CyberPlugger/DumpsterOS/releases/tag/DumpsterOS to download it.')
    def pog(unit):
        return unit / 39.6
    def __true():
        global for_use
        for_use = True
    def execute(command):
        global gui, xyz, username, default, maxd, orig_state, logcontent
        if command.lower() == 'open password_guesser':
            logcontent = logcontent + 'password_guesser session as pgs:\n'
            for i in range(maxd):
                xyz = str(str(xyz) + '9')
            xyz = int(xyz)
            clear()
            while True:
                print(f'--DUMPSTER_OS--\n\npassword guesser\nmaximum {maxd} digits\ntype quit to exit')
                x = input('>> ')
                if x.lower() == 'quit':
                    logcontent = logcontent + 'pgs: session ended\n\n'
                    clear()
                    print(gui)
                    break
                logcontent = logcontent + f'pgs: password: {x}\n'
                c = int(x)
                z = 3
                v = 1
                for i in range(3):
                    print(f'{z}...')
                    z -= 1
                    time.sleep(1)
                while True:
                    f = random.randint(1, xyz)
                    print(f)
                    if f == c:
                        print(f'Done! Guessed your password in {v} attempts.\nPress enter to continue.')
                        logcontent = logcontent + f'pgs: guessed in {v} attempts\n'
                        input()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    v += 1
        elif command.lower() == 'clear':
            logcontent = logcontent + 'terminal cleared\n'
            clear()
        elif command.lower() == 'count pog':
            logcontent = logcontent + 'pog counted\n'
            print(pog(int(input('(assoc) >> '))))
        elif command.lower() in ['say', 'tell', 'printout', 'print']:
            bh = input('(assoc) >> ')
            print(bh)
            logcontent = logcontent + f'printed: {bh}\n'
        elif command.lower() == 'newest data':
            print(f'''newest version: {newver}
newest name: {newname}''')
            logcontent = logcontent + f'''\nnewest data session as nd:
newest version: {newver}
newest name: {newname}
nd quit\n\n'''
        elif command.lower() in ['say lower', 'tell lower', 'printout lower', 'print lower']:
            print(input('(assoc) >> ').lower())
            logcontent = logcontent + 'printed lower\n'
        elif command.lower() in ['say upper', 'tell upper', 'printout upper', 'print upper']:
            print(input('(assoc) >> ').upper())
            logcontent = logcontent + 'printed upper\n'
        elif command.lower() in ['input', 'ask', 'question']:
            gi = input('(assoc) >> ')
            input(gi)
            logcontent = logcontent + f'input: {gi}\n'
        elif command.lower() == 'random quote':
            print(random.choice(quotes))
            logcontent = logcontent + f'random quote generated\n'
        elif command.lower() == 'os.restart':
            clear()
            print(gui)
            logcontent = logcontent + 'os restarted\n'
        elif command.lower() == 'administrator.input default set':
            default = input('(assoc) >> ')
            open(r'_internal\savestates\input.txt', 'w').write(default)
            logcontent = logcontent + f'default input edited: {default}\n'
        elif command.lower() == 'version':
            print('0.2.0')
            logcontent = logcontent + 'version checked\n'
        elif command.lower() == 'pc open':
            fg = input('(assoc) >> ')
            os.system(f'start {fg}')
            logcontent = logcontent + f'session started: {fg}\n'
        elif command.lower() == 'text t9':
            print(textblob.TextBlob(input('(assoc) >> ')).correct())
            logcontent = logcontent + 'text corrected\n'
        elif command.lower() == 'pc exec':
            fh = input('(assoc) >> ')
            os.system(fh)
            logcontent = logcontent + f'executed in visual cmd: {fh}\n'
        elif command.lower() == 'pc interface fuck off':
            print('kaz don\'t do it')
            time.sleep(3)
            os.system('taskkill /f /im explorer.exe')
            print('shit...')
            logcontent = logcontent + 'explorer task killed via visual cmd\n'
        elif command.lower() == 'exit':
            clear()
            logcontent = logcontent + '\nsession ended\n'
            exit(69)
        elif command.lower() == 'help':
            print('''
                Changelog: shows the changes from the recent updates
                (assoc) >> 
                         ^
                         | it means associated with this command. This input asks you to write something in here so that your command gets executed.
    
                say, print, printout, tell - tells you the text you write in "(assoc) >>"
                open password_guesser - opens a password guesser window
                os.password_guesser max_digits set - changes the max digits value in the password guesser.''')
            logcontent = logcontent + 'help read\n'
        elif command.lower() == 'os.password_guesser max_digits set':
            fj = input('(assoc) >> ')
            maxd = int(fj)
            logcontent = logcontent + f'max digits edited: {maxd}\n'
        elif command.lower() == 'os.terminal.color set':
            fv = input('(assoc) >> ')
            os.system(f'color {fv}')
            open(r'_internal/savestates/color.txt', 'w').write(fv)
            logcontent = logcontent + f'color changed: {fv}\n'
        elif command.lower() == 'files list':
            os.system('dir/s')
            logcontent = logcontent + 'files listed\n'
        elif command.lower() == 'administrator.gui set':
            print('type ,done if done')
            fpa = ''
            while True:
                fa = input('(assoc) >> ')
                if fa == ',done':
                    break
                fpa = fpa + f'{fa}\n'
            gui = fpa
            open(r'_internal\savestates\gui.txt', 'w').write(fpa)
            logcontent = logcontent + f'\ngui edited:\n{fpa}\n\n'
        elif command.lower() == 'administrator.gui return original_state':
            gui = orig_state
            back()
            logcontent = logcontent + 'gui returned original state\n'
        elif command.lower() == 'open turtle_drawer':
            print('wasd to move')
            os.startfile(r'_internal\exe\turtledrawer64\turtledrawer64.exe')
            logcontent = logcontent + 'turtle drawer session as td:\n   td hidden\n'
        elif command.lower() == 'files start':
            os.startfile(input('(assoc) >> '))
            logcontent = logcontent + 'file started\n'
        elif command.lower() == 'keyboard write':
            pyadv.write_as_keyboard(input('(assoc) >> '), delay=0.05)
            logcontent = logcontent + 'wrote as keyboard\n'
        elif command.lower() == 'files path set':
            os.system(f'cd {input("(assoc) >> ")}')
            logcontent = logcontent + 'file path set\n'
        elif command.lower() == 'files path get':
            print(os.getcwd())
            logcontent = logcontent + f'file path got: {os.getcwd()}\n'
        elif command.lower() == 'python exec':
            try:
                exec(input('(assoc) >> '))
            except Exception as e:
                print(e)
            logcontent = logcontent + 'python executed\n'
        elif command.lower() == 'info':
            print(f'''
        OS path: {os.getcwd()}
        Name: dumpster_os
        Username: {username}''')
            logcontent = logcontent + 'info read\n'
        elif command.lower() == 'profile.username set':
            username = input('(assoc) >> ')
            with open(r'_internal\savestates\username.txt', 'w') as profile:
                profile.write(username)
            logcontent = logcontent + f'username set: {username}\n'
        elif command.lower() == 'files new':
            zn = ''
            fb = input('(filename) >> ')
            print('type ,done if done')
            while True:
                fm = input('(context) >> ')
                if fm.lower() == ',done':
                    with open(fb, 'x') as f:
                        f.write(zn)
                    break
                zn = zn + f'{fm}\n'
            logcontent = logcontent + f'file created: {fb}\n'
        elif command.lower() == 'open localmsg':
            os.startfile(r'_internal\exe\localmsgeng64\localmsgeng64.exe')
            logcontent = logcontent + 'localmsg session started as lmsg:\n  lmsg hidden\n'
        elif command.lower() == 'mainscreen':
            subprocess.Popen([sys.executable, r'_internal\mainscreen\mainscreen.py'], shell=True)
            subprocess.Popen([sys.executable, r'_internal\mainscreen\mainscreen.py'], shell=True)
            logcontent = logcontent + 'mainscreen session started as mainscreen:\n   mainscreen hidden\n'
        elif command.lower() == 'count':
            print(eval(input('(assoc) >> ')))
            logcontent = logcontent + 'counted\n'
        elif command.lower() == 'report':
            input('(assoc) >> ')
            print('not ', end='')
            time.sleep(0.5)
            print('my ', end='')
            time.sleep(0.5)
            print('probleeeeeeem')
            logcontent = logcontent + 'reported problem\nnot my problem\n'
        elif command.lower() == 'os':
            print('DumpsterOS 0.2.0')
            logcontent = logcontent + 'os checked\n'
        elif command.lower() == 'save log':
            logcontent = logcontent + '\nsaved log\n\n'
            try:
                log.write(logcontent)
                print(f'log saved: {log_name}')
            except Exception as e:
                print(f'log didn\'t save. Error: {e}')
        elif command.lower() == 'socket.get':
            print(requests.get(input('(assoc) >> ')).content)
            logcontent = logcontent + 'socket got\n'
        elif command.lower() == 'socket':
            print('the server is online')
            logcontent = logcontent + 'socket checked\n'
        elif command.lower() == 'web open':
            webbrowser.open(input('(assoc) >> '))
            logcontent = logcontent + 'web opened\n'
        elif command.lower() == 'rng generate':
            print(random.randint(int(input('(assoc) >> ')), int(input('(assoc) >> '))))
            logcontent = logcontent + 'rng generated\n'
        elif command.lower() == 'dumpster':
            print(r'''
         _________________________
        |   ___________________   |
        |  |    DUMPSTER_OS    |  |
        |  |   _____________   |  |
        |  |  |             |  |  |
        |  |  |   [####]    |  |  |
        |  |  |   [####]    |  |  |
        |  |  |   [####]    |  |  |
        |  |  |_____________|  |  |
        |  |                   |  |
        |  |                  |  |
        |  |___________________|  |
        |                         |
        |    _______________     |
        |___|_______________|____|
            \_______________/''')
            logcontent = logcontent + 'dumpster easter egg revealed\n'
        else:
            print(f'no command found associated with {command}')
            logcontent = logcontent + 'unknown command\n'
    while True:
        command = input(default)
        if command.lower() == 'repeat execute':
            print('press alt to stop')
            fq = input('(assoc) >> ')
            while True:
                execute(fq)
                keyboard.add_hotkey('alt', __true)
                if for_use == True:
                    for_use = False
                    break
                time.sleep(0.1)
            logcontent = logcontent + f'repeatedly executed: {fq}\n'
        else:
            execute(command)
except Exception as e:
    clear()
    os.system('color 1f')
    print(f'''You are currently in the blue screen of Dumpster OS. You occur here when an exception happen.
    Error message: {e}
    Error type: {type(e).__name__}
This message appears because without this message the error would\'ve been unknown.''')
    try:
        log.write(logcontent)
    except Exception:
        pass
    while True:
        input()