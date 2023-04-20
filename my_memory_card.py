#Библиотеки
from PyQt5.QtCore import*
from PyQt5.QtWidgets import *
from random import *
import time

#Редактирование окна
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(500,250)

#Создание Виджетов и Групп
label_que = QLabel('Вопрос')
otvet = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Вариант1')
rbtn_2 = QRadioButton('Вариант2')
rbtn_3 = QRadioButton('Вариант3')
rbtn_4 = QRadioButton('Вариант4')

ButtonGroup = QButtonGroup()
ButtonGroup.addButton(rbtn_1)
ButtonGroup.addButton(rbtn_2)
ButtonGroup.addButton(rbtn_3)
ButtonGroup.addButton(rbtn_4)

#Создание и размещение линий
layout_answer1 = QHBoxLayout()
layout_answer2 = QVBoxLayout()
layout_answer3 = QVBoxLayout()
layout_answer4 = QVBoxLayout()
layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

#-----------------------------------------
layout_answer2.addWidget(rbtn_1)
layout_answer2.addWidget(rbtn_2)
layout_answer3.addWidget(rbtn_3)
layout_answer3.addWidget(rbtn_4)
layout_answer1.addLayout(layout_answer2)
layout_answer1.addLayout(layout_answer3)
RadioGroupBox.setLayout(layout_answer1)
RadioGroupBox.show()

#===============================================
AnsGroupBox = QGroupBox('Результат теста')
win_or_not = QLabel('правильно/неправильно')
win = QLabel('Правильный ответ')
layout_answer4.addWidget(win_or_not,alignment= Qt.AlignLeft)
layout_answer4.addWidget(win,alignment= Qt.AlignCenter)
AnsGroupBox.setLayout(layout_answer4)
AnsGroupBox.hide()

#--------------------------------------------------
layoutH1.addWidget(label_que,alignment=Qt.AlignCenter)
layoutH2.addWidget(RadioGroupBox)
layoutH2.addWidget(AnsGroupBox)
layoutH3.addWidget(otvet,stretch=3)
layout_main.addLayout(layoutH1, stretch=2)
layout_main.addLayout(layoutH2, stretch=6)
layout_main.addLayout(layoutH3, stretch=2)
layout_main.setSpacing(25)
main_win.setLayout(layout_main)

#---------------------------
#Классы
class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        
#Список Вопросов
question_list = []
question_list.append(Question('как создать свою функцию в Python','def','str','int','import'))
question_list.append(Question('Что делает функция int','преобразует строку в число','преобразует число в строку','позволяет создать свою функцию','ничего'))
question_list.append(Question('Что делает функция str','преобразует число в строку','преобразует строку в число','позволяет создать свою функцию','ничего'))
question_list.append(Question('Зачем нужна библиотека Turtle','позволяет рисовать на экране с помощью черепашки','Выбирает случайное число от задоного до задоного','позволяет создавать оконные приложения','тайкой библиотеки нету'))
question_list.append(Question('Столица России','Москва','Лондон','Майкоп','Кастрома'))
question_list.append(Question('Государственный язык Бразилии','Бразильский','Португальский','Английский','Испанский'))
question_list.append(Question('Столица Бразилии','Бразилиа','Москва','Лондон','Берлин'))
question_list.append(Question('Где находиться "Красная Площадь"','Краснодар','Москва','Берлин','Каменомостк'))
question_list.append(Question('Самая маленькая планета солнечной системы','Плутон','Земля','Меркурий','Марс'))
question_list.append(Question('Сколько колец на олимпийском флаге','пять','Семь','Десять','Три'))
question_list.append(Question('Какая страна самая маленькая в мире','Ватикан','Мальдивы','Мальта','Монако'))
question_list.append(Question('Какое стихийное бедствие измеряеться по шкале Рихтера','Землетрясения','Ураган','Ничего','Наводнения'))
question_list.append(Question('"K"- это химический символ какого элемента','Калий','Титан','Водород','Силиций'))
question_list.append(Question('Какой язык програмирования самый популярный в 2022 году','Python','СС+','java','C#'))

#Функции
def show_answer():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    otvet.setText('Следующий вопрос')

#-----Функция1------
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    otvet.setText('Ответить')
    ButtonGroup.setExclusive(True)

#-----Функция2------
def show_correct(res):
    print('Статистика:')
    print('- всего вопросов',main_win.total)
    print('- правильных ответов',main_win.score)
    print('Рейтинг:',main_win.score/main_win.total*100,'%')
    show_answer()

#-----Функция3------
def check_answer():
    if answer[0].isChecked():
        main_win.score += 1
        show_correct('Правильно')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked:
            show_correct('Неправильно')

#-----Функция4------
def ask(q):
    label_que.setText(q.question)
    win.setText(q.right_answer)
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    show_question()
    question_list.remove(q)
    ButtonGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    ButtonGroup.setExclusive(True)

#-----Функция5------
def next_question():
    curent_que = randint(0,len(question_list) - 1)
    ask(question_list[curent_que])
    main_win.total += 1


#-----Функция6------
def click_OK():
    if otvet.text() == 'Ответить':
        check_answer()
    else:
        next_question()




#основная часть
answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
main_win.score = 0
main_win.total = 0
next_question()
otvet.clicked.connect(click_OK)
#Запуск приложения
main_win.show()
app.exec_()