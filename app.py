from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Mobile Style Calculator</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      background: linear-gradient(135deg, #1e293b, #0f172a);
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      font-family: Arial, sans-serif;
    }
    .calculator {
      background: #111827;
      padding: 20px;
      border-radius: 20px;
      box-shadow: 0px 8px 20px rgba(0,0,0,0.5);
      width: 300px;
    }
    .screen {
      width: 100%;
      height: 60px;
      background: #0f172a;
      color: white;
      font-size: 28px;
      border: none;
      text-align: right;
      padding: 10px;
      border-radius: 10px;
      margin-bottom: 15px;
    }
    .buttons {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
    }
    button {
      padding: 20px;
      font-size: 20px;
      border: none;
      border-radius: 12px;
      background: #1e293b;
      color: white;
      cursor: pointer;
      transition: 0.2s;
    }
    button:hover {
      background: #334155;
      transform: scale(1.05);
    }
    .equal {
      background: #4ade80;
      color: black;
      font-weight: bold;
    }
    .equal:hover {
      background: #22c55e;
    }
    .operator {
      background: #f97316;
      color: white;
      font-weight: bold;
    }
    .operator:hover {
      background: #ea580c;
    }
  </style>
</head>
<body>
  <div class="calculator">
    <input type="text" class="screen" id="screen" disabled>
    <div class="buttons">
      <button onclick="clearScreen()">C</button>
      <button onclick="appendValue('/')">÷</button>
      <button onclick="appendValue('*')">×</button>
      <button onclick="backspace()">⌫</button>

      <button onclick="appendValue('7')">7</button>
      <button onclick="appendValue('8')">8</button>
      <button onclick="appendValue('9')">9</button>
      <button onclick="appendValue('-')" class="operator">-</button>

      <button onclick="appendValue('4')">4</button>
      <button onclick="appendValue('5')">5</button>
      <button onclick="appendValue('6')">6</button>
      <button onclick="appendValue('+')" class="operator">+</button>

      <button onclick="appendValue('1')">1</button>
      <button onclick="appendValue('2')">2</button>
      <button onclick="appendValue('3')">3</button>
      <button onclick="calculate()" class="equal">=</button>

      <button onclick="appendValue('0')">0</button>
      <button onclick="appendValue('.')">.</button>
    </div>
  </div>

  <script>
    const screen = document.getElementById('screen');

    function appendValue(value) {
      screen.value += value;
    }

    function clearScreen() {
      screen.value = '';
    }

    function backspace() {
      screen.value = screen.value.slice(0, -1);
    }

    function calculate() {
      try {
        screen.value = eval(screen.value);
      } catch {
        screen.value = 'Error';
      }
    }
  </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)

