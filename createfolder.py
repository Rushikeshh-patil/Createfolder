import os
import datetime

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

now = datetime.datetime.now()
#print(now)
def current_date_time():
        z = str(now)
        z = z[:10]
        return z
fn = current_date_time()
createFolder(f'./{fn} PLOTS/')
