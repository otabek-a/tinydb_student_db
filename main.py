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

student2={
    "id": 100,
    "name": "otabek",
    "age": 18,
    "gender": "male",
    "contact": "99-192-82-13",
    "grade_level": "Graded school",
    "subjects": {
        "math": 90,
        "science": 100,
        "english": 77
    },
    "attendance": 92.5,
    "activities": ["IT", "HISTORY Club"],
    "address": {
        "street": "45 chilquduq",
        "city": "zoom",
        "state": "Up",
        "zip_code": "P571"
    }
}
student3={
    "id": 1,
    "name": "sardor",
    "age": 18,
    "gender": "male",
    "contact": "99-192-13-13",
    "grade_level": "Graded school",
    "subjects": {
        "math": 79,
        "science": 90,
        "english": 87
    },
    "attendance": 92.5,
    "activities": ["dance club", "HISTORY Club"],
    "address": {
        "street": "56 zargaron",
        "city": "moontepa",
        "state": "left",
        "zip_code": "9090"
    }
}
student4 = {
    "id": 4,
    "name": "Abdulla",
    "age": 18,
    "gender": "male",
    "contact": "99-111-11-11",
    "grade_level": "Grade 11",
    "subjects": {
        "math": 82,
        "science": 88,
        "english": 79
    },
    "attendance": 91.0,
    "activities": ["Chess Club", "HISTORY Club"],
    "address": {
        "street": "23 Bog'bon",
        "city": "Toshkent",
        "state": "Yashil",
        "zip_code": "700100"
    }
}
student5 = {
    "id": 5,
    "name": "Ziyoda",
    "age": 17,
    "gender": "female",
    "contact": "99-222-22-22",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 89,
        "science": 91,
        "english": 85
    },
    "attendance": 94.0,
    "activities": ["Dance Club", "Art Club"],
    "address": {
        "street": "15 Amir Temur",
        "city": "Samarqand",
        "state": "Ko'k",
        "zip_code": "140105"
    }
}

students_table = db.table('students')
students_table.insert_multiple([student1,student2])
students_table.insert(student3)
students_table.insert(student4)
students_table.insert(student5)