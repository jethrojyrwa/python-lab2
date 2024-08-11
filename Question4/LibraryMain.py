import LibraryManager as lm

books = {
    "9780134670942": {
        "title": "Operating System Concepts",
        "author": "Abraham Silberschatz, Peter B. Galvin, Greg Gagne",
        "publisher": "John Wiley & Sons",
        "volume": 10,
        "year_of_publication": 2020
    },
    "9780262045604": {
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein",
        "publisher": "MIT Press",
        "volume": 4,
        "year_of_publication": 2020
    },
    "9780135172322": {
        "title": "Operating Systems: Three Easy Pieces",
        "author": "Remzi H. Arpaci-Dusseau, Andrea C. Arpaci-Dusseau",
        "publisher": "Arpaci-Dusseau Books",
        "volume": 2,
        "year_of_publication": 2022
    },
    "9780262033847": {
        "title": "Machine Learning",
        "author": "Tom M. Mitchell",
        "publisher": "McGraw-Hill",
        "volume": 1,
        "year_of_publication": 2021
    },
    "9780134685991": {
        "title": "Data Structures and Algorithm Analysis in C++",
        "author": "Mark Allen Weiss",
        "publisher": "Pearson",
        "volume": 4,
        "year_of_publication": 2020
    },
    "9781617294532": {
        "title": "Machine Learning with Python",
        "author": "Sebastian Raschka, Vahid Mirjalili",
        "publisher": "Manning Publications",
        "volume": 2,
        "year_of_publication": 2021
    },
    "9780135166307": {
        "title": "Operating Systems: Internals and Design Principles",
        "author": "William Stallings",
        "publisher": "Pearson",
        "volume": 9,
        "year_of_publication": 2021
    },
    "9780134845636": {
        "title": "Python Machine Learning By Example",
        "author": "Yuxi (Hayden) Liu",
        "publisher": "Packt Publishing",
        "volume": 3,
        "year_of_publication": 2020
    },
    "9781492051367": {
        "title": "Data Structures and Algorithms in Python",
        "author": "Michael T. Goodrich, Roberto Tamassia, Michael H. Goldwasser",
        "publisher": "O'Reilly Media",
        "volume": 1,
        "year_of_publication": 2020
    },
    "9780134093413": {
        "title": "Operating Systems: Principles and Practice",
        "author": "Thomas Anderson, Michael Dahlin",
        "publisher": "Pearson",
        "volume": 2,
        "year_of_publication": 2021
    },
    "9781492032649": {
        "title": "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow",
        "author": "Aurélien Géron",
        "publisher": "O'Reilly Media",
        "volume": 2,
        "year_of_publication": 2020
    },
    "9781107155621": {
        "title": "Machine Learning Yearning",
        "author": "Andrew Ng",
        "publisher": "Cambridge University Press",
        "volume": 1,
        "year_of_publication": 2020
    },
    "9780135974445": {
        "title": "Python Data Structures and Algorithms",
        "author": "Benjamin Baka",
        "publisher": "Packt Publishing",
        "volume": 1,
        "year_of_publication": 2021
    },
    "9780321623218": {
        "title": "Operating Systems Design and Implementation",
        "author": "Andrew S. Tanenbaum, Albert S. Woodhull",
        "publisher": "Pearson",
        "volume": 3,
        "year_of_publication": 2021
    },
    "9781491954249": {
        "title": "Data Structures and Algorithms in Java",
        "author": "Robert Lafore",
        "publisher": "O'Reilly Media",
        "volume": 2,
        "year_of_publication": 2022
    },
    "9781492041139": {
        "title": "Deep Learning with Python",
        "author": "François Chollet",
        "publisher": "Manning Publications",
        "volume": 1,
        "year_of_publication": 2021
    },
    "9780134686097": {
        "title": "Introduction to the Design and Analysis of Algorithms",
        "author": "Anany Levitin",
        "publisher": "Pearson",
        "volume": 3,
        "year_of_publication": 2020
    },
    "9780262033848": {
        "title": "Introduction to the Theory of Computation",
        "author": "Michael Sipser",
        "publisher": "MIT Press",
        "volume": 3,
        "year_of_publication": 2023
    },
    "9781492070880": {
        "title": "Machine Learning Engineering",
        "author": "Andriy Burkov",
        "publisher": "O'Reilly Media",
        "volume": 1,
        "year_of_publication": 2022
    },
    "9780134770986": {
        "title": "Modern Operating Systems",
        "author": "Andrew S. Tanenbaum, Herbert Bos",
        "publisher": "Pearson",
        "volume": 4,
        "year_of_publication": 2021
    },
    "9781107184816": {
        "title": "Pattern Recognition and Machine Learning",
        "author": "Christopher M. Bishop",
        "publisher": "Springer",
        "volume": 1,
        "year_of_publication": 2021
    },
    "9780262043839": {
        "title": "Fundamentals of Machine Learning for Predictive Data Analytics",
        "author": "John D. Kelleher, Brian Mac Namee, Aoife D'Arcy",
        "publisher": "MIT Press",
        "volume": 2,
        "year_of_publication": 2023
    },
    "9780135957057": {
        "title": "Introduction to the Theory of Computation",
        "author": "Michael Sipser",
        "publisher": "MIT Press",
        "volume": 4,
        "year_of_publication": 2024
    },
    "9781492056235": {
        "title": "Applied Text Analysis with Python",
        "author": "Benjamin Bengfort, Rebecca Bilbro, Tony Ojeda",
        "publisher": "O'Reilly Media",
        "volume": 1,
        "year_of_publication": 2022
    },
    "9781107196949": {
        "title": "Machine Learning: A Probabilistic Perspective",
        "author": "Kevin P. Murphy",
        "publisher": "MIT Press",
        "volume": 2,
        "year_of_publication": 2021
    },
    "9780135899932": {
        "title": "Deep Learning for Natural Language Processing",
        "author": "Jason Brownlee",
        "publisher": "Machine Learning Mastery",
        "volume": 1,
        "year_of_publication": 2023
    }
}


books = lm.addBook(books,'9781234567890',"Advanced Data Structures and Algorithms in Python","John Smith","Tech Books Publishing",1,2024)
print()

books = lm.removeBook(books,'9781234567890')
print()

lm.displayBook(books,'9781107184816')
print()

lm.searchBook(books,'Introduction to the Design and Analysis of Algorithms')
print()

lm.searchBook(books,'Reema Thareja')
print()

lm.listBooks(books)
print()

lm.updateBook(books,'9780134685991',"Data Structures and Algorithm Analysis in C++","Mark Allen","Pearson","5",2024)
print()

lm.searchByISBN(books,'9781492032649')
print()
