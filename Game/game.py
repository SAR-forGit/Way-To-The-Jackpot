from js import document
from js import Audio, document
from pyscript import document
import random

# from pyodide.ffi import create_once_callable
# from js import setTimeout

####################################################### Question Part ################################################################################
const question1 = [
    {
        question: "Which bird is known for its colorful feathers and tail?",
        answers: [
            {text: "A. Parrot", correct: false},
            {text: "B. Peacock", correct: true},
            {text: "C. Crow", correct: false},
            {text: "D. Sparrow", correct: false},
        ]
    },

    {
        question: "Which of these is a color of the rainbow?",
        answers: [
            {text: "A. Pink", correct: false},
            {text: "B. Orange", correct: true},
            {text: "C. Brown", correct: false},
            {text: "D. Purple", correct: false},
        ]
    },

    {
        question: "What does the acronym `HTML` stand for in web development?",
        answers: [
            {text: "A. HyperText Markup Language", correct: true},
            {text: "B. Hyper Transfer Machine Language", correct: false},
            {text: "C. High Tech Markup Language", correct: false},
            {text: "D. Hyperlink Text Management Language", correct: false},
        ]
    },

    {
        question: "Which of the following programming languages is primarily used for building Android mobile applications?",
        answers: [
            {text: "A. Python", correct: false},
            {text: "B. Swift", correct: false},
            {text: "C. Java", correct: true},
            {text: "D. Ruby", correct: false},
        ]
    },

    {
        question: "In object-oriented programming, what is the term used for a function that belongs to a class?",
        answers: [
            {text: "A. Object", correct: false},
            {text: "B. Constructor", correct: false},
            {text: "C. Method", correct: true},
            {text: "D. Instance", correct: false},
        ]
    },

    {
        question: "Which country is the largest producer of tea?",
        answers: [
            {text: "A. India", correct: false},
            {text: "B. China", correct: true},
            {text: "C. Kenya", correct: false},
            {text: "D. Sri Lanka", correct: false},
        ]
    },

    {
        question: "Which element has the chemical symbol `O`?",
        answers: [
            {text: "A. Oxygen", correct: true},
            {text: "B. Osmium", correct: false},
            {text: "C. Ozone", correct: false},
            {text: "D. Oganesson", correct: false},
        ]
    },
]

const question2 = [
    {
        question: "The currency of the United Kingdom is called?",
        answers: [
            {text: "A. Dollar", correct: false},
            {text: "B. Pound", correct: true},
            {text: "C. Euro", correct: false},
            {text: "D. Franc", correct: false},
        ]
    },

    {
        question: "Which of the following is used to declare a constant variable in JavaScript?",
        answers: [
            {text: "A. const", correct: true},
            {text: "B. let", correct: false},
            {text: "C. final", correct: false},
            {text: "D. var", correct: false},
        ]
    },

    {
        question: "Which of the following is NOT a valid data type in Python?",
        answers: [
            {text: "A. List", correct: false},
            {text: "B. Dictionary", correct: false},
            {text: "C. Array", correct: true},
            {text: "D. Tuple", correct: false},
        ]
    },

    {
        question: "Which sorting algorithm has the best average-case time complexity of O(n log n)?",
        answers: [
            {text: "A. QuickSort", correct: false},
            {text: "B. BubbleSort", correct: false},
            {text: "C. MergeSort", correct: true},
            {text: "D. InsertionSort", correct: false},
        ]
    },

    {
        question: "Who is the author of the famous novel `1984`?",
        answers: [
            {text: "A.  Aldous Huxley", correct: false},
            {text: "B. George Orwell", correct: true},
            {text: "C. J.D. Salinger", correct: false},
            {text: "D. William Golding", correct: false},
        ]
    },

    {
        question: "Who was the first Indian to win an individual Olympic gold medal?",
        answers: [
            {text: "A. Milkha Singh", correct: false},
            {text: "B. Vishwanathan Anand", correct: false},
            {text: "C. Abhinav Bindra", correct: true},
            {text: "D. Rajyavardhan Singh Rathore", correct: false},
        ]
    },

    {
        question: "The capital of the United States is??",
        answers: [
            {text: "A.  New York", correct: false},
            {text: "B. Washington, D.C.", correct: true},
            {text: "C. Los Angeles", correct: false},
            {text: "D. Chicago", correct: false},
        ]
    }
]


