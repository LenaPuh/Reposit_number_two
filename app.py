from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

RECORDS = [
    {"id": 1, "full_name": "Анна Иванова", "date": "25.02.2026 10:00"},
    {"id": 2, "full_name": "Олег Петров", "date": "25.02.2026 15:00"},
    {"id": 3, "full_name": "Мария Смирнова", "date": "26.02.2026 10:00"},
    {"id": 4, "full_name": "Олег Олегов", "date": "27.02.2026 12:00"}
]

@app.route('/')
def hello_world():
    hello='Hello, World!'
    return render_template("index.html", hello=hello)

@app.route("/list_records", methods=['GET', 'POST'])
def list_records(): 
    if request.method == 'POST':
        # удаляем последний элемент, если есть
        if RECORDS:
            RECORDS.pop()
        # перенаправляем, чтобы избежать повторной отправки формы при обновлении
        return redirect(url_for('list_records'))
    return render_template("list_records.html", records=RECORDS)

if __name__ == '__main__':
    app.run(debug=True)
