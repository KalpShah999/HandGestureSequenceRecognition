# Hand Gesture Sequcence Recognizer (multipipe)

This project extends the [following repo](https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe).

# Requirements
* mediapipe 0.8.1
* OpenCV 3.4.2 or Later
* Tensorflow 2.3.0 or Later<br>tf-nightly 2.5.0.dev or later (Only when creating a TFLite for an LSTM model)
* scikit-learn 0.23.2 or Later (Only if you want to display the confusion matrix) 
* matplotlib 3.3.2 or Later (Only if you want to display the confusion matrix)

# Demo
In order to run the program, run the following command in the terminal. 
```bash
python3 app.py
```

# input.py 
This additional script takes input from the main `app.py` script to track sequences of hand gestures to initiate different actions. Customs actions and corresponding sequences can be defined in the script manually as well. 
