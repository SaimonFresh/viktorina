#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(QApplication, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup, QWidget)
from random import shuffle,randint 
app = QApplication([])

class Question():
    def __init__(self, question, right_answer, wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions_list = []
questions_list.append(
    Question('Гос.Язык бразилии','Португальский', 'Английский','Испанский','Бразильский'))
questions_list.append(
    Question('Какого цвета нет на флаге России?','Зелёный','Красный','Белый','Синий'))
questions_list.append(
    Question('Национальная хижина якутов','Ураса','Юрта','Иглу','Хата'))
questions_list.append(
    Question('какой город России находится за полярным кругом?','Мурманск','Москва','Санкт-Питербург','Якутск'))
questions_list.append(
    Question('со сколькими странами граничит Россия?','17','14','10','24'))
questions_list.append(
    Question('какой город является столицей Испании?','Севилья','Мадрид','Толедо','Гранада'))
questions_list.append(
     Question('в какой стране проживает самое большое количество человек в мире?','США','Япония','Россия','Китай')
)
     


bth_OK = QPushButton('ответить')
lb_Question = QLabel('Самый сложный вопрос в мире')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)


AnsGroupBox = QGroupBox('Результат текста')
lb_Result = QLabel('Прав ты или нет')
lb_Correct = QLabel('ответ будет тут!')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result,alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct,alignment=Qt.AlignHCenter,stretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line1.addWidget(lb_Question,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()


layout_line3.addStretch(1)
layout_line3.addWidget(bth_OK,stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1,stretch=2)
layout_card.addLayout(layout_line2,stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    bth_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    bth_OK.setText('ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res) 
    show_result()


def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов:', window.total,'\n-Правильных ответов:',window.score)
        print('Рейтинг:', (window.score/window.total*100),'%')
    else:
        if answer[1].isChecked( )or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг:', (window.score/window.total*100),'%')
def next_question():
    window.total += 1 
    print('Статистика\n-Всего вопросов:', window.total,'\n-Правильных ответов:',window.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)
def click_OK():
    if bth_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()





window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
bth_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0 
next_question()
window.show()

app.exec_()

#AnsGroupBox RadioGroup
#QtWidget
#construct