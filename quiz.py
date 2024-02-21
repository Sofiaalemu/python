quiz = {
    "question1": {
        "question": "What is the minimum number of witnesses required for a marriage contract (Nikah)?",
        "answer": "Two"
    },
    "question2": {
        "question": "How many times is Prophet Muhammad's name mentioned in the Quran??",
        "answer": "four"
    },
   "question3": {
        "question": "How many Surahs start with the Arabic letters 'Sad'",
        "answer": "two"
    },
   "question4": {
        "question": "How many Surahs are named after Prophets in the Quran??",
        "answer": "six"
    },
"question5": {
        "question": " : Who was the companion known for her extensive knowledge of medicine and healing?",
        "answer": "Rufaidah al aslamia"
    },
"question6": {
        "question": " How many Surahs are completely revealed in Makkah??",
        "answer": "86"
    },
"question7": {
        "question": "Which Surah focuses on the story of Moses and Pharaoh (Fir'awn)??",
        "answer": "taha"
    },
"question8": {
        "question": "How many verses are in the longest Surah of the Quran?",
        "answer": "286"
    },
"question9": {
        "question": " Which companion was known as the '/Sword of Allah' due to his bravery??",
        "answer": "Khalid ibn al walid"
    },
"question10": {
        "question": " Who was the youngest companion of Prophet Muhammad??",
        "answer": "Anas ibn Malik"
    },
"question11": {
        "question": " Which companion led the funeral prayer of Prophet Muhammad?",
        "answer": "Abubekr siddiq"
    },
"question12": {
        "question": "Who was the companion known for his exceptional memorization of Hadith??",
        "answer": "Abu Hurairah"
    },
"question13": {
        "question": "Who was the youngest male companion to participate in the Battle of Badr?",
        "answer": "Usama ibn zaid"
    },
"question14": {
        "question": "Which companion was known for her bravery during the Battle of Uhud?",
        "answer": "Nusaybah bint ka'ab"
    },
"question15":{
        "question": "Who was the female companion who migrated twice for the sake of Islam?",
        "answer": "umm kulthum bint ali"

    },
"question16":{
        "question": "What is the minimum number of witnesses required for a marriage contract (Nikah)?",
        "answer": "Two"
    },
"question17":{
    "question":" How many days is the waiting period (Iddah) for a widow before she can remarry?",
    "answer": "four months and ten days"
    },
"question18":{
    "question":" What is the first month in Hijri",
    "answer": "Muharram"
    },



}

score = 0
for key, value in quiz.items():
    print(value('question'))
    answer = input('Answer?')
if answer.lower() == value[ 'answer'] . lower():
        print('Correct')
        score = score + 1
        print("Your score is: " + str(score))
        print(" ")

else:
        print("Wrong!")
        print("The answer is : " + value[' answer'])
        print("Your score is: " + str(score))
        print("")
        print("")

print("You got " + str(score) + " out of 7 questions correctly")
print("Your percentage is " + str(int(score/7 * 100)) + "%")
