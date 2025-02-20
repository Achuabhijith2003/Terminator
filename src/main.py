from memory.memory_manager import MemoryManager
from reminders.reminder_manager import ReminderManager
from listening.listener import Listener
from speaking.speaker import Speaker
from real_time_data.data_retriever import DataRetriever
from ai.ai_integration import AIIntegration
from utils import config

def main():
    # Initialize components
    memory_manager = MemoryManager()
    reminder_manager = ReminderManager()
    listener = Listener()
    speaker = Speaker()
    data_retriever = DataRetriever()
    ai_agent = AIIntegration()

    # Main loop
    while True:
        # Listen for commands
        command = listener.start_listening()
        
        # Ensure command is a valid string
        if not isinstance(command, str) or not command.strip():
            continue  # Ignore empty or invalid commands
        
        print(f"Command: {command}")
        
        # Check if the command contains the word "terminator"
        if "terminator" in command.lower():
            speaker.speak("I am the Terminator. How can I assist you?")
            
        
        # Optional: Add an exit command
        elif "exit" in command.lower() or "stop" in command.lower():
            speaker.speak("Shutting down. Goodbye!")
            break  # Exit the loop and end the program
        else:
            # Process the command
            result = ai_agent.generate_response_by_langchain(command)
            print("REspose: ", result)
            speaker.speak(result)
            

if __name__ == "__main__":
    main()