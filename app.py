from flask import Flask, render_template_string, request

app = Flask(__name__)

# Modern HTML Template
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Modern Calculator</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background: #ffffff;
            padding: 30px;
            border-radius: 15px;
            width: 350px;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
            text-align: center;
            animation: fadeIn 1s ease-in-out;
        }
        @keyframes fadeIn {
            from {opacity: 0; transform: translateY(-20px);}
            to {opacity: 1; transform: translateY(0);}
        }
        h2 {
            color: #333333;
            margin-bottom: 20px;
            font-size: 28px;
            letter-spacing: 1px;
        }
        input, select, button {
            width: 90%;
            padding: 12px;
            margin: 10px 0;
            border: 2px solid #ddd;
            border-radius: 10px;
            font-size: 16px;
            outline: none;
            transition: 0.3s;
        }
        input:focus, select:focus {
            border-color: #667eea;
            box-shadow: 0 0 8px rgba(102,126,234,0.3);
        }
        button {
            background: #667eea;
            color: white;
            border: none;
            cursor: pointer;
            font-weight: bold;
            letter-spacing: 1px;
            transition: 0.3s;
        }
        button:hover {
            background: #5a67d8;
            transform: scale(1.05);
        }
        .result {
            margin-top: 20px;
            font-size: 20px;
            font-weight: bold;
            color: #444;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>🔢 Modern Calculator</h2>
        <form method="POST">
            <input type="number" name="num1" step="any" placeholder="Enter first number" required><br>
            <input type="number" name="num2" step="any" placeholder="Enter second number" required><br>
            <select name="operation" required>
                <option value="add">Addition (+)</option>
                <option value="subtract">Subtraction (-)</option>
                <option value="multiply">Multiplication (*)</option>
                <option value="divide">Division (/)</option>
            </select><br>
            <button type="submit">Calculate</button>
        </form>
        {% if result is not none %}
            <div class="result">Result: {{ result }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = "Error: Division by zero" if num2 == 0 else num1 / num2
        except:
            result = "Invalid input!"
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