const question3 = [
    {
        question: "What is the chemical symbol for gold?",
        answers: [
            {text: "A. Au", correct: true},
            {text: "B. Ag", correct: false},
            {text: "C. Fe", correct: false},
            {text: "D. Pb", correct: false},
        ]
    },

    {
        question: "Which programming language is known as the `language of the web`?",
        answers: [
            {text: "A. Java", correct: false},
            {text: "B. Python", correct: false},
            {text: "C. HTML", correct: true},
            {text: "D. C++", correct: false},
        ]
    },

    {
        question: "Which of the following is used to define a class in Python?",
        answers: [
            {text: "A. class", correct: true},
            {text: "B. function", correct: false},
            {text: "C. def", correct: false},
            {text: "D. object", correct: false},
        ]
    },

    {
        question: "In SQL, which command is used to remove a table from a database?",
        answers: [
            {text: "A. DELETE", correct: false},
            {text: "B. REMOVE", correct: false},
            {text: "C. DROP", correct: true},
            {text: "D. TRUNCATE", correct: false},
        ]
    },

    {
        question: "What is the name of the Indian national parliament building?",
        answers: [
            {text: "A. Rashtrapati Bhavan", correct: false},
            {text: "B. Lok Sabha", correct: false},
            {text: "C. Rajya Sabha", correct: false},
            {text: "D. Sansad Bhavan", correct: true},
        ]
    },

    {
        question: "What is the name of the largest desert in the world?",
        answers: [
            {text: "A. Sahara", correct: false},
            {text: "B. Kalahari", correct: false},
            {text: "C. Gobi", correct: false},
            {text: "D. Antarctic Desert", correct: true},
        ]
    },

    {
        question: "Which instrument is played using a bow?",
        answers: [
            {text: "A. Guitar", correct: false},
            {text: "B. Violin", correct: true},
            {text: "C. Trumpet", correct: false},
            {text: "D. Flute", correct: false},
        ]
    }
]

const question4 = [
    {
        question: "Who was the first President of India?",
        answers: [
            {text: "A. Jawaharlal Nehru", correct: false},
            {text: "B. Rajendra Prasad", correct: true},
            {text: "C. Sardar Vallabhbhai Patel", correct: false},
            {text: "D. Dr. Zakir Husain", correct: false},
        ]
    },

    {
        question: "What does the acronym `API stand for in software development?",
        answers: [
            {text: "A. Automated Process Interface", correct: false},
            {text: "B. Application Programming Interface", correct: true},
            {text: "C. Automated Programming Interface", correct: false},
            {text: "D. Application Process Interface", correct: false},
        ]
    },

    {
        question: "Which of the following is a correct way to declare a function in JavaScript?",
        answers: [
            {text: "A. function myFunction() { }", correct: true},
            {text: "B. func myFunction() { }", correct: false},
            {text: "C. def myFunction() { }", correct: false},
            {text: "D. function: myFunction() { }", correct: false},
        ]
    },

    {
        question: "In which programming language was the first version of the Linux operating system written?",
        answers: [
            {text: "A. C", correct: true},
            {text: "B. C++", correct: false},
            {text: "C. Java", correct: false},
            {text: "D. Python", correct: false},
        ]
    },

    {
        question: "What is the national flower of Japan?",
        answers: [
            {text: "A. Rose", correct: false},
            {text: "B. Lotus", correct: false},
            {text: "C. Orchid", correct: false},
            {text: "D. Cherry Blossom", correct: true},
        ]
    },

    

    {
        question: "Which Indian city is known as the `City of Joy`?",
        answers: [
            {text: "A. Delhi", correct: false},
            {text: "B. Mumbai", correct: false},
            {text: "C. Kolkata", correct: true},
            {text: "D. Bangalore", correct: false},
        ]
    },

    {
        question: "Which element is represented by the symbol `Na`?",
        answers: [
            {text: "A. Nitrogen", correct: false},
            {text: "B. Sodium", correct: true},
            {text: "C. Neon", correct: false},
            {text: "D. Nickel", correct: false},
        ]
    }
]

