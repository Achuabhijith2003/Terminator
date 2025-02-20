# Terminator AI Agent

This project is an AI agent themed around "Terminator," developed using OpenAI, LangChain, and Python. The agent is designed to run on a Raspberry Pi and includes capabilities for memory management, reminders, listening and speaking functionalities, and retrieving real-time data such as time and weather.

## Features

- **Memory Management**: The agent can save, retrieve, and clear memories using the MemoryManager class.
- **Reminders**: Users can set, get, and remove reminders with the ReminderManager class.
- **Listening**: The agent can capture audio input and process it using the Listener class.
- **Speaking**: The agent can convert text to speech with the Speaker class.
- **Real-Time Data Retrieval**: The agent can fetch the current time and weather information using the DataRetriever class.

## Project Structure

```
terminator-ai-agent
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── memory
│   │   ├── __init__.py
│   │   └── memory_manager.py
│   ├── reminders
│   │   ├── __init__.py
│   │   └── reminder_manager.py
│   ├── listening
│   │   ├── __init__.py
│   │   └── listener.py
│   ├── speaking
│   │   ├── __init__.py
│   │   └── speaker.py
│   ├── real_time_data
│   │   ├── __init__.py
│   │   └── data_retriever.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
├── requirements.txt
├── config.py
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd terminator-ai-agent
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the application by editing the `config.py` file to include your API keys and other necessary settings.

4. Run the application:
   ```
   python src/main.py
   ```

## Usage

- To interact with the agent, use voice commands for listening and speaking functionalities.
- Set reminders by specifying the time and message.
- Retrieve real-time data by asking the agent for the current time or weather.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.