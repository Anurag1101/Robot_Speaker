import pyttsx3

if __name__ == '__main__':
    print("Welcome to Robot Speaker Created by Anurag")
    
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    while True:
        x = input("What you want me to speak: ")
        
        if x == "bored":
            engine.say("Bye Bye Friend, Hope you enjoyed my service!!")
            engine.runAndWait()
            break
        
        # Use the engine to say the input text
        engine.say(x)
        
        # Process and speak the queued command
        engine.runAndWait()

        
    

    