const question5 = [
    {
        question: "What is the tallest mountain in the world?",
        answers: [
            {text: "A. K2", correct: false},
            {text: "B. Mount Everest", correct: true},
            {text: "C. Mount Kilimanjaro", correct: false},
            {text: "D. Mount Fuji", correct: false},
        ]
    },

    {
        question: "In which year did India become a republic?",
        answers: [
            {text: "A. 1947", correct: false},
            {text: "B. 1949", correct: false},
            {text: "C. 1950", correct: true},
            {text: "D. 1952", correct: false},
        ]
    },


    {
        question: "Which of the following is used to declare a variable in JavaScript?",
        answers: [
            {text: "A. var", correct: false},
            {text: "B. let", correct: false},
            {text: "C. const", correct: false},
            {text: "D. All are correct", correct: true},
        ]
    },

    {
        question: "What does the === operator do in JavaScript?",
        answers: [
            {text: "A. Compares both value and type", correct: true},
            {text: "B. Compares only value", correct: false},
            {text: "C. Checks for equality of variables", correct: false},
            {text: "D. Checks if two strings are equal", correct: false},
        ]
    },

    {
        question: "Which of the following is an example of a high-level programming language?",
        answers: [
            {text: "A. Assembly", correct: false},
            {text: "B. Machine code", correct: false},
            {text: "C. Python", correct: true},
            {text: "D. Binary", correct: false},
        ]
    },

    {
        question: "What is the official language of Brazil??",
        answers: [
            {text: "A. Spanish", correct: false},
            {text: "B. Portuguese", correct: true},
            {text: "C. French", correct: false},
            {text: "D. Italian", correct: false},
        ]
    },

    {
        question: "Which is the largest ocean on Earth?",
        answers: [
            {text: "A. Atlantic Ocean", correct: false},
            {text: "B. Indian Ocean", correct: false},
            {text: "C. Pacific Ocean", correct: true},
            {text: "D. Arctic Ocean", correct: false},
        ]
    }
]

const question6 = [
    {
        question: "Who was the first woman Prime Minister of the United Kingdom?",
        answers: [
            {text: "A. Margaret Thatcher", correct: true},
            {text: "B. Theresa May", correct: false},
            {text: "C. Indira Gandhi", correct: false},
            {text: "D. Queen Elizabeth II", correct: false},
        ]
    },

    {
        question: "In C++, which of the following is used for dynamic memory allocation?",
        answers: [
            {text: "A. malloc()", correct: false},
            {text: "B. alloc()", correct: false},
            {text: "C. calloc()", correct: false},
            {text: "D. new", correct: true},
        ]
    },
    
    {
        question: "Which of the following is NOT a correct way to define a function in Python?",
        answers: [
            {text: "A. def myFunction():", correct: false},
            {text: "B. function myFunction():", correct: true},
            {text: "C. def my_function():", correct: false},
            {text: "D. def function myFunction():", correct: false},
        ]
    },

    {
        question: "Which of the following is a core concept of object-oriented programming (OOP)?",
        answers: [
            {text: "A. Abstraction", correct: true},
            {text: "B. Procedural programming", correct: false},
            {text: "C. Functional programming", correct: false},
            {text: "D. Data processing", correct: false},
        ]
    },

    {
        question: "The Taj Mahal is made of which type of stone?",
        answers: [
            {text: "A. Granite", correct: false},
            {text: "B. Marble", correct: true},
            {text: "C. Limestone", correct: false},
            {text: "D. Sandstone", correct: false},
        ]
    },

    {
        question: "What is the capital city of Australia?",
        answers: [
            {text: "A. Sydney", correct: false},
            {text: "B. Melbourne", correct: false},
            {text: "C. Brisbane", correct: false},
            {text: "D. Canberra", correct: true},
        ]
    },

    {
        question: "Who painted the Mona Lisa?",
        answers: [
            {text: "A. Michelangelo", correct: false},
            {text: "B. Pablo Picasso", correct: false},
            {text: "C. Leonardo da Vinci", correct: true},
            {text: "D. Vincent van Gogh", correct: false},
        ]
    }
]

const question7 = [
    {
        question: "The currency of which country is called the ‘Yuan’?",
        answers: [
            {text: "A. Japan", correct: false},
            {text: "B. China", correct: true},
            {text: "C. South Korea", correct: false},
            {text: "D. Taiwan", correct: false},
        ]
    },

    {
        question: "Who invented the first practical telephone?",
        answers: [
            {text: "A. Nikola Tesla", correct: false},
            {text: "B. Thomas Edison", correct: false},
            {text: "C. Alexander Graham Bell", correct: true},
            {text: "D. Michael Faraday", correct: false},
        ]
    },

    {
        question: "Who was the first emperor of the Mughal Empire?",
        answers: [
            {text: "A. Akbar", correct: false},
            {text: "B. Humayun", correct: false},
            {text: "C. Babur", correct: true},
            {text: "D. Shah Jahan", correct: false},
        ]
    },

    {
        question: "Who is credited with developing the theory of evolution?",
        answers: [
            {text: "A. Charles Darwin", correct: true},
            {text: "B. Albert Einstein", correct: false},
            {text: "C. Isaac Newton", correct: false},
            {text: "D. Louis Pasteur", correct: false},
        ]
    }
]

