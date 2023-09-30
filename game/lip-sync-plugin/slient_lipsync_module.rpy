init python:
    import os
    import pygame
    
    # Directory containing the lipsync data files
    lipsync_data_dir = "lip-sync-plugin/lip-sync-data/"
    lipsync_key_released = False  # Flag to track whether the Space or Enter key is released
    mouse_button_released = False  # Flag to track whether the mouse button is released
    touch_released = False  # Flag to track whether a touch event is released
    renpy.music.register_channel("lipsync", 'sfx', loop=False)
    
    # Function to load lipsync data for a character and audio track
    def load_lipsync_data(chapter_name, audio_track):
        global lipsync_data
        lipsync_data = []
        # Construct the relative path to the lipsync data file
        audio_file = os.path.basename(audio_track)
        file_path = os.path.join(lipsync_data_dir, chapter_name, os.path.splitext(audio_file)[0] + ".txt").replace("\\",'/')
        # Load the lipsync data using renpy.load()
        lipsync_text = renpy.file(file_path).read().decode("utf-8")
        # Parse the lipsync data and store it as a list of tuples (start_time, mouth_shape)
        for line in lipsync_text.strip().split('\n'):
            start_time, mouth_shape = line.strip().split('\t')
            lipsync_data.append((float(start_time), mouth_shape))
    
    # Function to apply lipsync animation to a dialogue
    def lipsync(character, chapter_name, audio_track, dialogue, default_mouth="mouth_A", invisible=False):
        global lipsync_key_released, mouse_button_released, touch_released
        character_name = str(character.name)
        track_name = 'audio/Voice/'+character_name+'.ogg'
        load_lipsync_data(chapter_name, audio_track)  # Load lipsync data based on the audio track
        prev_start_time = 0
        interrupted = False  # Flag to track if the interaction was interrupted
        # Show the mouth shapes at the appropriate times
        d_mouth = default_mouth[6:]
        renpy.store._history = False
        for i in range(len(lipsync_data)):
            if i == 0:
                renpy.store._history = True
                renpy.say(who=character, what=dialogue+"{fast}", interact=False)   # show the dialogue
                renpy.store._history = False
            else:
                renpy.say(who=character, what=dialogue+"{fast}", interact=False)   # show the dialogue
            start_time, mouth_shape = lipsync_data[i]
            if d_mouth != 'X' or d_mouth != 'A':
                renpy.music.play(track_name, channel="lipsync", relative_volume=0.3)
            if invisible == False:
                renpy.show(str(character.name) + ' mouth_' + mouth_shape)                    # Show the mouth shape image
            if i < len(lipsync_data) - 1:   
                next_start_time = lipsync_data[i + 1][0]
                duration = next_start_time - start_time + 0.01                      # Calculate duration between mouth shapes
            else:
                duration = 0.01  # Last mouth shape, no next_start_time
            renpy.pause(duration)  # Pause to synchronize with audio
            # Check for player interaction and break if interrupted
            touched = any(event.type == pygame.FINGERDOWN for event in pygame.event.get())
            mouse_clicked = pygame.mouse.get_pressed()[0]
            keys = pygame.key.get_pressed()
            # Check for skip or user input keys (e.g., RETURN, SPACE, CTRL) to stop playback
            if renpy.is_skipping() or touched or (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]):
                if invisible == False:
                    renpy.show(str(character.name) + ' ' + default_mouth)
                renpy.store._history = True
                renpy.music.stop(channel="lipsync")
                return
            if (keys[pygame.K_RETURN] or keys[pygame.K_SPACE]) and lipsync_key_released:
                if invisible == False:
                    renpy.show(str(character.name) + ' ' + default_mouth)
                lipsync_key_released = False
                renpy.store._history = True
                renpy.music.stop(channel="lipsync")
                return
            if not keys[pygame.K_RETURN] and not keys[pygame.K_SPACE]:
                lipsync_key_released = True  # Set the flag to True when the keys are released
            # Check for touch release and set the interrupted flag
            if touch_released:
                interrupted = True
                touch_released = False
            # Check for mouse button release and set the interrupted flag
            if mouse_clicked:
                if mouse_button_released:
                    interrupted = True
                    mouse_button_released = False
            else:
                mouse_button_released = True  # Set the flag to True when the mouse button is released
            if interrupted:
                break
        # Ensure that the facial expression returns to 'mouth_X' when the function ends
        if invisible == False:
            renpy.show(str(character.name) + ' ' + default_mouth)
        if not interrupted:
            renpy.say(who=character, what=dialogue+"{fast}", interact=True)   # show the dialogue
        renpy.store._history = True
        renpy.music.stop(channel="lipsync")