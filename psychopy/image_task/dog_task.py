
'''

Dog image likeability task

11/30/18 mbod - initial setup and testing


1. setup psychopy modules
2. setup up logging
3. define window and image and text stimuli
4. make list of images to display from images folder
5. trial loop - for each image (stimulus) - 5 second trials
    a. draw stimuli
    b. flip screen
    c. get rating and log response
    

'''

# 1. setup modules

from psychopy import visual, core, event, logging
import os
import random


# 2. setup logging

LOG_DIR = 'logs'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

log_path = os.path.join(LOG_DIR,'dog_task_test.log')

logger = logging.LogFile(log_path, filemode='w')
logger.setLevel(logging.DEBUG)



# 3. define window and stimuli
win = visual.Window(monitor='testMonitor', fullscr=False, units='deg')

pictureStim = visual.ImageStim(win, pos=(0,3))
promptStim = visual.TextStim(win, text='How cute?', pos=(0,-2))
resp1 = visual.TextStim(win, text='1', pos=(-6,-3.5), height=0.8)
resp2 = visual.TextStim(win, text='2', pos=(-3,-3.5), height=0.8)
resp3 = visual.TextStim(win, text='3', pos=(0,-3.5), height=0.8)
resp4 = visual.TextStim(win, text='4', pos=(3,-3.5), height=0.8)
resp5 = visual.TextStim(win, text='5', pos=(6,-3.5), height=0.8)
anchor1 = visual.TextStim(win, text='pretty cute', pos=(-6,-4.5), height=0.7)
anchor5 = visual.TextStim(win, text='so darn cute!', pos=(6,-4.5), height=0.7)


resp_stim = [resp1, resp2, resp3, resp4, resp5]

stimuli = [pictureStim, promptStim, 
            resp1, resp2, resp3, resp4, resp5, anchor1, anchor5]


trial_clock = core.Clock()



# 4. list of images
images = [i for i in os.listdir('images') if i.endswith('.jpeg')]

# create a random order of images
random.shuffle(images)


# 5. TRIAL LOOP

for dog in images:

    # set the image in pictureStim to current stimulus
    pictureStim.setImage(os.path.join('images', dog))
    
    # reset color of resp stimuli
    for rs in [resp1, resp2, resp3, resp4, resp5]:
        rs.setColor('white')
    
    # reset trial clock
    trial_clock.reset()
    
    # display for 5 seconds and get rating
    
    made_resp = False
    
    while trial_clock.getTime() < 5.0:
        for stim in stimuli:
            stim.draw()
        
        win.flip()
        
        # get rating response
        resp = event.getKeys(keyList=['1','2','3','4','5'])
        
        if len(resp)>0 and not made_resp:
            
            made_resp = True
            
            resp_int = int(resp[0])-1
            resp_stim[resp_int].setColor('red')
 

# tidy up at the end
logging.flush()
win.close()
core.quit()