const question8 = [
    {
        question: "What is the national flower of India?",
        answers: [
            {text: "A. Rose", correct: false},
            {text: "B. Lotus", correct: true},
            {text: "C. Jasmine", correct: false},
            {text: "D. Sunflower", correct: false},
        ]
    },

    {
        question: "In which year did India successfully test its first nuclear bomb?",
        answers: [
            {text: "A. 1971", correct: false},
            {text: "B. 1991", correct: false},
            {text: "C. 1998", correct: true},
            {text: "D. 2001", correct: false},
        ]
    },

    {
        question: "Who was the first woman to win a Nobel Prize?",
        answers: [
            {text: "A. Marie Curie", correct: true},
            {text: "B. Rosalind Franklin", correct: false},
            {text: "C. Ada Lovelace", correct: false},
            {text: "D. Florence Nightingale", correct: false},
        ]
    },

    {
        question: "What is the largest planet in our solar system?",
        answers: [
            {text: "A. Earth", correct: false},
            {text: "B. Mars", correct: false},
            {text: "C. Saturn", correct: false},
            {text: "D. Jupiter", correct: true},
        ]
    }
]

const question9 = [
    {
        question: "Who invented the telephone?",
        answers: [
            {text: "A. Thomas Edison", correct: false},
            {text: "B. Nikola Tesla", correct: false},
            {text: "C. Alexander Graham Bell", correct: true},
            {text: "D. Guglielmo Marconi", correct: false},
        ]
    },

    {
        question: "Which river is known as the longest river in the world?",
        answers: [
            {text: "A. Amazon", correct: false},
            {text: "B. Nile", correct: true},
            {text: "C. Ganges", correct: false},
            {text: "D. Yangtze", correct: false},
        ]
    },

    {
        question: "The first Asian city to host the Summer Olympics was?",
        answers: [
            {text: "A. Tokyo", correct: true},
            {text: "B. Beijing", correct: false},
            {text: "C. Seoul", correct: false},
            {text: "D. New Delhi", correct: false},
        ]
    },

    {
        question: "Who is the founder of the Facebook social media platform?",
        answers: [
            {text: "A. Steve Jobs", correct: false},
            {text: "B. Jeff Bezos", correct: false},
            {text: "C. Mark Zuckerberg", correct: true},
            {text: "D. Larry Page", correct: false},
        ]
    }
]

const question10 = [
    {
        question: "Which of the following countries does not have a royal family?",
        answers: [
            {text: "A. United Kingdom", correct: false},
            {text: "B. Spain", correct: false},
            {text: "C. Thailand", correct: false},
            {text: "D. United States", correct: true},
        ]
    },

    {
        question: "Which country hosted the first FIFA World Cup in 1930?",
        answers: [
            {text: "A. Italy", correct: false},
            {text: "B. Brazil", correct: false},
            {text: "C. France", correct: false},
            {text: "D. Uruguay", correct: true},
        ]
    },

    {
        question: "Who was the first woman to win a Nobel Prize?",
        answers: [
            {text: "A. Florence Nightingale", correct: false},
            {text: "B. Marie Curie", correct: true},
            {text: "C. Mother Teresa", correct: false},
            {text: "D. Rosalind Franklin", correct: false},
        ]
    },

    {
        question: "In which year was the first artificial satellite, Sputnik 1, launched?",
        answers: [
            {text: "A. 1957", correct: true},
            {text: "B. 1961", correct: false},
            {text: "C. 1969", correct: false},
            {text: "D. 1947", correct: false},
        ]
    },

    {
        question: "Who is considered the `father of modern chemistry`?",
        answers: [
            {text: "A. Albert Einstein", correct: false},
            {text: "B. Antoine Lavoisier", correct: true},
            {text: "C. Dmitri Mendeleev", correct: false},
            {text: "D. Isaac Newton", correct: false},
        ]
    },
    
    {
        question: "Who was the first man to walk on the moon?",
        answers: [
            {text: "A. Neil Armstrong", correct: true},
            {text: "B. Buzz Aldrin", correct: false},
            {text: "C. John Glenn", correct: false},
            {text: "D. Alan Shepard", correct: false},
        ]
    }
]

