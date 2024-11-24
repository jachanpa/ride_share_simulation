# ride_share_simulation
Real-Time Ride Sharing Simulation
This project simulates a real-time ride-sharing application, matching riders with drivers based on proximity, calculating fares, and estimating ride durations. It also demonstrates database management for tracking drivers, riders, and rides.

Features
Driver and Rider Management:

Register drivers and riders in the system.
Track driver locations, availability, and total earnings.
Ride Matching:

Match riders with the nearest available drivers using the Haversine formula for distance calculation.
Fare and Duration Calculation:

Compute ride fare based on distance.
Estimate ride duration based on average speed.
Database Integration:

SQLite database to store driver, rider, and ride details.
Real-Time Simulation:

Simulates random ride requests and driver availability updates in real-time.
Prerequisites
Python 3.x
SQLite3 (comes pre-installed with Python)
Installation
Clone this repository:

bash
Copy code
git clone https://github.com/your-username/real-time-ride-sharing.git
cd real-time-ride-sharing
Install required packages (if any):

bash
Copy code
pip install -r requirements.txt
Note: No external libraries are required for this project.

How to Run
Run the Python file:

bash
Copy code
python ride_sharing_simulation.py
The simulation will:

Create drivers and riders.
Match riders with the nearest drivers.
Update the driver's availability and location in real time.
Project Files
ride_sharing_simulation.py: Main script for the ride-sharing simulation.
Database (ride_sharing.db): SQLite database generated automatically during runtime. Contains three tables:
Drivers: Stores driver information (ID, location, availability, earnings).
Riders: Stores rider information (ID, location).
Rides: Logs ride details (rider, driver, fare, distance, duration).

Future Improvements
Add real-time GPS tracking for drivers and riders.
Integrate a payment gateway simulation for ride fare transactions.
Extend support for ride cancellations and disputes.
License
This project is licensed under the MIT License.

Author
Jagadeesh
Feel free to reach out for feedback or collaboration!

