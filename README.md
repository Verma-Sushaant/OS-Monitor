# Real Time OS Monitor

## Overview
The Real Time OS Monitor is a real-time system monitoring application that provides insights into CPU, memory, disk, network, and GPU usage. The application includes an interactive GUI for visualizing system performance.

## Features
- **Real-Time Monitoring:** Tracks CPU, memory, disk, network, and GPU usage.
- **Interactive Visualization:** Displays real-time system metrics with dynamic graphs.

## Project Structure
```
AI-Powered-OS-Monitor/
|── system_monitor/
|   |── __init__.py
|   │── cpu_details.py        # Fetches and analyzes CPU usage data
|   │── memory_details.py     # Monitors memory usage
|   │── disk_details.py       # Tracks disk usage statistics
|
|── hardwre-monitor/
|   |── __init__.py
|   │── network_details.py    # Monitors network activity
|   │── gpu_details.py        # Retrieves GPU performance metrics
|
|── application/
|   |── __init__.py
|   │── main.py               # Integrates all modules and runs the GUI
|
│── README.md             # Project documentation
```

## Installation
### Prerequisites
- Python 3.x

### Steps to Run the Application
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/AI-Powered-OS-Monitor.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Real-Time-OS-Monitor
   ```
3. Run the application:
   ```sh
   python main.py
   ```

## Usage
- The application launches a GUI displaying real-time graphs and system performance metrics.

## Future Enhancements
- Extend monitoring for multiple devices.
- Add remote monitoring and mobile integration.
- Implement cloud-based system performance tracking.
- Will use AI models to detect abnormal system behavior.

## License
This project is licensed under Creative Commons (CC BY-NC 4.0).

## Author
**[Verma-Sushaant]**(https://github.com/Verma-Sushaant)

## Contributions
Contributions are welcome! Please create a pull request or raise an issue if you'd like to improve the project.