const question11 = [
    {
        question: "Who composed the famous symphony “Ode to Joy”?",
        answers: [
            {text: "A. Ludwig van Beethoven", correct: true},
            {text: "B. Wolfgang Amadeus Mozart", correct: false},
            {text: "C. Johannes Brahms", correct: false},
            {text: "D. Franz Schubert", correct: false},
        ]
    },

    {
        question: "Which scientist is credited with the discovery of the structure of DNA?",
        answers: [
            {text: "A. Gregor Mendel", correct: false},
            {text: "B. James Watson and Francis Crick", correct: true},
            {text: "C. Charles Darwin", correct: false},
            {text: "D. Albert Einstein", correct: false},
        ]
    },

    {
        question: "Who is known as the “Father of the Nation” in the United States?",
        answers: [
            {text: "A. George Washington", correct: true},
            {text: "B. Abraham Lincoln", correct: false},
            {text: "C. Benjamin Franklin", correct: false},
            {text: "D. Thomas Jefferson", correct: false},
        ]
    },

    {
        question: "The human body's largest organ is?",
        answers: [
            {text: "A. Brain", correct: false},
            {text: "B. Liver", correct: false},
            {text: "C. Heart", correct: false},
            {text: "D. Skin", correct: true},
        ]
    }
]

const question12 = [
    {
        question: "Which country was the first to grant women the right to vote?",
        answers: [
            {text: "A. United States", correct: false},
            {text: "B. New Zealand", correct: true},
            {text: "C. Australia", correct: false},
            {text: "D. United Kingdom", correct: false},
        ]
    },

    {
        question: "Which scientist developed the theory of general relativity?",
        answers: [
            {text: "A. Isaac Newton", correct: false},
            {text: "B. Albert Einstein", correct: true},
            {text: "C. Niels Bohr", correct: false},
            {text: "D. Michael Faraday", correct: false},
        ]
    },

        {
        question: "The Battle of Waterloo took place in which year?",
        answers: [
            {text: "A. 1812", correct: false},
            {text: "B. 1815", correct: true},
            {text: "C. 1805", correct: false},
            {text: "D. 1820", correct: false},
        ]
    },

    {
        question: "The discovery of the electron is attributed to which scientist?",
        answers: [
            {text: "A. Niels Bohr", correct: false},
            {text: "B. Albert Einstein", correct: false},
            {text: "C. J.J. Thomson", correct: true},
            {text: "D. Ernest Rutherford", correct: false},
        ]
    }
]

const question13 = [
    {
        question: "Which famous Indian leader was known as ‘Netaji’?",
        answers: [
            {text: "A. Jawaharlal Nehru", correct: false},
            {text: "B. Subhas Chandra Bose", correct: true},
            {text: "C. Bhagat Singh", correct: false},
            {text: "D. Sardar Patel", correct: false},
        ]
    },

    {
        question: "Who was the first emperor of the Mughal dynasty in India?",
        answers: [
            {text: "A. Akbar", correct: false},
            {text: "B. Shah Jahan", correct: false},
            {text: "C. Babur", correct: true},
            {text: "D. Humayun", correct: false},
        ]
    },
    
    {
        question: "Who was the first man to fly solo nonstop across the Atlantic Ocean?",
        answers: [
            {text: "A. Charles Lindbergh", correct: true},
            {text: "B. Amelia Earhart", correct: false},
            {text: "C. Orville Wright", correct: false},
            {text: "D. Yuri Gagarin", correct: false},
        ]
    },

    {
        question: "What is the capital of Canada?",
        answers: [
            {text: "A. Toronto", correct: false},
            {text: "B. Ottawa", correct: true},
            {text: "C. Vancouver", correct: false},
            {text: "D. Montreal", correct: false},
        ]
    }
]

