from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

#2) Создай объект-приложение, окно приложения. Задай заголовок и размеры.
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('MemoryCard')
main_win.resize(600, 400)
#3) Создай виджет-вопрос и виджет-кнопку «Ответить».
question = QLabel('Какой национальности не существует')
btn = QPushButton('Ответить')
#4) Создай набор переключателей с вариантами ответов. Расположи их по лэйаутам и объедини в группу.
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1) 
#RadioGroupBox.hide()
#5) Расположи вопрос, группу переключателей и кнопку по лэйаутам.
AnsGroupBox = QGroupBox('Результат теста')
is_right = QLabel('Правильно/Не правильно')
right_answer = QLabel('Правильный ответ')
ans_layout = QVBoxLayout()
ans_layout.addWidget(is_right)
ans_layout.addWidget(right_answer, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(ans_layout)
#6) При необходимости, добавь пробелы между виджетами и выровняй их по краю/центру.
layout = QVBoxLayout()
layout.addWidget(question, alignment=Qt.AlignCenter)
layout.addWidget(RadioGroupBox)
layout.addWidget(AnsGroupBox)
layout.addWidget(btn, alignment=Qt.AlignCenter)
main_win.setLayout(layout)
#6.1) Объединение кнопок в группу
RG = QButtonGroup()
RG.addButton(rbtn_1)
RG.addButton(rbtn_2)
RG.addButton(rbtn_3)
RG.addButton(rbtn_4)
#Функция задающая вопрос
class Question():
    def __init__(self,quest, right_answer, w1, w2, w3 ):
        self.question = quest
        self.right_answer = right_answer
        self.wrong1 = w1
        self.wrong2 = w2
        self.wrong3 = w3


def ask(q):
    question.setText(q.question)
    rbtn_1.setText(q.right_answer)
    rbtn_2.setText(q.wrong1)
    rbtn_3.setText(q.wrong2)
    rbtn_4.setText(q.wrong3)
question_list = list()

question_list.append( Question('Государственный язык Бразилии',
'Португальский',
'Испанский','Итальянский','Бразильский'))

question_list.append( Question('День народного единства отмечается',
'4 ноября',
'7 октября','12 июня','31 ноября'))

question_list.append( Question('Сколько мне лет',
'13',
'10','12','11'))

question_list.append( Question('Сколько будет 2*2?',
'4',
'6','8','5'))




RadioGroupBox.show()
AnsGroupBox.hide()

main_win.total = 0
main_win.score = 0

from random import randint
def next_question():
    main_win.total += 1
    main_win.cur_question = randint(0, len(question_list)-1)
    q = question_list[main_win.cur_question]
    ask(q)           



def check_answer():
    if rbtn_1.isChecked():
        is_right.setText('Правильно')
        right_answer.setText(rbtn_1.text())
        main_win.score += 1
    else:
        is_right.setText('Не правильно')
        right_answer.setText(rbtn_1.text())
    print('Статистика')
    print('-Всего вопросов:',main_win.total)
    print('-Правильные ответы',main_win.score)
    print('Рейтинг:', main_win.score/main_win.total * 100, '%')
next_question()


ask(question_list[0])
main_win.cur_question = -1


#7) Обработчик события нажатия кнопки 'Ответить'
def show_result():
    if btn.text() == 'Следующий вопрос':
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn.setText('Ответить')
        RG.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RG.setExclusive(True)
        next_question()
    else:
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn.setText("Следующий вопрос")
        check_answer()


      
    

btn.clicked.connect(show_result)



main_win.show()
app.exec_()
