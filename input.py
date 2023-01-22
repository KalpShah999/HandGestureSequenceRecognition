import os

right_inputs = []
left_inputs = []
input_lag = 1
input_lag_counter = 0
temp_input = ""

def normalize_input(input, handedness):
    global right_inputs
    global left_inputs
    global input_lag
    global input_lag_counter
    global temp_input
    
    if (handedness == "Right"):
        if (len(right_inputs) == 0):
            right_inputs.append(input)
            print(input, handedness)
        elif (right_inputs[-1] != input and temp_input != input):
            temp_input = input
            input_lag_counter = 0
        elif (right_inputs[-1] != input):
            if input_lag_counter == input_lag:
                right_inputs.append(input)
                input_lag_counter += 1
                print(input, handedness)
                #print(right_inputs)
            elif (input_lag_counter < input_lag):
                input_lag_counter += 1
    else:
        if (len(left_inputs) == 0):
            left_inputs.append(input)
            print(input, handedness)
        elif (left_inputs[-1] != input and temp_input != input):
            temp_input = input
            input_lag_counter = 0
        elif (left_inputs[-1] != input):
            if input_lag_counter == input_lag:
                left_inputs.append(input)
                input_lag_counter += 1
                print(input, handedness)
                #print(left_inputs)
            elif (input_lag_counter < input_lag):
                input_lag_counter += 1
                
def normalize_input_2(inputs):
    global right_inputs
    global left_inputs
    global input_lag
    global input_lag_counter
    global temp_input
    
    if (handedness == "Right"):
        if (len(right_inputs) == 0):
            right_inputs.append(input)
            print(input, handedness)
        elif (right_inputs[-1] != input and temp_input != input):
            temp_input = input
            input_lag_counter = 0
        elif (right_inputs[-1] != input):
            if input_lag_counter == input_lag:
                right_inputs.append(input)
                input_lag_counter += 1
                print(input, handedness)
                #print(right_inputs)
            elif (input_lag_counter < input_lag):
                input_lag_counter += 1
    else:
        if (len(left_inputs) == 0):
            left_inputs.append(input)
            print(input, handedness)
        elif (left_inputs[-1] != input and temp_input != input):
            temp_input = input
            input_lag_counter = 0
        elif (left_inputs[-1] != input):
            if input_lag_counter == input_lag:
                left_inputs.append(input)
                input_lag_counter += 1
                print(input, handedness)
                #print(left_inputs)
            elif (input_lag_counter < input_lag):
                input_lag_counter += 1


def check_sequence():
    global right_inputs
    global left_inputs
    
    sequences = [["Open", "Close", "OK", "Pointer", "Open", "Close"], ["Open", "Close", "Pointer", "Open", "Close"]]
    
    #print(arr_temp)
        
    if (right_inputs[-len(sequences[0]):] == sequences[0]):
        print("---   Putting system to sleep   ---")
        os.system("""osascript -e 'tell app "Finder" to sleep'""")
        right_inputs.clear()
    elif (right_inputs[-len(sequences[1]):] == sequences[1]):
        print("---   Open Spotify   ---")
        os.system("""osascript -e 'tell app "spotify" to activate'""")
        right_inputs.clear()


def get_input(input, handedness):
    normalize_input(input, handedness)
    check_sequence()
    

def get_input_2(inputs):
    normalize_input(input, handedness)
    check_sequence()