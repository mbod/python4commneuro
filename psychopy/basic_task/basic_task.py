

######################################
# Example of a simple PsychoPy3 task #
######################################

'''
Uses basic Python structures and idioms to create a 
text based task where positive and negative attributes 
are shown paired with a target
'''




# import specific psychopy submodules
from psychopy import visual, core, event, logging

import os

LOG_DIR = 'logs'

log_path = os.path.join(LOG_DIR, 'test_log.log')


if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    

words = ['happy', 'organized', 'sad', 'fun', 'unreliable']



# setup logging
logger = logging.LogFile(log_path, filemode='w')
logger.setLevel(logging.DEBUG)


# ----- define window and stimuli

win = visual.Window(monitor='testMonitor', fullscr=False, units='deg')

textStim = visual.TextStim(win, height=2)
respStim_y = visual.TextStim(win, text='yes', pos=(-5,-5))
respStim_n = visual.TextStim(win, text='no', pos=(5, -5))
condStim = visual.TextStim(win, text='CONDITION', pos=(0,6), height=1.8)


trial_clock = core.Clock()


for word in words:
    
    trial_clock.reset()
    
    #event.flush()  # clear out any unwanted key presses
    
    respStim_n.setColor('white')
    respStim_y.setColor('white')
    
    no_resp = True
    
    responses = []
    
    textStim.setText(word)
    logging.log('Set stim to: {}'.format(word), logging.DATA)

    while trial_clock.getTime() < 3.0:

        textStim.draw()
        respStim_y.draw()
        respStim_n.draw()
        condStim.draw()

        win.flip()
    
        resp = event.getKeys(keyList=['1','2'])
        
        if len(resp)>0 and no_resp:
            
            no_resp = False
            
            responses.append(resp[0])
            
            logging.log('RATING WAS {}'.format(resp), logging.DATA)
            
            if resp[0]=='1':
                respStim_y.setColor('red')
                
            if resp[0]=='2':
                respStim_n.setColor('red')
                
    logging.log('{} responses made: {}'.format(len(responses), responses), logging.DATA)


# tidy up at the end
logging.flush()
win.close()
core.quit()

