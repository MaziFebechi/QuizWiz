# Flask Quiz App

This is a Flask-based Quiz App that allows users to answer questions based on different topics and difficulty levels. The app consists of three main pages: question selection, difficulty and username page, and the preview page.

## Features

- Question Selection: Users can choose the specific topic or category of questions they want to answer.
- Difficulty and Username Page: Users can select the difficulty level of the questions and provide their username before starting the quiz.
- Preview Page: Users can preview the selected options (topic, difficulty, and username) before starting the quiz.
- Main Quiz Page: Users will be presented with a series of questions based on their selected options. If the user selects a wrong answer, the window will turn red until the correct answer is chosen.

## Setup and Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/QuizWiz.git
```

2. Change into the project directory:

```bash
cd quiz-app
```

3. Create and activate a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Access the Quiz App in your web browser at `http://localhost:5000`.

3. Select the topic, difficulty level, and provide your username on the respective pages.

4. Preview the selected options and click "Start Quiz" to begin.

5. Answer the questions on the main quiz page. If you select a wrong answer, the window will turn red until the correct answer is chosen.

