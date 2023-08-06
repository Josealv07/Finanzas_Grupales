from flask import Flask, render_template, request, redirect

app = Flask(__name__)

gastos_compartidos = []

@app.route('/')
def index():
    return render_template('index.html', gastos=gastos_compartidos)

@app.route('/agregar_gasto', methods=['POST'])
def agregar_gasto():
    concepto = request.form['concepto']
    monto = float(request.form['monto'])

    # Agregar el nuevo gasto a la lista
    gastos_compartidos.append({'concepto': concepto, 'monto': monto})

    # Redirigir a la página principal
    return redirect('/')





if __name__ == '__main__':
    app.run(debug=True)
