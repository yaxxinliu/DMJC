#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.01), November 26, 2015, at 16:22
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
  
The script was edited by Eugenia Barkova.  
"""

######### Import relevant libraries #################################
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui, hardware
from psychopy.constants import *  # things like STARTED, FINISHED
import scipy.stats as ss
import time
import numpy as np
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'novelty'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if not dlg.OK: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

if not os.path.exists(_thisDir + os.sep + 'data' + os.sep + expInfo['participant']):
    os.makedirs(_thisDir + os.sep + 'data/' + expInfo['participant'])

# Data file name stem = absolute path + name; later add .psyexp, , .log, etc
filename_scene_fam = _thisDir + os.sep + u'data/%s/%s_%s_scene_fam_%s' % (
    expInfo['participant'], expInfo['participant'], expName, expInfo['date'])
filename_training = _thisDir + os.sep + u'data/%s/%s_%s_training_%s' % (
    expInfo['participant'], expInfo['participant'], expName, expInfo['date'])
filename_test = _thisDir + os.sep + u'data/%s/%s_%s_test_%s' % (
    expInfo['participant'], expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath=u'/Users/labuser/Documents/Eugenia/attachments/',
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename_scene_fam)
# save a log file for detail verbose info
logFile = logging.LogFile(filename_scene_fam + '.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
# size=(1920, 1080), fullscr=True
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
                    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
                    blendMode='avg', useFBO=True,
                    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] is not None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # couldn't get a reliable measure so guess

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# --------------------------------------------------------------------
# Start of instructions for scene familiriazation, to move forward
# use 'space'
#  -------------------------------------------------------------------

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
### visual component to hold slides from the power point with instruction
scene_instructions = visual.ImageStim(win=win, name='scene_instructions',
                                      image='sin', mask=None,
                                      ori=0, pos=[0, 0], size=[1.8, 2],
                                      color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                      flipHoriz=False, flipVert=False,
                                      texRes=128, interpolate=True, depth=0.0)

# -------Start Routine "Instructions"-------
instructions = data.TrialHandler(nReps=1, method='sequential',
                                 extraInfo=expInfo, originPath=u'/Users/labuser/Documents/Eugenia/attachments/',
                                 trialList=data.importConditions("scene/instructions.xlsx"),
                                 seed=None, name='Instructions')

# thisExp.addLoop(instructions)  # add the loop to the experiment. If uncommented, the instructions will appear in
# output file
thisInstruction = instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisScene_familarization.rgb)
if thisInstruction is not None:
    for paramName in thisInstruction.keys():
        exec (paramName + '= thisInstruction.' + paramName)

# loop through slides in the instructions power point
for thisInstruction in instructions:
    currentLoop = instructions
    # abbreviate parameter names if possible (e.g. rgb = thisScene_familarization.rgb)
    if thisInstruction is not None:
        for paramName in thisInstruction.keys():
            exec (paramName + '= thisInstruction.' + paramName)

    # ------Prepare to start Routine "Instructions"-------
    t = 0
    InstructionsClock.reset()  # clock 
    frameN = -1
    routineTimer.add(900.000000)  # set an arbitrary big timer, so that subjects have time to read instruction

    # add a key response to track if subject pressed 'space' to move on to the next slide
    confirm_instr = event.BuilderKeyResponse()
    confirm_instr.status = NOT_STARTED
    # update slide --------------------------
    if inst_scenes == None:
        # if end of the file - end routine
        break
    scene_instructions.setImage("images/" + inst_scenes)
    # ----------------------------------------
    # keep track of which components have finished
    InstructionsComponents = [scene_instructions, confirm_instr]
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "Instructions"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = InstructionsClock.getTime()
        frameN += 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # instruction slide updates 
        if t >= 0.0 and scene_instructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            scene_instructions.tStart = t  # underestimates by a little under one frame
            scene_instructions.frameNStart = frameN  # exact frame index
            scene_instructions.setAutoDraw(True)
        if scene_instructions.status == STARTED and t >= (
                    0.0 + (900.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            scene_instructions.setAutoDraw(False)

        # *confirm_instr* updates
        if t >= 0.0 and confirm_instr.status == NOT_STARTED:
            # keep track of start time/frame for later
            confirm_instr.tStart = t  # underestimates by a little under one frame
            confirm_instr.frameNStart = frameN  # exact frame index
            confirm_instr.status = STARTED
            event.clearEvents(eventType='keyboard')
        if confirm_instr.status == STARTED and t >= (
                    0.0 + (900.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            confirm_instr.status = STOPPED
        # track 'space'
        if confirm_instr.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # space was pressed
                # move on to next slide
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine i.e. a space was pressed
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or len(event.getKeys(keyList=["escape", "a"])) == 2:
            core.quit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# ------------------------------------------------------------------------------------------------------------
# Instructions ended -> move on to the scene familiarization task called "scenes"
# -----------------------------------------------------------------------------------------------------------


# Initialize components for Routine "scenes"
scenesClock = core.Clock()
# Visual component to hold scene 
scene_image = visual.ImageStim(win=win, name='image',
                               image='sin', mask=None,
                               ori=0, pos=[0, 0], size=1.5,
                               color=[1, 1, 1], colorSpace='rgb', opacity=1,
                               flipHoriz=False, flipVert=False,
                               texRes=128, interpolate=True, depth=0.0)
# Fixation point
fix = visual.TextStim(win=win, ori=0, name='fix',
                      text=u'+', font=u'Arial',
                      pos=[0, 0], height=0.1, wrapWidth=None,
                      color=u'black', colorSpace='rgb', opacity=1,
                      depth=-1.0)
# Text components hold indoor/outdoor choice
indoors = visual.TextStim(win=win, ori=0, name='indoors',
                          text=u'INDOORS', font=u'Arial',
                          pos=[-0.25, -0.85], height=0.1, wrapWidth=None,
                          color=u'white', colorSpace='rgb', opacity=1,
                          depth=-2.0)
outdoors = visual.TextStim(win=win, ori=0, name='outdoors',
                           text=u'OUTDOORS', font=u'Arial',
                           pos=[0.25, -0.85], height=0.1, wrapWidth=None,
                           color=u'white', colorSpace='rgb', opacity=1,
                           depth=-3.0)

# set up handler to look after randomisation of conditions etc
# scenes were pre-randomized for eachparticipantt -> update filename according to subject number
filename = u'scene/scene_fam_' + str(expInfo['participant']) + '.csv'
# create a handler that loops through the file selecting each scene sequentially 
scene_familarization = data.TrialHandler(nReps=1, method='sequential',
                                         extraInfo=expInfo, originPath=u'/Users/labuser/Documents/Eugenia/attachments/',
                                         trialList=data.importConditions(filename),
                                         seed=None, name='scene_familarization')
thisExp.addLoop(scene_familarization)  # add the loop to the experiment
thisScene_familarization = scene_familarization.trialList[0]  # initialize stimuli
# abbreviate parameter names if possible (e.g. rgb=thisScene_familarization.rgb)
if thisScene_familarization != None:
    for paramName in thisScene_familarization.keys():
        exec (paramName + '= thisScene_familarization.' + paramName)

# ##############################################################
# Ashkan: Add a screen that says "Get Ready for Scene Task \n Press Space Bar to Start"
# #############################################################
instructions = visual.TextStim(win=win, ori=0, name='outdoors',
                           text=u'OUTDOORS', font=u'Arial',
                           pos=[0, 0], height=0.1, wrapWidth=None,
                           color=u'white', colorSpace='rgb', opacity=1,
                           depth=0)
instructions.setText("Get Ready for Scene Task \n Press Space Bar to Start")
instructions.draw()
win.flip()
while True:
    time.sleep(1)  # Reduces amount of resources used
    if event.getKeys(keyList=['esc', 'escape']):
        core.quit()
    elif event.getKeys(keyList=['space']):
        break


# loop through the scenes 
for thisScene_familarization in scene_familarization:
    currentLoop = scene_familarization
    # abbreviate parameter names if possible (e.g. rgb = thisScene_familarization.rgb)
    if thisScene_familarization is not None:
        for paramName in thisScene_familarization.keys():
            exec (paramName + '= thisScene_familarization.' + paramName)

    # ------Prepare to start Routine "scenes"-------
    t = 0
    scenesClock.reset()  # clock 
    frameN = -1
    routineTimer.add(3.000000)  # each trial at this stage is 3 sec long
    # update component parameters for each repeat
    scene_image.setImage("images/" + scene)
    in_out_key = event.BuilderKeyResponse()  # add key response to record subject's choice
    in_out_key.status = NOT_STARTED
    # keep track of which components have finished
    scenesComponents = [scene_image, fix, indoors, outdoors, in_out_key]
    # reset color of indoor/outdoor in the beginning of each trial
    indoors.color = 'white'
    outdoors.color = 'white'
    for thisComponent in scenesComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "scenes"-------
    continueRoutine = True
    # loop for each frame
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = scenesClock.getTime()
        frameN += 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *image* updates
        if t >= 1 and scene_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            scene_image.tStart = t  # underestimates by a little under one frame
            scene_image.frameNStart = frameN  # exact frame index
            scene_image.setAutoDraw(True)
        # these lines in each component take care of the time of each of the component on the screen
        # once it's timer is almost done, we stop drawing it on every frame
        if scene_image.status == STARTED and t >= (
                    1 + (2 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            scene_image.setAutoDraw(False)

        # *fix* updates
        if t >= 0.5 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t  # underestimates by a little under one frame
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        if fix.status == STARTED and t >= (
                    0.5 + (0.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            fix.setAutoDraw(False)

        # *indoors* updates
        if t >= 1.0 and indoors.status == NOT_STARTED:
            # keep track of start time/frame for later
            indoors.tStart = t  # underestimates by a little under one frame
            indoors.frameNStart = frameN  # exact frame index
            indoors.setAutoDraw(True)
        if indoors.status == STARTED and t >= (
                    1.0 + (2.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            indoors.setAutoDraw(False)

        # *outdoors* updates
        if t >= 1.0 and outdoors.status == NOT_STARTED:
            # keep track of start time/frame for later
            outdoors.tStart = t  # underestimates by a little under one frame
            outdoors.frameNStart = frameN  # exact frame index
            outdoors.setAutoDraw(True)
        if outdoors.status == STARTED and t >= (
                    1.0 + (2.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            outdoors.setAutoDraw(False)

        # *in_out_key* updates
        if t >= 1.5 and in_out_key.status == NOT_STARTED:
            # keep track of start time/frame for later
            in_out_key.tStart = t  # underestimates by a little under one frame
            in_out_key.frameNStart = frameN  # exact frame index
            in_out_key.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(in_out_key.clock.reset)  # t=0 on next screen flip
        if in_out_key.status == STARTED and t >= (
                    1.0 + (2.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            in_out_key.status = STOPPED

        # track response: 'left' = indoor, 'right' = outdoor    
        if in_out_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # either 'left' or 'right' was pressed
                in_out_key.keys = theseKeys[0]  # record just the first key pressed
                in_out_key.rt = in_out_key.clock.getTime()
                # light up the choice made by the subject, unless it was very close to the end of trial
                if t <= 2.8:
                    if in_out_key.keys == 'left':
                        indoors.color = 'yellow'
                    else:
                        outdoors.color = 'yellow'
                # was this 'correct'?
                if (in_out_key.keys == str(in_out)) or (in_out_key.keys == in_out):
                    in_out_key.corr = 1
                else:
                    in_out_key.corr = 0

        # check if all components are finished
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scenesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # scroll to next routine if 'tab' is pressed       
    if event.getKeys(keyList=["tab"]):
        break

    # -------Wrap up current trial, record responses-------
    for thisComponent in scenesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if in_out_key.keys in ['', [], None]:  # No response was made
        in_out_key.keys = None
        # was no response the correct answer?!
        if str(in_out).lower() == 'none':
            in_out_key.corr = 1  # correct non-response
        else:
            in_out_key.corr = 0  # failed to respond (incorrectly)
    # store subjects choices 
    scene_familarization.addData('in_out_key.keys', in_out_key.keys)
    scene_familarization.addData('in_out_key.corr', in_out_key.corr)
    if in_out_key.keys is not None:  # we had a response
        scene_familarization.addData('in_out_key.rt', in_out_key.rt)
    thisExp.nextEntry()

# -------Ending Routine "Scenes"-------
for thisComponent in scenesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ##############################################################
# Ashkan: Add a screen that says "You completed the scene task \n Please get the experimenter"
# #############################################################
instructions.setText("You completed the scene task \n Please get the experimenter")
instructions.draw()
win.flip()
while True:
    time.sleep(1)  # Reduces amount of resources used
    if event.getKeys(keyList=['esc', 'escape']):
        core.quit()
    elif event.getKeys(keyList=['space']):
        break


# -----------------------------------------------------------------------------------------------------------
# Scene familiarization ended-> move on to training
# -----------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------
# Training Instructions called 'train_instr'
# -----------------------------------------------------------------------------------------------------------

# Initialize components for Routine "train_instr"
train_instrClock = core.Clock()
# visual component to hold slides from the training instruction power point
tr_instructions = visual.ImageStim(win=win, name='tr_instructions',
                                   image='sin', mask=None,
                                   ori=0, pos=[0, 0], size=[1.8, 2],
                                   color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                   flipHoriz=False, flipVert=False,
                                   texRes=128, interpolate=True, depth=0.0)

# ------ Routine "train_instr"-------
# set up the loop for training instructions
train_instructions = data.TrialHandler(nReps=1, method='sequential',
                                       extraInfo=expInfo, originPath=u'/Users/labuser/Documents/Eugenia/attachments/',
                                       trialList=data.importConditions("training/train_instructions.xlsx"),
                                       seed=None, name='Training_instructions')

# thisExp.addLoop(train_instructions)  # add the loop to the experiment.
# If uncommented, instructions will be displayed in output file.
thisTrInstruction = train_instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisScene_familarization.rgb)
if thisTrInstruction is not None:
    for paramName in thisTrInstruction.keys():
        exec (paramName + '= thisTrInstruction.' + paramName)

# loop for each slide 
for thisTrInstruction in train_instructions:
    currentLoop = train_instructions
    # abbreviate parameter names if possible (e.g. rgb = thisScene_familarization.rgb)
    if thisTrInstruction is not None:
        for paramName in thisTrInstruction.keys():
            exec (paramName + '= thisTrInstruction.' + paramName)

    # ------Prepare to start Routine "train_instr"-------
    t = 0
    InstructionsClock.reset()  # clock 
    frameN = -1
    # select an arbitrary large enough time for reading one slide
    # the routine is forced to move to next slide when subject presses 'space'
    routineTimer.add(900.000000)
    # update component parameters for each repeat
    confirm_instr = event.BuilderKeyResponse()  # add key response for 'space'
    confirm_instr.status = NOT_STARTED
    # update component parameters for each repeat
    if inst_train is None:
        break
    tr_instructions.setImage("images/" + inst_train)
    # -------------------------------------------
    # keep track of which components have finished
    TrInstructionsComponents = [tr_instructions, confirm_instr]
    for thisComponent in TrInstructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "train_instr"-------
    continueRoutine = True
    # loop for each frame
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = InstructionsClock.getTime()
        frameN += 1  # number of completed frames (so 0 is the first frame)

        # update/draw components on each frame
        # *Initial_instructions* updates
        if t >= 0.0 and tr_instructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            tr_instructions.tStart = t  # underestimates by a little under one frame
            tr_instructions.frameNStart = frameN  # exact frame index
            tr_instructions.setAutoDraw(True)
        if tr_instructions.status == STARTED and t >= (
                    0.0 + (900.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            tr_instructions.setAutoDraw(False)

        # *confirm_instr* updates
        if t >= 0.0 and confirm_instr.status == NOT_STARTED:
            # keep track of start time/frame for later
            confirm_instr.tStart = t  # underestimates by a little under one frame
            confirm_instr.frameNStart = frameN  # exact frame index
            confirm_instr.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if confirm_instr.status == STARTED and t >= (
                    0.0 + (900.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            confirm_instr.status = STOPPED
        if confirm_instr.status == STARTED:
            # track if subject pressed 'space'
            theseKeys = event.getKeys(keyList=['space'])
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            # check if subject wants to move to the next slide    
            if len(theseKeys) > 0:
                # a response ends the routine
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
            # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # move to training if 'tab' is pressed       
    if event.getKeys(keyList=["tab"]):
        continueRoutine = False

# -------Ending Routine "train_instr"-------
for thisComponent in TrInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)




# -----------------------------------------------------------------------------------------------------------
# Training instructions are done -> move on to practice
# -----------------------------------------------------------------------------------------------------------

# visuals for both practice and training
###############################################################

# Initialize components for Routine "trial"
trialClock = core.Clock()
# Text component to hold instructions for break times
trial_break = visual.TextStim(win=win, ori=0, name='trial_break',
                              text=None, font=u'Arial',
                              pos=[0, 0], height=0.1, wrapWidth=None,
                              color=u'white', colorSpace='rgb', opacity=1,
                              depth=0.0)
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
# fixation point
fixation = visual.TextStim(win=win, ori=0, name='fixation',
                           text=u'+', font=u'Arial',
                           pos=[0, 0], height=0.1, wrapWidth=None,
                           color=u'black', colorSpace=' rgb', opacity=1,
                           depth=-2.0)

# No response Message
no_response = visual.TextStim(win=win, ori=0, name='no_response', text=u' ', font=u'Arial',
                              pos=[0, 0], height=0.1, wrapWidth=None,
                              color=u'red', colorSpace='rgb', opacity=1,
                              depth=-8.0)

# Novel/Familiar 'decorative mat'
trainScene = visual.ImageStim(win=win, name='trainScene',
                              image='sin', mask=None,
                              ori=0, pos=[0, 0], size=1.5,
                              color=[1, 1, 1], colorSpace='rgb', opacity=1,
                              flipHoriz=False, flipVert=False,
                              texRes=128, interpolate=True, depth=-3.0)

# components for two symbols
stim1 = visual.ImageStim(win=win, name='stim1',
                         image='sin', mask=None,
                         ori=0, pos=[-0.35, 0], size=[0.35, 0.8],
                         color=[1, 1, 1], colorSpace='rgb', opacity=1,
                         flipHoriz=False, flipVert=False,
                         texRes=128, interpolate=True, depth=-4.0)
light_up1 = visual.Rect(win=win, width=0.35, height=0.8, name='light_up1',
                        ori=0, pos=[-0.35, 0],
                        lineColor='white', lineColorSpace='rgb',
                        fillColor=None, fillColorSpace='rgb', opacity=1,
                        lineWidth=4,
                        interpolate=True, depth=-6.0)
stim2 = visual.ImageStim(win=win, name='stim2',
                         image='sin', mask=None,
                         ori=0, pos=[0.35, 0], size=[0.35, 0.8],
                         color=[1, 1, 1], colorSpace='rgb', opacity=1,
                         flipHoriz=False, flipVert=False,
                         texRes=128, interpolate=True, depth=-5.0)
light_up2 = visual.Rect(win=win, width=0.35, height=0.8, name='light_up2',
                        ori=0, pos=[0.35, 0],
                        lineColor='white', lineColorSpace='rgb',
                        fillColor=None, fillColorSpace='rgb', opacity=1,
                        lineWidth=4,
                        interpolate=True, depth=-6.0)

# components for feedback
feedback1 = visual.TextStim(win=win, ori=0, name='feedback1', text=u' ', font=u'Arial',
                            pos=[-0.35, 0], height=0.3, wrapWidth=None,
                            color=u'red', colorSpace='rgb', opacity=1,
                            depth=-8.0)
feedback2 = visual.TextStim(win=win, ori=0, name='feedback2', text=u' ', font=u'Arial',
                            pos=[0.35, 0], height=0.3, wrapWidth=None,
                            color=u'red', colorSpace='rgb', opacity=1,
                            depth=-9.0)
# white boxes to make feedback visible
box1 = visual.Rect(win=win, width=0.3, height=0.4, name='box1',
                   ori=0, pos=[-0.35, 0],
                   lineColor='white', lineColorSpace='rgb',
                   fillColor='white', fillColorSpace='rgb', opacity=1,
                   lineWidth=4,
                   interpolate=True, depth=-7.0)
box2 = visual.Rect(win=win, width=0.3, height=0.4, name='box2',
                   ori=0, pos=[0.35, 0],
                   lineColor='white', lineColorSpace='rgb',
                   fillColor='white', fillColorSpace='rgb', opacity=1,
                   lineWidth=4,
                   interpolate=True, depth=-7.0)

###############################################################

pract_instructions = visual.TextStim(win=win, ori=0, name='pract',
                                     text=u'', font=u'Arial',
                                     pos=[0, 0], height=0.2, wrapWidth=None,
                                     color=u'white', colorSpace='rgb', opacity=1,
                                     depth=0.0)

# ---------- Practice instructions ----------
pract_instructions.setText(
    "You will now do a practice phase before starting the game. \n\n Press the SPACE BAR to start.")

continueRoutine = True
while continueRoutine:

    pract_instructions.draw()

    if event.getKeys(keyList=['space']):
        continueRoutine = False

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    win.flip()

# ---------- Practice phase ----------

# set up handler to look after randomisation of conditions etc
filename = u'practice/practice.csv'
practice = data.TrialHandler(nReps=1, method='sequential',
                             extraInfo=expInfo, originPath=u'/Users/labuser/Documents/Eugenia/attachments/',
                             trialList=data.importConditions(filename),
                             seed=None, name='practice')

thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible
if thisPractice is not None:
    for paramName in thisPractice.keys():
        exec (paramName + '= thisPractice.' + paramName)

# ---- Add random variables for feedback probabilities --------------------

# there are maximum of 6 of each pair
a_prac = ss.binom.rvs(1, 0.8, size=6)  # worth 100 points if 1 and 0 if 0
b_prac = np.fabs(np.ones(6) - a_prac)  # worth 100 points if 1 and 0 if 0
c_prac = ss.binom.rvs(1, 0.7, size=6)  # worth 100 points if 1 and 0 if 0
d_prac = np.fabs(np.ones(6) - c_prac)  # worth 100 points if 1 and 0 if 0

# create a dictionary to hold the distributions for each symbol
conditions = {"A": a_prac, "B": b_prac, "C": c_prac, "D": d_prac}

# Dictionary that holds current indexes in the conditions array. At all times A = B, A'=B', C=D, C'=D'
indexes = {"A": 0, "B": 0, "A'": 0, "B'": 0, "C": 0, "D": 0, "C'": 0, "D'": 0}
done = False  # start checking performance if True
all = 0  # number of all trials passed
points = 0  # current number of points

# loop for every trial
for thisPractice in practice:

    # check if it is a break time ------------------------------------------------------
    break_time = 1.0
    trial_break.setText(u"")
    break_text = u"Take a break for a bit. Once you're ready to continue press 'space'.\n"
    # -----------------------------------------------------------------------------------
    currentLoop = practice
    # abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
    if thisPractice is not None:
        for paramName in thisPractice.keys():
            exec (paramName + '= thisPractice.' + paramName)

    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    routineTimer.add(break_time + 5.000000)
    # update scene and symbols for each trial
    trainScene.setImage("images/" + image)
    stim1.setImage("images/" + card1)
    stim2.setImage("images/" + card2)
    # add a key response for trial
    response = event.BuilderKeyResponse()
    response.status = NOT_STARTED
    # add a key response for ending a break
    break_response = event.BuilderKeyResponse()
    break_response.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = [ISI, fixation, trainScene, light_up1, light_up2, box1, box2, stim1, stim2, response,
                       no_response, break_response, feedback1, feedback2]
    # boxes have to be clear until feedback is shown
    # on feedback, fill in
    box1.lineColor = None
    box2.lineColor = None
    box1.fillColor = None
    box2.fillColor = None
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial"-------
    continueRoutine = True

    # loop for every frame
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN += 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *break_response* updates
        if t >= 0.0 and break_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            break_response.tStart = t  # underestimates by a little under one frame
            break_response.frameNStart = frameN  # exact frame index
            break_response.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if break_response.status == STARTED and t >= (
                    0.0 + (break_time - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            trial_break.setText('')
            break_response.status = STOPPED
        if break_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # a 'space' was pressed -> end routine current trial
                trial_break.setText('')
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine -> move to next trial
            break

        # *fixation* updates
        if t >= break_time and fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation.tStart = t  # underestimates by a little under one frame
            fixation.frameNStart = frameN  # exact frame index
            fixation.setAutoDraw(True)
        if fixation.status == STARTED and t >= (
                    break_time + (0.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            fixation.setAutoDraw(False)

        # *trainScene* updates
        if t >= break_time + 0.5 and trainScene.status == NOT_STARTED:
            # keep track of start time/frame for later
            trainScene.tStart = t  # underestimates by a little under one frame
            trainScene.frameNStart = frameN  # exact frame index
            trainScene.setAutoDraw(True)
        if trainScene.status == STARTED and t >= (
                        break_time + 0.5 + (3.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            trainScene.setAutoDraw(False)

        # *stim1* updates
        if t >= break_time + 2.0 and stim1.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim1.tStart = t  # underestimates by a little under one frame
            stim1.frameNStart = frameN  # exact frame index
            stim1.setAutoDraw(True)
        if stim1.status == STARTED and t >= (
                        break_time + 2.0 + (3.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            stim1.setAutoDraw(False)

        # *light_up1* updates
        if t >= break_time + 2.0 and light_up1.status == NOT_STARTED:
            # keep track of start time/frame for later
            light_up1.tStart = t  # underestimates by a little under one frame
            light_up1.frameNStart = frameN  # exact frame index
            light_up1.setAutoDraw(True)
        if light_up1.status == STARTED and t >= (
                        break_time + 2.0 + (3.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            light_up1.setAutoDraw(False)

        # *light_up2* updates
        if t >= break_time + 2.0 and light_up2.status == NOT_STARTED:
            # keep track of start time/frame for later
            light_up2.tStart = t  # underestimates by a little under one frame
            light_up2.frameNStart = frameN  # exact frame index
            light_up2.setAutoDraw(True)
        if light_up2.status == STARTED and t >= (
                        break_time + 2.0 + (3.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            light_up2.setAutoDraw(False)

        # *stim2* updates
        if t >= break_time + 2.0 and stim2.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim2.tStart = t  # underestimates by a little under one frame
            stim2.frameNStart = frameN  # exact frame index
            stim2.setAutoDraw(True)
        if stim2.status == STARTED and t >= (
                        break_time + 2.0 + (3.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            stim2.setAutoDraw(False)

        # *response* updates
        if t >= break_time + 2.0 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')

        # light up the picked card
        if t <= break_time + 3.3:
            if response.keys == 'left':
                light_up1.lineColor = 'yellow'
            elif response.keys == 'right':
                light_up2.lineColor = 'yellow'

        if response.status == STARTED and t >= (
                        break_time + 2.0 + (1.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            response.status = STOPPED
            all += 1  # counter for how many trials we've been through over all

            cond = None

            # check what condition was selected
            if response.keys == 'left':
                cond = cond1
            if response.keys == 'right':
                cond = cond2

            if cond is not None:
                i = indexes[cond]
            # update index for the feedback array
            indexes[cond1] += 1
            indexes[cond2] += 1
            # update counts for performance check
            # identify which pair is in the current trial
            pair = "AB"
            if cond == "A'" or cond == "B'":
                pair = "A'B'"
            elif cond == "C'" or cond == "D'":
                pair = "C'D'"
            elif cond == "C" or cond == "D":
                pair = "CD"

            # update feedback
            if response.keys == 'left':
                box1.lineColor = 'white'
                box1.fillColor = 'white'
                no_response.setText(u' ')
                feedback2.setText(u' ')
                if conditions[cond1][i] == 1:
                    feedback1.setText(u'100')
                    points += 100
                else:
                    feedback1.setText(u'0')
            elif response.keys == 'right':
                box2.lineColor = 'white'
                box2.fillColor = 'white'
                no_response.setText(u' ')
                feedback1.setText(u' ')
                if conditions[cond2][i] == 1:
                    feedback2.setText(u'100')
                    points += 100
                else:
                    feedback2.setText(u'0')
            else:
                no_response.setText(u'TOO SLOW')
                feedback2.setText(u' ')
                feedback1.setText(u' ')

        if response.status == STARTED:
            # track which symbol the subject chose
            theseKeys = event.getKeys(keyList=['left', 'right'])
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if not response.keys:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()

        # ---- Show feedback ----------------------------------------------------------
        if t >= break_time + 3.5 and box1.status == NOT_STARTED:
            # keep track of start time/frame for later
            box1.tStart = t  # underestimates by a little under one frame
            box1.frameNStart = frameN  # exact frame index
            box1.setAutoDraw(True)
        if box1.status == STARTED and t >= (
                        break_time + 3.5 + (1.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            box1.setAutoDraw(False)

        if t >= break_time + 3.5 and box2.status == NOT_STARTED:
            # keep track of start time/frame for later
            box2.tStart = t  # underestimates by a little under one frame
            box2.frameNStart = frameN  # exact frame index
            box2.setAutoDraw(True)
        if box2.status == STARTED and t >= (
                        break_time + 3.5 + (1.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            box2.setAutoDraw(False)

        # *feedback1* updates
        # set feedback according to probability and record performance
        if t >= break_time + 3.5 and feedback1.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback1.tStart = t  # underestimates by a little under one frame
            feedback1.frameNStart = frameN  # exact frame index
            feedback1.setAutoDraw(True)
        if feedback1.status == STARTED and t >= (
                        break_time + 3.5 + (1.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            feedback1.setAutoDraw(False)
        # *feedback2* updates
        if t >= break_time + 3.5 and feedback2.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback2.tStart = t  # underestimates by a little under one frame
            feedback2.frameNStart = frameN  # exact frame index
            feedback2.setAutoDraw(True)
        if feedback2.status == STARTED and t >= (
                        break_time + 3.5 + (1.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            feedback2.setAutoDraw(False)
        # *no_response updates
        if t >= break_time + 3.5 and no_response.status == NOT_STARTED:
            no_response.tStart = t  # underestimates by a little under one frame
            no_response.frameNStart = frameN  # exact frame index
            no_response.setAutoDraw(True)
        if no_response.status == STARTED and t >= (
                        break_time + 3.5 + (1.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            no_response.setAutoDraw(False)
        # ------------------------------------------------------------------------------

        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period

        # check if all components have finished
        # check for scroll to next routine
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # update light up boxes before next trial
    light_up1.lineColor = 'white'
    light_up2.lineColor = 'white'

    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
        # store data for training (TrialHandler)

    thisExp.nextEntry()

# ---------- Practice finished instructions ----------
pract_instructions.setText(
    "You had a score of %d.\n\nPress SPACE to start the Game." % points)

continueRoutine = True
while continueRoutine:

    pract_instructions.draw()

    if event.getKeys(keyList=['space']):
        continueRoutine = False

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    win.flip()

# -----------------------------------------------------------------------------------------------------------
# practice is done -> move on to training
# -----------------------------------------------------------------------------------------------------------

# set up handler to look after randomisation of conditions etc
# adjust filename according to participant number
filename = u'training/training_' + expInfo['participant'] + '.csv'
training = data.TrialHandler(nReps=1, method='sequential',
                             extraInfo=expInfo, originPath=u'/Users/labuser/Documents/Eugenia/attachments/',
                             trialList=data.importConditions(filename),
                             seed=None, name='training')

thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath=u'/Users/labuser/Documents/Eugenia/attachments/',
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename_training)

thisExp.addLoop(training)  # add the loop to the experiment
thisTraining = training.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTraining.rgb)
if thisTraining is not None:
    for paramName in thisTraining.keys():
        exec (paramName + '= thisTraining.' + paramName)

# ---- Add random variables for feedback probabilities --------------------


# there are maximum of 60 of each pair 

a_old = np.concatenate([np.ones(0.8 * 55), np.zeros(0.2 * 55)])
np.random.shuffle(a_old)
a_old = np.concatenate([[0, 1, 1, 1, 1], a_old])
b_old = np.fabs(np.ones(60) - a_old)  # worth 100 points if 1 and 0 if 0

a_new = np.concatenate([np.ones(0.8 * 55), np.zeros(0.2 * 55)])
np.random.shuffle(a_new)
a_new = np.concatenate([[0, 1, 1, 1, 1], a_new])
b_new = np.fabs(np.ones(60) - a_new)  # worth 100 points if 1 and 0 if 0

c_old = np.concatenate([np.ones((0.7 * 55) + 1), np.zeros(0.3 * 55)])  # + 1 to make total 55
np.random.shuffle(c_old)
c_old = np.concatenate([[0, 1, 1, 0, 1], c_old])
d_old = np.fabs(np.ones(60) - c_old)  # worth 100 points if 1 and 0 if 0

c_new = np.concatenate([np.ones((0.7 * 55) + 1), np.zeros(0.3 * 55)])  # + 1 to make total 55
np.random.shuffle(c_new)
c_new = np.concatenate([[0, 1, 1, 0, 1], c_new])
d_new = np.fabs(np.ones(60) - c_new)  # worth 100 points if 1 and 0 if 0

# create a dictionary to hold the distributions for each symbol
conditions = {"A": a_old, "B": b_old, "A'": a_new, "B'": b_new, "C": c_old, "D": d_old, "C'": c_new, "D'": d_new}

# ---------------------------------------------------------------------------

# ----- Add variables to keep track of where we are in the dictionary and the performance criterion
# Choose A over B, A' over B', C over D, C' over D'
right_resp = {"A": 1, "B": 0, "A'": 1, "B'": 0, "C": 1, "D": 0, "C'": 1, "D'": 0}
# The letter and its pair
pair_dict = {"A": "B", "B": "A", "A'": "B'", "B'": "A'", "C": "D", "D": "C", "C'": "D'", "D'": "C'"}
# Dictionary that holds current indexes in the conditions array. At all times A = B, A'=B', C=D, C'=D'
indexes = {"A": 0, "B": 0, "A'": 0, "B'": 0, "C": 0, "D": 0, "C'": 0, "D'": 0}
# number of successful trials for each pair
performance = {"AB": 0, "A'B'": 0, "CD": 0, "C'D'": 0}
# current number of trials passed for each pair 
count = {"AB": 0, "A'B'": 0, "CD": 0, "C'D'": 0}
# performance threshold
threshold = {"AB": 0.70, "A'B'": 0.70, "CD": 0.60, "C'D'": 0.60}
done = False  # start checking performance if True
all = 0  # number of all trials passed
points = 0  # current number of points
# ---------------------------------------------------------------------------

long_break = False  # flag to take a break after each 40 trials
crit = False  # Flag to determine whether participant will do Test Phase

# loop for every trial
for thisTraining in training:
    # check if it is a break time ------------------------------------------------------
    break_time = 1.0
    trial_break.setText(u"")
    break_text = u"Take a break for a bit. Once you're ready to continue press 'space'.\n"
    if all % 40 != 0:
        long_break = False
        trial_break.setText('')
        # if a multiple of 40, then take a break - change duration of the break and its text
    if all != 0 and all % 40 == 0 and not long_break:
        break_time = 900.0
        trial_break.setText(break_text)
        long_break = True
    # -----------------------------------------------------------------------------------
    currentLoop = training
    # abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
    if thisTraining is not None:
        for paramName in thisTraining.keys():
            exec (paramName + '= thisTraining.' + paramName)

    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    routineTimer.add(break_time + 5.000000)
    # update scene and symbols for each trial
    trainScene.setImage("images/" + image)
    stim1.setImage("images/" + card1)
    stim2.setImage("images/" + card2)
    # add a key response for trial
    response = event.BuilderKeyResponse()
    response.status = NOT_STARTED
    # add a key response for ending a break
    break_response = event.BuilderKeyResponse()
    break_response.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = [trial_break, ISI, fixation, trainScene, light_up1, light_up2, box1, box2, stim1, stim2, response,
                       no_response, break_response, feedback1, feedback2]
    # boxes have to be clear until feedback is shown
    # on feedback, fill in
    box1.lineColor = None
    box2.lineColor = None
    box1.fillColor = None
    box2.fillColor = None
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial"-------
    continueRoutine = True

    # loop for every frame
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN += 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *trial_break* updates
        if t >= 0.0 and trial_break.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_break.tStart = t  # underestimates by a little under one frame
            trial_break.frameNStart = frameN  # exact frame index
            trial_break.setAutoDraw(True)
        if trial_break.status == STARTED and t >= (
                    0.0 + (break_time - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            trial_break.setAutoDraw(False)

        # *break_response* updates
        if t >= 0.0 and break_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            break_response.tStart = t  # underestimates by a little under one frame
            break_response.frameNStart = frameN  # exact frame index
            break_response.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if break_response.status == STARTED and t >= (
                    0.0 + (break_time - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            trial_break.setText('')
            break_response.status = STOPPED
        if break_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # a 'space' was pressed -> end routine current trial
                trial_break.setText('')
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine -> move to next trial
            break

        # *fixation* updates
        if t >= break_time and fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation.tStart = t  # underestimates by a little under one frame
            fixation.frameNStart = frameN  # exact frame index
            fixation.setAutoDraw(True)
        if fixation.status == STARTED and t >= (
                    break_time + (0.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            fixation.setAutoDraw(False)

        # *trainScene* updates
        if t >= break_time + 0.5 and trainScene.status == NOT_STARTED:
            # keep track of start time/frame for later
            trainScene.tStart = t  # underestimates by a little under one frame
            trainScene.frameNStart = frameN  # exact frame index
            trainScene.setAutoDraw(True)
        if trainScene.status == STARTED and t >= (
                        break_time + 0.5 + (3.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            trainScene.setAutoDraw(False)

        # *stim1* updates
        if t >= break_time + 2.0 and stim1.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim1.tStart = t  # underestimates by a little under one frame
            stim1.frameNStart = frameN  # exact frame index
            stim1.setAutoDraw(True)
        if stim1.status == STARTED and t >= (
                        break_time + 2.0 + (3.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            stim1.setAutoDraw(False)

        # *light_up1* updates
        if t >= break_time + 2.0 and light_up1.status == NOT_STARTED:
            # keep track of start time/frame for later
            light_up1.tStart = t  # underestimates by a little under one frame
            light_up1.frameNStart = frameN  # exact frame index
            light_up1.setAutoDraw(True)
        if light_up1.status == STARTED and t >= (
                        break_time + 2.0 + (3.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            light_up1.setAutoDraw(False)

        # *light_up2* updates
        if t >= break_time + 2.0 and light_up2.status == NOT_STARTED:
            # keep track of start time/frame for later
            light_up2.tStart = t  # underestimates by a little under one frame
            light_up2.frameNStart = frameN  # exact frame index
            light_up2.setAutoDraw(True)
        if light_up2.status == STARTED and t >= (
                        break_time + 2.0 + (3.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            light_up2.setAutoDraw(False)

        # *stim2* updates
        if t >= break_time + 2.0 and stim2.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim2.tStart = t  # underestimates by a little under one frame
            stim2.frameNStart = frameN  # exact frame index
            stim2.setAutoDraw(True)
        if stim2.status == STARTED and t >= (
                        break_time + 2.0 + (3.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            stim2.setAutoDraw(False)

        # *response* updates
        if t >= break_time + 2.0 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')

        # light up the picked card
        if t <= break_time + 3.3:
            if response.keys == 'left':
                light_up1.lineColor = 'yellow'
            elif response.keys == 'right':
                light_up2.lineColor = 'yellow'

        if response.status == STARTED and t >= (
                        break_time + 2.0 + (1.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            response.status = STOPPED
            all += 1  # counter for how many trials we've been through over all

            cond = None

            # check what condition was selected
            if response.keys == 'left':
                cond = cond1
            if response.keys == 'right':
                cond = cond2

            if cond is not None:
                i = indexes[cond]
            # update index for the feedback array
            indexes[cond1] += 1
            indexes[cond2] += 1
            # update counts for performance check
            # identify which pair is in the current trial
            pair = "AB"
            if cond1 == "A'" or cond1 == "B'":
                pair = "A'B'"
            elif cond1 == "C'" or cond1 == "D'":
                pair = "C'D'"
            elif cond1 == "C" or cond1 == "D":
                pair = "CD"
            count[pair] += 1  # how many of this pair appeared in trials

            if cond is not None:
                performance[pair] += right_resp[cond]  # update individual performance for every pair

            # update feedback
            if response.keys == 'left':
                box1.lineColor = 'white'
                box1.fillColor = 'white'
                no_response.setText(u' ')
                feedback2.setText(u' ')
                if conditions[cond1][i] == 1:
                    feedback1.setText(u'100')
                    points += 100
                else:
                    feedback1.setText(u'0')
            elif response.keys == 'right':
                box2.lineColor = 'white'
                box2.fillColor = 'white'
                no_response.setText(u' ')
                feedback1.setText(u' ')
                if conditions[cond2][i] == 1:
                    feedback2.setText(u'100')
                    points += 100
                else:
                    feedback2.setText(u'0')
            else:
                no_response.setText(u'TOO SLOW')
                feedback2.setText(u' ')
                feedback1.setText(u' ')

            # do performance check in the end of each trial after 100 trials and stop this stage is reached
            # performance.
            if all > 100:
                per = 0  # performance for current pair
                done = True
                # loop through every pair
                for key in count:
                    if count[key] != 0:
                        per = performance[key] / count[key]
                        # log current performance
                        logging.log(level=logging.DATA,
                                    msg='Count for ' + key + ' = ' + str(count[key]) + ', cur_correct = ' + str(
                                        performance[key]) + ', performance = ' + str(per))
                        if per <= threshold[key]:
                            done = False
                    else:
                        done = False
                        # ---------------------------------------------------------------------------------------------------------

        if response.status == STARTED:
            # track which symbol the subject chose
            theseKeys = event.getKeys(keyList=['left', 'right'])
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if not response.keys:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()

        # ---- Show feedback ----------------------------------------------------------
        if t >= break_time + 3.5 and box1.status == NOT_STARTED:
            # keep track of start time/frame for later
            box1.tStart = t  # underestimates by a little under one frame
            box1.frameNStart = frameN  # exact frame index
            box1.setAutoDraw(True)
        if box1.status == STARTED and t >= (
                        break_time + 3.5 + (1.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            box1.setAutoDraw(False)

        if t >= break_time + 3.5 and box2.status == NOT_STARTED:
            # keep track of start time/frame for later
            box2.tStart = t  # underestimates by a little under one frame
            box2.frameNStart = frameN  # exact frame index
            box2.setAutoDraw(True)
        if box2.status == STARTED and t >= (
                        break_time + 3.5 + (1.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            box2.setAutoDraw(False)

        # *feedback1* updates
        # set feedback according to probability and record performance
        if t >= break_time + 3.5 and feedback1.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback1.tStart = t  # underestimates by a little under one frame
            feedback1.frameNStart = frameN  # exact frame index
            feedback1.setAutoDraw(True)
        if feedback1.status == STARTED and t >= (
                        break_time + 3.5 + (1.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            feedback1.setAutoDraw(False)
        # *feedback2* updates
        if t >= break_time + 3.5 and feedback2.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback2.tStart = t  # underestimates by a little under one frame
            feedback2.frameNStart = frameN  # exact frame index
            feedback2.setAutoDraw(True)
        if feedback2.status == STARTED and t >= (
                        break_time + 3.5 + (1.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            feedback2.setAutoDraw(False)
        # *no_response updates
        if t >= break_time + 3.5 and no_response.status == NOT_STARTED:
            no_response.tStart = t  # underestimates by a little under one frame
            no_response.frameNStart = frameN  # exact frame index
            no_response.setAutoDraw(True)
        if no_response.status == STARTED and t >= (
                        break_time + 3.5 + (1.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            no_response.setAutoDraw(False)
        # ------------------------------------------------------------------------------

        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period

        # check if all components have finished
        # check for scroll to next routine
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # update light up boxes before next trial
    light_up1.lineColor = 'white'
    light_up2.lineColor = 'white'

    if done or event.getKeys(keyList=["tab"]):
        crit = True
        break

    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
    # store data for training (TrialHandler)

    # Use cond1 over cond since cond could be None if there is no response
    if right_resp[cond1]:
        training.addData('right_resp', cond1)
    else:
        training.addData('right_resp', pair_dict[cond1])

    if count[pair] != 0:
        training.addData('pair_perc_corr', performance[pair] / count[pair])

    if response.keys is not None:  # we had a response
        training.addData('resp_corr', right_resp[cond])
        training.addData('train_response', response.keys)
        training.addData('feedback1', conditions[cond1][i])
        training.addData('feedback2', conditions[cond2][i])
        training.addData('feedback1_text', feedback1.text)
        training.addData('feedback2_text', feedback2.text)
        training.addData('train_response_cond', cond)
        training.addData('train_response.rt', response.rt)
    thisExp.nextEntry()




# ##############################################################
# Ashkan: Add a screen that says "You completed this task \n Please get the experimenter"
# #############################################################
instructions.setText("You completed this task \n Please get the experimenter")
instructions.draw()
win.flip()
while True:
    time.sleep(1)  # Reduces amount of resources used
    if event.getKeys(keyList=['esc', 'escape']):
        core.quit()
    elif event.getKeys(keyList=['space']):
        break


# -----------------------------------------------------------------------------------------------------------
# Training  done-> move on to testing
# ----------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------
# Test instructions
# -----------------------------------------------------------------------------------------------------------

# Initialize components for Routine "test_inst"
test_instClock = core.Clock()
# points won in training
points_txt = visual.TextStim(win=win, ori=0, name='points_txt',
                             text=u'', font=u'Arial',
                             pos=[0, 0], height=0.1, wrapWidth=None,
                             color=u'Black', colorSpace='rgb', opacity=1,
                             depth=0.0)

ts_instructions = visual.ImageStim(win=win, name='ts_instructions',
                                   image='sin', mask=None,
                                   ori=0, pos=[0, 0], size=[1.8, 2],
                                   color=[1, 1, 1], colorSpace='rgb', opacity=1,
                                   flipHoriz=False, flipVert=False,
                                   texRes=128, interpolate=True, depth=0.0)

# -----------------------------------------------------------------------------------------------------------
# first show points from training 
# -----------------------------------------------------------------------------------------------------------
t = 0
test_instClock.reset()  # clock 
frameN = -1
routineTimer.add(900.000000)
# update component parameters for each repeat
inst_exit = event.BuilderKeyResponse()  # create an object of type KeyResponse
inst_exit.status = NOT_STARTED
# keep track of which components have finished
pointsComponents = []

# test_instComponents = []
# end.setText(u" You've earned " + str(
#    points) + " points! \n Thank you for participating in the experiment. \n Please press 'space' to exit. ")


num_corr = 0
for key in count:
    num_corr += performance[key]

points_txt_str = u"You got %d%% correct!" % int((num_corr / all) * 100)
if not crit:
    points_txt_str += u"\n Thank you for participating in the experiment. \n Please press 'space' to exit. "

points_txt.setText(points_txt_str)
pointsComponents.append(points_txt)
pointsComponents.append(inst_exit)
for thisComponent in pointsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "points"-------
continueRoutine = True
# loop for each frame
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = test_instClock.getTime()
    frameN += 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *test_instructions* updates
    if t >= 0.0 and points_txt.status == NOT_STARTED:
        # keep track of start time/frame for later
        points_txt.tStart = t  # underestimates by a little under one frame
        points_txt.frameNStart = frameN  # exact frame index
        points_txt.setAutoDraw(True)
    if points_txt.status == STARTED and t >= (
                0.0 + (900.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
        points_txt.setAutoDraw(False)

    # *inst_exit* updates
    if t >= 0.0 and inst_exit.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_exit.tStart = t  # underestimates by a little under one frame
        inst_exit.frameNStart = frameN  # exact frame index
        inst_exit.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(inst_exit.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if inst_exit.status == STARTED and t >= (
                0.0 + (900.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
        inst_exit.status = STOPPED
    if inst_exit.status == STARTED:
        # move forward on 'space'
        theseKeys = event.getKeys(keyList=['space'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed

            # Exit the experimen. The particpant will not do the test phase
            # Exit the experiment. The particpant will not do the test phase
            if not crit:
                win.close()
                core.quit()
            inst_exit.keys = theseKeys[-1]  # just the last key pressed
            inst_exit.rt = inst_exit.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pointsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "points"-------
for thisComponent in pointsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.nextEntry()

# -----------------------------------------------------------------------------------------------------------
# Actual test instructions
# -----------------------------------------------------------------------------------------------------------

# set up trial handler so it draws slides from file test_instructions.xlsx
test_instructions = data.TrialHandler(nReps=1, method='sequential',
                                      extraInfo=expInfo, originPath=u'/Users/labuser/Documents/Eugenia/attachments/',
                                      trialList=data.importConditions("test/test_instructions.xlsx"),
                                      seed=None, name='test_instructions')
# thisExp.addLoop(test_instructions)  # add the loop to the experiment.
#  If uncommented, the instructions will be added to the output file.
thisInstruction = test_instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisScene_familarization.rgb)
if thisInstruction is not None:
    for paramName in thisInstruction.keys():
        exec (paramName + '= thisInstruction.' + paramName)

# loop for each slide
for thisInstruction in test_instructions:
    currentLoop = test_instructions
    # abbreviate parameter names if possible (e.g. rgb = thisScene_familarization.rgb)
    if thisInstruction is not None:
        for paramName in thisInstruction.keys():
            exec (paramName + '= thisInstruction.' + paramName)

    # ------Prepare to start Routine "test_inst"-------
    t = 0
    InstructionsClock.reset()  # clock 
    frameN = -1
    routineTimer.add(900.000000)
    # update component parameters for each repeat
    confirm_instr = event.BuilderKeyResponse()  # create an object of type KeyResponse
    confirm_instr.status = NOT_STARTED
    # update slide 
    if test_inst is None:
        break
    ts_instructions.setImage("images/" + test_inst)
    # keep track of which components have finished
    TestInstructionsComponents = [ts_instructions, confirm_instr]
    for thisComponent in TestInstructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "test_inst"-------
    continueRoutine = True
    # update/draw components on each frame
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = InstructionsClock.getTime()
        frameN += 1  # number of completed frames (so 0 is the first frame)

        # *ts_instructions* updates
        if t >= 0.0 and ts_instructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            ts_instructions.tStart = t  # underestimates by a little under one frame
            ts_instructions.frameNStart = frameN  # exact frame index
            ts_instructions.setAutoDraw(True)
        if ts_instructions.status == STARTED and t >= (
                    0.0 + (900.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            ts_instructions.setAutoDraw(False)

        # *confirm_instr* updates
        if t >= 0.0 and confirm_instr.status == NOT_STARTED:
            # keep track of start time/frame for later
            confirm_instr.tStart = t  # underestimates by a little under one frame
            confirm_instr.frameNStart = frameN  # exact frame index
            confirm_instr.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if confirm_instr.status == STARTED and t >= (
                    0.0 + (900.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            confirm_instr.status = STOPPED
        if confirm_instr.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # a space was pressed
                # a response ends the routine
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in TestInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# -----------------------------------------------------------------------------------------------------------
# Test Instructions are done -> move on to test stage
# -----------------------------------------------------------------------------------------------------------

# Initialize components for Routine "test_trial"
test_trialClock = core.Clock()
test_fix = visual.TextStim(win=win, ori=0, name='test_fix',
                           text=u'+', font=u'Arial',
                           pos=[0, 0], height=0.2, wrapWidth=None,
                           color=u'black', colorSpace='rgb', opacity=1,
                           depth=0.0)
test_stimA = visual.ImageStim(win=win, name='test_stimA',
                              image='sin', mask=None,
                              ori=0, pos=[-0.35, 0], size=[0.35, 0.8],
                              color=[1, 1, 1], colorSpace='rgb', opacity=1,
                              flipHoriz=False, flipVert=False,
                              texRes=128, interpolate=True, depth=-1.0)
test_stimB = visual.ImageStim(win=win, name='test_stimB',
                              image='sin', mask=None,
                              ori=0, pos=[0.35, 0], size=[0.35, 0.8],
                              color=[1, 1, 1], colorSpace='rgb', opacity=1,
                              flipHoriz=False, flipVert=False,
                              texRes=128, interpolate=True, depth=-2.0)

end = visual.TextStim(win=win, ori=0, name='end',
                      text=u'', font=u'Arial',
                      pos=[0, 0], height=0.2, wrapWidth=None,
                      color=u'white', colorSpace='rgb', opacity=1,
                      depth=0.0)

# set up handler to look after randomisation of conditions etc
# select test file according to participant's number
filename = u'test/test_' + expInfo['participant'] + '.csv'
test = data.TrialHandler(nReps=1, method='sequential',
                         extraInfo=expInfo, originPath=u'/Users/labuser/Documents/Eugenia/attachments/',
                         trialList=data.importConditions(filename),
                         seed=None, name='test')

thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath=u'/Users/labuser/Documents/Eugenia/attachments/',
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename_test)

thisExp.addLoop(test)  # add the loop to the experiment
thisTest = test.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTest.rgb)
if thisTest != None:
    for paramName in thisTest.keys():
        exec (paramName + '= thisTest.' + paramName)

## Reset probabilities for the test stage ##
a_old = ss.binom.rvs(1, 0.8, size=25)
b_old = np.fabs(np.ones(25) - a_old)
a_new = ss.binom.rvs(1, 0.8, size=25)
b_new = np.fabs(np.ones(25) - a_new)
c_old = ss.binom.rvs(1, 0.7, size=25)
d_old = np.fabs(np.ones(25) - c_old)
c_new = ss.binom.rvs(1, 0.7, size=25)
d_new = np.fabs(np.ones(25) - c_new)

conditions = {"A": a_old, "B": b_old, "A'": a_new, "B'": b_new, "C": c_old, "D": d_old, "C'": c_new, "D'": d_new}
cond_prob = {"A": 0.8, "B": 0.2, "A'": 0.8, "B'": 0.2, "C": 0.7, "D": 0.3, "C'": 0.7, "D'": 0.3}

###########################################

# index for condition arrays
indexes = {"A": 0, "B": 0, "A'": 0, "B'": 0, "C": 0, "D": 0, "C'": 0, "D'": 0}
done = False
all = 0
num_corr = 0
points = 0
# loop for trials 
for thisTest in test:
    currentLoop = test
    all += 1
    # abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
    if thisTest is not None:
        for paramName in thisTest.keys():
            exec (paramName + '= thisTest.' + paramName)

    # ------Prepare to start Routine "test_trial"-------
    t = 0
    test_trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    test_stimA.setImage("images/" + trial_card1)
    test_stimB.setImage("images/" + trial_card2)
    test_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    test_response.status = NOT_STARTED
    # keep track of which components have finished
    test_trialComponents = [test_fix, test_stimA, test_stimB, light_up1, light_up2, test_response]
    # reuse light up boxes from training
    light_up1.lineColor = 'white'
    light_up2.lineColor = 'white'
    for thisComponent in test_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "test_trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = test_trialClock.getTime()
        frameN += 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *test_fix* updates
        if t >= 1 and test_fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            test_fix.tStart = t  # underestimates by a little under one frame
            test_fix.frameNStart = frameN  # exact frame index
            test_fix.setAutoDraw(True)
        if test_fix.status == STARTED and t >= (
                    1 + (0.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            test_fix.setAutoDraw(False)

        # *test_stimA* updates
        if t >= 1.5 and test_stimA.status == NOT_STARTED:
            # keep track of start time/frame for later
            test_stimA.tStart = t  # underestimates by a little under one frame
            test_stimA.frameNStart = frameN  # exact frame index
            test_stimA.setAutoDraw(True)
        if test_stimA.status == STARTED and t >= (
                    1.5 + (1.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            test_stimA.setAutoDraw(False)

        # *test_stimB* updates
        if t >= 1.5 and test_stimB.status == NOT_STARTED:
            # keep track of start time/frame for later
            test_stimB.tStart = t  # underestimates by a little under one frame
            test_stimB.frameNStart = frameN  # exact frame index
            test_stimB.setAutoDraw(True)
        if test_stimB.status == STARTED and t >= (
                    1.5 + (1.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            test_stimB.setAutoDraw(False)

        # *light_up1* updates
        if t >= 1.5 and light_up1.status == NOT_STARTED:
            # keep track of start time/frame for later
            light_up1.tStart = t  # underestimates by a little under one frame
            light_up1.frameNStart = frameN  # exact frame index
            light_up1.setAutoDraw(True)
        if light_up1.status == STARTED and t >= (
                    1.5 + (1.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            light_up1.setAutoDraw(False)

        # *light_up2* updates
        if t >= 1.5 and light_up2.status == NOT_STARTED:
            # keep track of start time/frame for later
            light_up2.tStart = t  # underestimates by a little under one frame
            light_up2.frameNStart = frameN  # exact frame index
            light_up2.setAutoDraw(True)
        if light_up2.status == STARTED and t >= (
                    1.5 + (1.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            light_up2.setAutoDraw(False)

        # *response* updates
        if t >= 1.5 and test_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            test_response.tStart = t  # underestimates by a little under one frame
            test_response.frameNStart = frameN  # exact frame index
            test_response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(test_response.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')

        if test_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if not test_response.keys:  # then this was the first keypress
                    test_response.keys = theseKeys[0]  # just the first key pressed
                    test_response.rt = test_response.clock.getTime()
        if test_response.status == STARTED and t >= (
                    1.5 + (1.5 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
            test_response.status = STOPPED

            # Update points and indexes into arrays

            cond = None

            if test_response.keys == 'left':
                cond = trial_cond1
            if test_response.keys == 'right':
                cond = trial_cond2

            if cond is not None:

                i = indexes[cond]

                if conditions[trial_cond1][indexes[trial_cond1]] == conditions[trial_cond2][indexes[trial_cond2]]:
                    num_corr += 1
                else:
                    num_corr += conditions[cond][i]

                points += conditions[cond][i] * 100
            # update index in the feedback array
            indexes[trial_cond1] += 1
            indexes[trial_cond2] += 1
            # ------------------------------------

        # light up chosen symbol
        if t <= 2.8:
            if test_response.keys == 'left':
                light_up1.lineColor = 'yellow'

            elif test_response.keys == 'right':
                light_up2.lineColor = 'yellow'

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in test_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # force end stage on tab        
    if event.getKeys(keyList=["tab"]):
        break

    # -------Ending Routine "test_trial"-------
    for thisComponent in test_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if test_response.keys in ['', [], None]:  # No response was made
        test_response.keys = None
        # store data for training (TrialHandler)
    test.addData('test_response.keys', test_response.keys)
    if test_response.keys is not None:  # we had a response
        test.addData('test_response_cond', cond)
        test.addData('test_response.rt', test_response.rt)
    thisExp.nextEntry()

##### End the experiment - show points

# ------Prepare to start Routine "test_points"-------
t = 0
test_instClock.reset()  # clock 
frameN = -1
routineTimer.add(900.000000)
# update component parameters for each repeat
end_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
end_resp.status = NOT_STARTED
# keep track of which components have finished
test_instComponents = []

points_txt_str = u"You got %d%% correct!" % int((num_corr / all) * 100)

end.setText(points_txt_str + "\n Thank you for participating in the experiment. \n Please press 'space' to exit. ")

test_instComponents.append(end)
test_instComponents.append(end_resp)
for thisComponent in test_instComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "test_inst"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = test_instClock.getTime()
    frameN += 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *test_instructions* updates
    if t >= 0.0 and end.status == NOT_STARTED:
        # keep track of start time/frame for later
        end.tStart = t  # underestimates by a little under one frame
        end.frameNStart = frameN  # exact frame index
        end.setAutoDraw(True)
    if end.status == STARTED and t >= (0.0 + (900.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
        end.setAutoDraw(False)

    # *inst_exit* updates
    if t >= 0.0 and end_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_resp.tStart = t  # underestimates by a little under one frame
        end_resp.frameNStart = frameN  # exact frame index
        end_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(end_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if end_resp.status == STARTED and t >= (
                0.0 + (900.0 - win.monitorFramePeriod * 0.75)):  # most of one frame period left
        end_resp.status = STOPPED
    if end_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            end_resp.keys = theseKeys[-1]  # just the last key pressed
            end_resp.rt = inst_exit.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test_instComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in test_instComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

win.close()
core.quit()
