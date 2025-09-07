from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Simple Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        .container {
            background: white;
            width: 300px;
            margin: 100px auto;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        }
        input, select, button {
            width: 90%;
            padding: 10px;
            margin: 8px 0;
            font-size: 16px;
        }
        button {
            background: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }
        button:hover {
            background: #45a049;
        }
        h2 {
            margin-bottom: 15px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Simple Calculator</h2>
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
            <h3>Result: {{ result }}</h3>
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

