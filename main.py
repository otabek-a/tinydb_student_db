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
student6 = {
    "id": 6,
    "name": "Rustam",
    "age": 19,
    "gender": "male",
    "contact": "99-333-33-33",
    "grade_level": "Grade 12",
    "subjects": {
        "math": 76,
        "science": 84,
        "english": 80
    },
    "attendance": 89.5,
    "activities": ["Football Team", "Math Club"],
    "address": {
        "street": "32 Shohrux",
        "city": "Andijon",
        "state": "Qizil",
        "zip_code": "170200"
    }
}
student7 = {
    "id": 7,
    "name": "Madina",
    "age": 18,
    "gender": "female",
    "contact": "99-444-44-44",
    "grade_level": "Grade 11",
    "subjects": {
        "math": 92,
        "science": 90,
        "english": 88
    },
    "attendance": 96.0,
    "activities": ["Reading Club", "HISTORY Club"],
    "address": {
        "street": "45 Islom Karimov",
        "city": "Buxoro",
        "state": "Oq",
        "zip_code": "200300"
    }
}
student8 = {
    "id": 8,
    "name": "Azizbek",
    "age": 20,
    "gender": "male",
    "contact": "99-555-55-55",
    "grade_level": "Grade 12",
    "subjects": {
        "math": 87,
        "science": 93,
        "english": 86
    },
    "attendance": 92.0,
    "activities": ["IT Club", "Robotics"],
    "address": {
        "street": "67 Mustaqillik",
        "city": "Qarshi",
        "state": "Ko'k",
        "zip_code": "180200"
    }
}
student9 = {
    "id": 9,
    "name": "Dilnoza",
    "age": 17,
    "gender": "female",
    "contact": "99-666-66-66",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 84,
        "science": 88,
        "english": 89
    },
    "attendance": 93.5,
    "activities": ["Art Club", "Dance Club"],
    "address": {
        "street": "90 Yangiobod",
        "city": "Farg'ona",
        "state": "Yashil",
        "zip_code": "150400"
    }
}


students_table = db.table('students')
students_table.insert_multiple([student1,student2])
students_table.insert(student3)
students_table.insert(student4)
students_table.insert(student5)
students_table.insert(student6)
students_table.insert(student7)
students_table.insert(student8)
students_table.insert(student9)