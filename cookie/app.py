
from flask import Flask, request, render_template
from random import randint

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")
predict  = ( "Если Вы проявите инициативу, успех не заставит себя ждать.",
 "Ваши надежды и планы сбудутся сверх всяких ожиданий", 
 "Вам предлагается мечта всей жизни. Скажите да!",
 "Вас ждет приятный сюрприз.",
 "Время – ваш союзник, лучше отложить принятие важного решения хотя бы на день.",
 "Любимая песня на радио – предвестник удачи."<
 "К лету ты  подрастешь на 2 см",
 "Смейся всегда беспечно, чтобы счастье длилось вечно.",
 "Если в течение 15 секунд не крикнешь 'УРА', то все пропало!",
 "Не хочешь сладкого? Пей сухое!",
 "Обратите внимание на брюнетку напротив",  
 "К осени чувства не ослабнут, а станут сильнее.",
 )
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def get_predict():
    a = predict[randint(0, len(predict)-1)]
    return render_template(
        'index.html',
        appText = a
    )


if __name__ == '__main__':
    app.run(debug = True)