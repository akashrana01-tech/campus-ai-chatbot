from typing import List, Dict, Any, Optional
from datetime import datetime
from models import db, InterviewTest, User

QUESTION_BANKS: Dict[str, List[Dict[str, Any]]] = {
    "C": [
        {
            "id": 1,
            "question": "Which operator is used to access the value at the address stored in a pointer variable in C?",
            "options": ["& (Address-of)", "* (Dereference)", "-> (Arrow)", ". (Dot)"],
            "correct": 1,
            "explanation": "The asterisk (*) is the dereference operator in C, used to access the value stored at the memory address held by a pointer."
        },
        {
            "id": 2,
            "question": "What is the return type of the malloc() function in C?",
            "options": ["int*", "char*", "void*", "float*"],
            "correct": 2,
            "explanation": "malloc() allocates memory and returns a pointer of type void*, which can be typecast to any desired pointer type."
        },
        {
            "id": 3,
            "question": "Which of the following functions is used to release dynamically allocated memory in C?",
            "options": ["remove()", "delete()", "free()", "clear()"],
            "correct": 2,
            "explanation": "free() is the standard C library function in <stdlib.h> used to deallocate dynamically allocated memory."
        },
        {
            "id": 4,
            "question": "What is the default return value of a C program if main() completes successfully?",
            "options": ["-1", "0", "1", "void"],
            "correct": 1,
            "explanation": "Returning 0 from the main() function indicates that the program executed successfully without any errors to the operating system."
        },
        {
            "id": 5,
            "question": "Which header file is required to use the printf() and scanf() functions in C?",
            "options": ["<stdlib.h>", "<conio.h>", "<stdio.h>", "<math.h>"],
            "correct": 2,
            "explanation": "<stdio.h> stands for Standard Input Output header and contains declarations for printf() and scanf()."
        }
    ],
    "C++": [
        {
            "id": 1,
            "question": "Which OOP concept in C++ allows a function or operator to act in multiple forms?",
            "options": ["Encapsulation", "Polymorphism", "Inheritance", "Abstraction"],
            "correct": 1,
            "explanation": "Polymorphism (meaning 'many forms') allows the same function name or operator to exhibit different behaviors based on arguments or calling object."
        },
        {
            "id": 2,
            "question": "Which keyword is used to prevent a class method from modifying object data members?",
            "options": ["static", "final", "const", "mutable"],
            "correct": 2,
            "explanation": "A member function declared with the 'const' suffix (e.g., int getVal() const) is not allowed to modify any non-mutable data members of the object."
        },
        {
            "id": 3,
            "question": "What is a virtual function in C++ primarily used for?",
            "options": ["Compile-time polymorphism", "Runtime polymorphism (Dynamic binding)", "Memory deallocation", "Data hiding"],
            "correct": 1,
            "explanation": "Virtual functions enable runtime polymorphism / dynamic dispatch through base class pointers or references."
        },
        {
            "id": 4,
            "question": "Which access specifier in C++ makes class members accessible only to the class itself and its derived classes?",
            "options": ["public", "private", "protected", "internal"],
            "correct": 2,
            "explanation": "The 'protected' access specifier permits member access within the declaring class and its derived/child classes."
        },
        {
            "id": 5,
            "question": "What type of constructor is called when an object is initialized with another existing object of the same class?",
            "options": ["Default Constructor", "Parameterized Constructor", "Copy Constructor", "Dynamic Constructor"],
            "correct": 2,
            "explanation": "A Copy Constructor initializes an object using an existing object of the same class (e.g., MyClass b = a;)."
        }
    ],
    "Java": [
        {
            "id": 1,
            "question": "Which component of the Java Architecture is responsible for converting bytecode into machine code at runtime?",
            "options": ["JDK", "JRE", "JVM JIT Compiler", "Java Compiler (javac)"],
            "correct": 2,
            "explanation": "The JIT (Just-In-Time) compiler inside the JVM compiles bytecode into native machine instructions at runtime for improved performance."
        },
        {
            "id": 2,
            "question": "Can an interface in Java 8 and above contain method implementations?",
            "options": ["No, never", "Yes, using default and static methods", "Yes, but only private methods", "Only using abstract methods"],
            "correct": 1,
            "explanation": "Starting in Java 8, interfaces can contain concrete method implementations using the 'default' and 'static' keywords."
        },
        {
            "id": 3,
            "question": "Which collection class in Java allows key-value pairs with unique keys and null values?",
            "options": ["HashSet", "ArrayList", "HashMap", "TreeMap"],
            "correct": 2,
            "explanation": "HashMap stores key-value pairs, allows one null key and multiple null values, and guarantees fast O(1) average lookup."
        },
        {
            "id": 4,
            "question": "What happens if a static method is called on a null reference in Java?",
            "options": ["NullPointerException", "Executes normally because static methods belong to the class", "Compilation Error", "StackOverflowError"],
            "correct": 1,
            "explanation": "Static methods belong to the class and are bound at compile time, so invoking a static method via a null reference executes without NullPointerException."
        },
        {
            "id": 5,
            "question": "Which keyword is used in Java to ensure that a variable is read directly from main memory rather than thread cache?",
            "options": ["transient", "synchronized", "volatile", "final"],
            "correct": 2,
            "explanation": "The 'volatile' keyword ensures visibility of changes to variables across multiple threads by reading from and writing to main memory."
        }
    ],
    "HTML": [
        {
            "id": 1,
            "question": "Which HTML5 semantic element is most appropriate for wrapping navigation links?",
            "options": ["<section>", "<nav>", "<aside>", "<header>"],
            "correct": 1,
            "explanation": "The <nav> element is intended for major navigation blocks of links on a web page."
        },
        {
            "id": 2,
            "question": "What is the purpose of the 'alt' attribute on an <img> tag?",
            "options": ["Image height", "Alternative text for accessibility and screen readers", "Image border style", "Tooltip on hover"],
            "correct": 1,
            "explanation": "The 'alt' attribute provides alternative text for accessibility screen readers and displays when the image fails to load."
        },
        {
            "id": 3,
            "question": "Which CSS layout model is designed specifically for 1-dimensional layouts (either rows or columns)?",
            "options": ["CSS Grid", "Flexbox", "Table layout", "Float layout"],
            "correct": 1,
            "explanation": "Flexbox (Flexible Box Layout) is designed for 1-dimensional layouts (a single row or column), whereas CSS Grid handles 2 dimensions."
        },
        {
            "id": 4,
            "question": "Which JavaScript method is used to attach an event handler to an HTML element without overwriting existing handlers?",
            "options": ["element.onclick = fn", "element.addEventListener()", "element.attachHandler()", "element.bindEvent()"],
            "correct": 1,
            "explanation": "element.addEventListener() allows attaching multiple event listeners to an element without overwriting existing ones."
        },
        {
            "id": 5,
            "question": "What does CSS 'box-sizing: border-box' do?",
            "options": ["Adds a 1px border around every element", "Includes padding and border in the element's total width and height", "Removes all margins", "Sets display to inline-block"],
            "correct": 1,
            "explanation": "border-box ensures that padding and border are included within the specified width and height of the box."
        }
    ],
    "Python": [
        {
            "id": 1,
            "question": "What is the main difference between a Python list and a Python tuple?",
            "options": ["Lists are immutable, tuples are mutable", "Lists are mutable, tuples are immutable", "Tuples cannot store integers", "Lists can only hold strings"],
            "correct": 1,
            "explanation": "Lists can be modified after creation (mutable), while tuples cannot be modified once defined (immutable)."
        },
        {
            "id": 2,
            "question": "Which Python built-in function returns the length of an object such as a list or string?",
            "options": ["size()", "count()", "len()", "length()"],
            "correct": 2,
            "explanation": "The len() function returns the number of items in an iterable, string, list, tuple, or dictionary."
        },
        {
            "id": 3,
            "question": "What is the output of `[x**2 for x in range(4)]` in Python?",
            "options": ["[1, 4, 9, 16]", "[0, 1, 4, 9]", "[0, 2, 4, 6]", "[1, 2, 3, 4]"],
            "correct": 1,
            "explanation": "range(4) produces 0, 1, 2, 3. Squaring each yields 0, 1, 4, 9."
        },
        {
            "id": 4,
            "question": "Which keyword is used to define an anonymous (inline) function in Python?",
            "options": ["def", "inline", "lambda", "func"],
            "correct": 2,
            "explanation": "The 'lambda' keyword creates small, anonymous inline functions in Python (e.g. lambda x: x * 2)."
        },
        {
            "id": 5,
            "question": "Which data structure in Python stores unique, unordered elements?",
            "options": ["List", "Dictionary", "Tuple", "Set"],
            "correct": 3,
            "explanation": "A Set in Python stores unique, unordered elements and eliminates duplicates automatically."
        }
    ],
    "SQL": [
        {
            "id": 1,
            "question": "Which SQL clause is used to filter records resulting from a GROUP BY clause?",
            "options": ["WHERE", "ORDER BY", "HAVING", "LIMIT"],
            "correct": 2,
            "explanation": "HAVING filters groups created by GROUP BY, whereas WHERE filters individual rows before grouping."
        },
        {
            "id": 2,
            "question": "Which type of SQL JOIN returns all rows from the left table, and matching rows from the right table?",
            "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN"],
            "correct": 1,
            "explanation": "A LEFT JOIN returns all records from the left table and the matched records from the right table (filling NULL if unmatched)."
        },
        {
            "id": 3,
            "question": "What does ACID stand for in Database Management Systems?",
            "options": ["Atomicity, Consistency, Isolation, Durability", "Action, Control, Integrity, Data", "Access, Concurrency, Index, Database", "Accuracy, Security, Isolation, Delivery"],
            "correct": 0,
            "explanation": "ACID stands for Atomicity, Consistency, Isolation, and Durability — the 4 fundamental properties of reliable database transactions."
        },
        {
            "id": 4,
            "question": "Which SQL command is used to remove all records from a table without deleting the table structure?",
            "options": ["DROP TABLE", "TRUNCATE TABLE", "ALTER TABLE", "REMOVE TABLE"],
            "correct": 1,
            "explanation": "TRUNCATE TABLE quickly removes all rows from a table while keeping the table structure and column definitions intact."
        },
        {
            "id": 5,
            "question": "What is a Foreign Key in a relational database?",
            "options": ["A key that encrypts user data", "A field in one table that uniquely identifies a row in another table", "The first column in every table", "A key generated by external cloud APIs"],
            "correct": 1,
            "explanation": "A Foreign Key is a field (or collection of fields) in one table that refers to the Primary Key in another table, establishing relational integrity."
        }
    ]
}


