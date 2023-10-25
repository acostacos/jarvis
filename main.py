from jarvis import Jarvis

def main():
    j = Jarvis(language='english+f3') 
    j.listen_for_name()

    # Keep listening for name in background
    # If name is heard, acknowledge
    # get question - Use whisper for recognition now
    # Get question and put it to open ai with prompt
    # Get prompt and convert to speech

if __name__ == '__main__':
    main()
