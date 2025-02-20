class Listener:
    def __init__(self):
        self.is_listening = False

    def start_listening(self, callback):
        self.is_listening = True
        # Code to start capturing audio input and processing it
        # Call the callback function with the processed audio input

    def stop_listening(self):
        self.is_listening = False
        # Code to stop capturing audio input