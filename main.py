from tinydb import TinyDB, Query

# Create or connect to the database
db = TinyDB('students.json')
student1={
    "id": 101,
    "name": "John Doe",
    "age": 16,
    "gender": "Male",
    "contact": "123-456-7890",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 85,
        "science": 90,
        "english": 88
    },
    "attendance": 92.5,
    "activities": ["Basketball", "Debate Club"],
    "address": {
        "street": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "zip_code": "62704"
    }
}



students_table = db.table('students')
students_table.insert(student1)