const question14 = [
    {
        question: "The famous `Mona Lisa` painting is housed in which museum?",
        answers: [
            {text: "A. The Louvre", correct: true},
            {text: "B. The British Museum", correct: false},
            {text: "C. The Vatican Museums", correct: false},
            {text: "D. The Uffizi Gallery", correct: false},
        ]
    },

    {
        question: "Who painted the famous artwork `The Starry Night`?",
        answers: [
            {text: "A. Leonardo da Vinci", correct: false},
            {text: "B. Vincent van Gogh", correct: true},
            {text: "C. Pablo Picasso", correct: false},
            {text: "D. Claude Monet", correct: false},
        ]
    },

    {
        question: "In which year did India launch its Mars Orbiter Mission (Mangalyaan)?",
        answers: [
            {text: "A. 2012", correct: false},
            {text: "B. 2013", correct: false},
            {text: "C. 2014", correct: true},
            {text: "D. 2015", correct: false},
        ]
    },

    {
        question: "Who is considered the father of modern physics?",
        answers: [
            {text: "A. Albert Einstein", correct: false},
            {text: "B. Isaac Newton", correct: true},
            {text: "C. Nikola Tesla", correct: false},
            {text: "D. Galileo Galilei", correct: false},
        ]
    }
]

const question15 = [
    {
        question: "Which element is the rarest naturally occurring in the Earth's crust?",
        answers: [
            {text: "A. Gold", correct: false},
            {text: "B. Osmium", correct: false},
            {text: "C. Francium", correct: true},
            {text: "D. Platinum", correct: false},
        ]
    },

    {
        question: "Which planet is known as the `Morning Star` or `Evening Star`?",
        answers: [
            {text: "A. Mars", correct: false},
            {text: "B. Venus", correct: true},
            {text: "C. Jupiter", correct: false},
            {text: "D. Mercury", correct: false},
        ]
    },

    {
        question: "Which country has the highest population in the world?",
        answers: [
            {text: "A. India", correct: false},
            {text: "B. United States", correct: false},
            {text: "C. China", correct: true},
            {text: "D. Russia", correct: false},
        ]
    },

    {
        question: "The currency of which country is called the `Ringgit`?",
        answers: [
            {text: "A. Thailand", correct: false},
            {text: "B. Malaysia", correct: true},
            {text: "C. Indonesia", correct: false},
            {text: "D. Singapore", correct: false},
        ]
    }
]

const question16 = [
    {
        question: "Which city is known as the `City of Canals`?",
        answers: [
            {text: "A. Venice", correct: true},
            {text: "B. Amsterdam", correct: false},
            {text: "C. Bangkok", correct: false},
            {text: "D. Cairo", correct: false},
        ]
    },

    {
        question: "The first Nobel Prize in Literature was awarded to which author?",
        answers: [
            {text: "A. Ernest Hemingway", correct: false},
            {text: "B. Mark Twain", correct: false},
            {text: "C. Rabindranath Tagore", correct: false},
            {text: "D. Sully Prudhomme", correct: true},
        ]
    },

    {
        question: "The Battle of Plassey in 1757 was fought between the British East India Company and which ruler of Bengal?",
        answers: [
            {text: "A. Mir Jafar", correct: false},
            {text: "B. Nawab Siraj-ud-Daula", correct: true},
            {text: "C. Shuja-ud-Daula", correct: false},
            {text: "D. Ranjit Singh", correct: false},
        ]
    },

    {
        question: "What is the name of the largest moon of Saturn?",
        answers: [
            {text: "A. Europa", correct: false},
            {text: "B. Ganymede", correct: false},
            {text: "C. Titan", correct: true},
            {text: "D. Io", correct: false},
        ]
    }
]

const question17 = [
    {
        question: "In which year did India launch its first mission to Mars, `Mangalyaan`?",
        answers: [
            {text: "A. 2012", correct: false},
            {text: "B. 2013", correct: false},
            {text: "C. 2014", correct: true},
            {text: "D. 2015", correct: false},
        ]
    },

    {
        question: "Which mathematician is considered the father of modern calculus?",
        answers: [
            {text: "A. Isaac Newton", correct: false},
            {text: "B. Albert Einstein", correct: false},
            {text: "C. Carl Friedrich Gauss", correct: false},
            {text: "D. Gottfried Wilhelm Leibniz", correct: true},
        ]
    },

    {
        question: "Who is the father of Software Engineering?",
        answers: [
            {text: "A. Margaret Hamilton", correct: false},
            {text: "B. Watts S. Humphrey", correct: true},
            {text: "C. Alan Turing", correct: false},
            {text: "D. Boris Beizer", correct: false},
        ]
    },


    {
        question: "The Battle of Waterloo took place in which year?",
        answers: [
            {text: "A. 1812", correct: false},
            {text: "B. 1815", correct: true},
            {text: "C. 1805", correct: false},
            {text: "D. 1820", correct: false},
        ]
    }
]

