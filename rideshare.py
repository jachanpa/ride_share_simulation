import math
import time
import random
import sqlite3

BASE_FARE = 5.0
FARE_PER_KM = 2.0
AVERAGE_SPEED_KMPH = 40

def setup_database():
    conn = sqlite3.connect('ride_sharing.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Drivers (
            driver_id TEXT PRIMARY KEY,
            latitude REAL,
            longitude REAL,
            available INTEGER,
            total_earnings REAL DEFAULT 0
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Riders (
            rider_id TEXT PRIMARY KEY,
            latitude REAL,
            longitude REAL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Rides (
            ride_id INTEGER PRIMARY KEY AUTOINCREMENT,
            rider_id TEXT,
            driver_id TEXT,
            distance REAL,
            fare REAL,
            duration REAL,
            payment_status TEXT DEFAULT 'Pending',
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

class Driver:
    def __init__(self, driver_id, lat, lon, db_conn):
        self.driver_id = driver_id
        self.location = (lat, lon)
        self.available = True
        self.total_earnings = 0
        self.db_conn = db_conn
        self.save_to_db()

    def save_to_db(self):
        with self.db_conn:
            self.db_conn.execute('''
                INSERT OR REPLACE INTO Drivers (driver_id, latitude, longitude, available, total_earnings)
                VALUES (?, ?, ?, ?, ?)
            ''', (self.driver_id, self.location[0], self.location[1], int(self.available), self.total_earnings))

    def update_location(self, lat, lon):
        self.location = (lat, lon)
        self.save_to_db()

    def set_availability(self, status):
        self.available = status
        self.save_to_db()

    def update_earnings(self, fare):
        self.total_earnings += fare
        self.save_to_db()

    def __str__(self):
        return f"Driver {self.driver_id} at {self.location}, Available: {self.available}, Earnings: {self.total_earnings}"

class Rider:
    def __init__(self, rider_id, lat, lon, db_conn):
        self.rider_id = rider_id
        self.location = (lat, lon)
        self.db_conn = db_conn
        self.save_to_db()

    def save_to_db(self):
        with self.db_conn:
            self.db_conn.execute('''
                INSERT INTO Riders (rider_id, latitude, longitude)
                VALUES (?, ?, ?)
            ''', (self.rider_id, self.location[0], self.location[1]))

    def __str__(self):
        return f"Rider {self.rider_id} at {self.location}"

def haversine_distance(coord1, coord2):
    R = 6371
    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def calculate_fare_and_duration(distance):
    fare = BASE_FARE + (distance * FARE_PER_KM)
    duration = (distance / AVERAGE_SPEED_KMPH) * 60
    return fare, duration

def match_ride(rider, drivers, db_conn):
    nearest_driver = None
    min_distance = float('inf')
    for driver in drivers:
        if driver.available:
            distance = haversine_distance(rider.location, driver.location)
            if distance < min_distance:
                min_distance = distance
                nearest_driver = driver
    if nearest_driver:
        fare, duration = calculate_fare_and_duration(min_distance)
        nearest_driver.set_availability(False)
        nearest_driver.update_earnings(fare)
        print(f"Matched {rider} with {nearest_driver}")
        print(f"Distance: {min_distance:.2f} km, Fare: {fare:.2f}, Duration: {duration:.2f} minutes")
        with db_conn:
            db_conn.execute('''
                INSERT INTO Rides (rider_id, driver_id, distance, fare, duration, payment_status)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (rider.rider_id, nearest_driver.driver_id, min_distance, fare, duration, 'Pending'))
        return nearest_driver
    else:
        print(f"No drivers available for {rider}")
        return None

def real_time_ride_sharing_simulation():
    setup_database()
    conn = sqlite3.connect('ride_sharing.db')
    drivers = [
        Driver('D1', 40.7128, -74.0060, conn),
        Driver('D2', 34.0522, -118.2437, conn),
        Driver('D3', 41.8781, -87.6298, conn)
    ]
    while True:
        new_rider = Rider(f"R{random.randint(1000, 9999)}", random.uniform(30, 50), random.uniform(-125, -70), conn)
        print(f"New rider request: {new_rider}")
        match_ride(new_rider, drivers, conn)
        if random.random() > 0.7:
            completed_driver = random.choice(drivers)
            completed_driver.set_availability(True)
            completed_driver.update_location(random.uniform(30, 50), random.uniform(-125, -70))
            print(f"Driver {completed_driver.driver_id} is now available at {completed_driver.location}")
        time.sleep(2)

real_time_ride_sharing_simulation()
