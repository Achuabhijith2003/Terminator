from memory.memory_manager import MemoryManager
from reminders.reminder_manager import ReminderManager
from listening.listener import Listener
from speaking.speaker import Speaker
from real_time_data.data_retriever import DataRetriever

def main():
    # Initialize components
    memory_manager = MemoryManager()
    reminder_manager = ReminderManager()
    listener = Listener()
    speaker = Speaker()
    data_retriever = DataRetriever()

    # Main loop
    while True:
        # Listen for commands
        command = listener.start_listening()
        
        # Ensure command is a valid string
        if not isinstance(command, str) or not command.strip():
            continue  # Ignore empty or invalid commands
        
        print("Command:", type(command), command)
        
        # Check if the command contains the word "terminator"
        if "terminator" in command.lower():
            speaker.speak("I am the Terminator. How can I assist you?")
        
        # Optional: Add an exit command
        if "exit" in command.lower() or "stop" in command.lower():
            speaker.speak("Shutting down. Goodbye!")
            break  # Exit the loop and end the program
        else:
            # Process the command
            speaker.speak("I am sorry, I cannot help you with that.")

if __name__ == "__main__":
    main()