First_question = random.choice(question1)
Second_question = random.choice(question2)
Third_question = random.choice(question3)
Fourth_question = random.choice(question4)
Fifth_question = random.choice(question5)
Sixth_question = random.choice(question6)
Seven_question = random.choice(question7)
Eight_question = random.choice(question8)
Nine_question = random.choice(question9)
Ten_question = random.choice(question10)
Eleventh_question = random.choice(question11)
Twelfth_question = random.choice(question12)
Thirteen_question = random.choice(question13)
Fourteen_question = random.choice(question14)
Fifteen_question = random.choice(question15)
Sixteen_question = random.choice(question16)
Seventeen_question = random.choice(question17)

questions = [
    First_question, Second_question, Third_question, Fourth_question,
    Fifth_question, Sixth_question, Seven_question, Eight_question,
    Nine_question, Ten_question, Eleventh_question, Twelfth_question,
    Thirteen_question, Fourteen_question, Fifteen_question, Sixteen_question,
    Seventeen_question
]

############################################################ Code Part ################################################################################


questionElement = document.querySelector("#question")
answerButtons = document.querySelector("#answer-buttons")
nextButton = document.querySelector("#next-btn")
winner = document.querySelector("#Winner_Message")


currentQuestionIndex = 0
score = 0

def Game_resetAudio():
    audio = Audio("Game_Sources/Game_resetAudio.mp3")
    audio.play()

def Game_WrongAnswer_Audio():
    audio = Audio("Game_Sources/Game_WrongAnswerAudio.mp3")
    audio.play()

def Game_RightAnswer_Audio():
    audio = Audio("Game_Sources/Game_RightAnswerAudio.mp3")
    audio.play()

def Game_WinnerAudio():
    audio = Audio("Game_Sources/Game_WinnerAudio.mp3")
    audio.play()


def startQuiz():
    global currentQuestionIndex, score
    currentQuestionIndex = 0
    score = 0
    nextButton.innerHTML = "Next"
    showQuestion()
    Game_resetAudio()

def showQuestion():
    resetState()
    currentQuestion = questions[currentQuestionIndex]
    questionNo = currentQuestionIndex + 1
    questionElement.innerHTML = f"{questionNo}. {currentQuestion['question']}"
    
    answerButtons = document.querySelector("#answer-buttons")
    for answer in currentQuestion["answers"]:
        button = document.createElement("button")
        button.innerHTML = answer["text"]
        button.classList.add("btn")
        answerButtons.appendChild(button)

        if answer["correct"]:
            #button.setAttribute("data-correct", "true")
            button.dataset.correct = answer["correct"]
        
        button.addEventListener("click", selectAnswer)

def resetState():
    winner = document.querySelector("#Winner_Message")
    winner.style.display = "none"
    nextButton = document.querySelector("#next-btn")
    nextButton.style.display = "none"
    answerButtons = document.querySelector("#answer-buttons")
    while answerButtons.firstChild:
        answerButtons.removeChild(answerButtons.firstChild)

def selectAnswer(event):
    global score
    selectedBtn = event.target
    isCorrect = selectedBtn.getAttribute("data-correct") == "true"
    if isCorrect:
        selectedBtn.classList.add("correct")
        score += 1
        nextButton.style.display = "block"
        Game_RightAnswer_Audio()

    else:
        selectedBtn.classList.add("incorrect")
        Game_WrongAnswer_Audio()

    answerButtons = document.querySelector("#answer-buttons").children #doubt
    for button in answerButtons:
        if button.getAttribute("data-correct") == "true":
            button.classList.add("correct")
        button.disabled = True


def showScore():
    resetState()
    answerButtons.innerHTML = f"You scored {score} out of {len(questions)}!"
    nextButton = document.querySelector("#next-btn")
    nextButton.innerHTML = "Play Again"
    nextButton.style.display = "block"
    winner.style.display = "block"
    Game_WinnerAudio()

def handleNextButton():
    global currentQuestionIndex
    currentQuestionIndex += 1
    if currentQuestionIndex < len(questions):
        showQuestion()
    else:
        showScore()

nextButton = document.querySelector("#next-btn")
nextButton.addEventListener("click", lambda: handleNextButton() if currentQuestionIndex < len(questions) else startQuiz())

Game_resetAudio()
startQuiz()