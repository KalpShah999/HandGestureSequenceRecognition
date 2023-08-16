import os

# Define arrays to keep track of the sequence of hand gesture events 
right_inputs = []
left_inputs = []

# Define an input lag (number of consequtive readings for a gesture to be registered)
input_lag = 1

# Define temporary variables 
input_lag_counter = 0
temp_input = ""


# Function that debounces the input signal of the gesture type on either hand (right and left)
def normalize_input(input, handedness):
    global right_inputs
    global left_inputs
    global input_lag
    global input_lag_counter
    global temp_input
    
    # Check which hand the gesture is coming from 
    if (handedness == "Right"):
        
        # Add new gesture in sequence if the sequence just started 
        if (len(right_inputs) == 0):
            right_inputs.append(input)
            print(input, handedness)
            
        # Begin tracking a new gesture as a potential stable signal 
        elif (right_inputs[-1] != input and temp_input != input):
            temp_input = input
            input_lag_counter = 0
        
        # Stabalize the signal 
        elif (right_inputs[-1] != input):
            # Add the gesture to the sequence if it was stable past the input lab 
            if input_lag_counter == input_lag:
                right_inputs.append(input)
                input_lag_counter += 1
                print(input, handedness)
                
            # Increase the input lag counter until the gesture is deemed stable 
            elif (input_lag_counter < input_lag):
                input_lag_counter += 1
    else:
        # Add new gesture in sequence if the sequence just started 
        if (len(left_inputs) == 0):
            left_inputs.append(input)
            print(input, handedness)
            
        # Begin tracking a new gesture as a potential stable signal 
        elif (left_inputs[-1] != input and temp_input != input):
            temp_input = input
            input_lag_counter = 0
        
        # Stabalize the signal 
        elif (left_inputs[-1] != input):
            # Add the gesture to the sequence if it was stable past the input lab 
            if input_lag_counter == input_lag:
                left_inputs.append(input)
                input_lag_counter += 1
                print(input, handedness)
                
            # Increase the input lag counter until the gesture is deemed stable 
            elif (input_lag_counter < input_lag):
                input_lag_counter += 1


# This function checks if a sequence matches one of the predefined sequences 
def check_sequence():
    global right_inputs
    global left_inputs
    
    # Define possible sequnces 
    sequences = [["Open", "Close", "OK", "Pointer", "Open", "Close"], 
                 ["Open", "Close", "Pointer", "Open", "Close"]]
    
        
    # Check to see is a sequence is matched 
    if (right_inputs[-len(sequences[0]):] == sequences[0]):
        # Put the computer to sleep if the first sequence is matched (can be changed to anything)
        print("---   Putting system to sleep   ---")
        os.system("""osascript -e 'tell app "Finder" to sleep'""")
        right_inputs.clear()
        
    elif (right_inputs[-len(sequences[1]):] == sequences[1]):
        # Open spotify if the second sequence is matched (can be changed to anything)
        print("---   Open Spotify   ---")
        os.system("""osascript -e 'tell app "spotify" to activate'""")
        right_inputs.clear()

# Function to debounce the signal and check for any sequences 
def get_input(input, handedness):
    normalize_input(input, handedness)
    check_sequence()