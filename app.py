from flask import Flask, request, jsonify, render_template
from question_generator import generate_question
from code_evaluator import evaluate_code
from interview_simulator import simulate_interview

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_question', methods=['POST'])
def api_generate_question():
    data = request.json
    tech_stack = data.get('tech_stack', 'Python')
    category = data.get('category', '算法')
    difficulty = data.get('difficulty', 'L3')
    question = generate_question(tech_stack, category, difficulty)
    return jsonify({'question': question})

@app.route('/evaluate_code', methods=['POST'])
def api_evaluate_code():
    data = request.json
    code = data.get('code', '')
    language = data.get('language', 'Python')
    test_cases = data.get('test_cases', [])
    evaluation = evaluate_code(code, language, test_cases)
    return jsonify(evaluation)

@app.route('/simulate_interview', methods=['POST'])
def api_simulate_interview():
    data = request.json
    initial_difficulty = data.get('difficulty', 'L3')
    interview = simulate_interview(initial_difficulty)
    return jsonify(interview)

if __name__ == '__main__':
    app.run(debug=True)