import subprocess
import time

url1 = 'https://www.youtube.com/'
url2 = 'https://github.com/kirodotdev/spirit-of-kiro'


chrome_path = '/usr/bin/google-chrome'

subprocess.Popen(['wmctrl', '-s', '1'])

subprocess.Popen([chrome_path, '--new-windows', url1])
time.sleep(1.5)

subprocess.Popen(['wmctrl', '-s', '2'])
time.sleep(0.5)

subprocess.Popen([chrome_path, '--new-window', url2])


def check_for_windows(tag='none',timeout=10)
    
    if tag == 'none
        time.sleep(0.5)
        return False