class InterviewService:
    """Manages practice MCQ questions, evaluations, and score recording."""

    @staticmethod
    def get_subjects() -> List[str]:
        return list(QUESTION_BANKS.keys())

    @staticmethod
    def get_test_questions(subject: str) -> List[Dict[str, Any]]:
        questions = QUESTION_BANKS.get(subject.upper(), QUESTION_BANKS.get("JAVA", []))
        # Return without revealing correct answer index to frontend
        clean = []
        for q in questions:
            clean.append({
                "id": q["id"],
                "question": q["question"],
                "options": q["options"]
            })
        return clean

    @staticmethod
    def evaluate_test(subject: str, answers: Dict[str, int], user_id: Optional[int] = None) -> Dict[str, Any]:
        """
        Evaluates submitted answers, calculates score, and saves to InterviewTest table.
        """
        subject_key = subject.upper() if subject.upper() in QUESTION_BANKS else "C"
        questions = QUESTION_BANKS.get(subject_key, [])
        total = len(questions)
        correct_count = 0
        detailed_results = []

        for q in questions:
            qid_str = str(q["id"])
            user_choice = answers.get(qid_str)
            is_correct = (user_choice == q["correct"])
            if is_correct:
                correct_count += 1

            detailed_results.append({
                "id": q["id"],
                "question": q["question"],
                "options": q["options"],
                "user_choice": user_choice,
                "correct_choice": q["correct"],
                "is_correct": is_correct,
                "explanation": q["explanation"]
            })

        score_pct = round((correct_count / max(total, 1)) * 100)
        result_status = "Pass" if score_pct >= 60 else "Needs Practice"

        # Record in database if user is logged in
        test_record = None
        if user_id:
            try:
                test_record = InterviewTest(
                    user_id=user_id,
                    subject=subject_key,
                    score=score_pct,
                    total_questions=total,
                    result=result_status,
                    test_date=datetime.utcnow()
                )
                db.session.add(test_record)
                db.session.commit()
            except Exception:
                db.session.rollback()

        return {
            "subject": subject_key,
            "total_questions": total,
            "correct_count": correct_count,
            "score": score_pct,
            "result": result_status,
            "detailed_results": detailed_results,
            "saved": bool(test_record is not None)
        }
