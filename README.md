# Ride Share Simulation

## Real-Time Ride Sharing Simulation

This project simulates a real-time ride-sharing application, matching riders with drivers based on proximity, calculating fares, and estimating ride durations. It also demonstrates database management for tracking drivers, riders, and rides.

---

## Features

### Driver and Rider Management
- Register drivers and riders in the system.
- Track driver locations, availability, and total earnings.

### Ride Matching
- Match riders with the nearest available drivers using the **Haversine formula** for distance calculation.

### Fare and Duration Calculation
- Compute ride fare based on distance.
- Estimate ride duration based on average speed.

### Database Integration
- SQLite database to store driver, rider, and ride details.

### Real-Time Simulation
- Simulates random ride requests and driver availability updates in real time.

---

## Prerequisites

- **Python 3.x**
- **SQLite3** (comes pre-installed with Python)

---

## Installation

### Clone this repository:
```bash
git clone https://github.com/your-username/real-time-ride-sharing.git
cd real-time-ride-sharing

