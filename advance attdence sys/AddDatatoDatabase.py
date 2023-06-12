import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendance-f1253-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "1":
        {
            "name": "Harsh",
            "major": "Robotics",
            "starting_year": 2021,
            "total_attendance": 1,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-1-20 00:54:34"
        },
    "2":
        {
            "name": "Nitesh",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 1,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2023-1-20 00:54:34"
        },
    "3":
        {
            "name": "Khemchand",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 1,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2023-1-20 00:54:34"
        }
   
}

for key, value in data.items():
    ref.child(key).set(value)