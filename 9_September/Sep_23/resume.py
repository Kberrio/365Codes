from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def resume():
    resume_data = {
        'name': 'John Doe',
        'title': 'Software Developer',
        'summary': 'Experienced software developer with a passion for creating efficient and scalable web applications.',
        'experience': [
            {
                'title': 'Senior Software Developer',
                'company': 'Tech Corp',
                'period': '2018 - Present',
                'description': 'Lead development of enterprise-level web applications using Python and JavaScript.'
            },
            {
                'title': 'Software Developer',
                'company': 'StartUp Inc',
                'period': '2015 - 2018',
                'description': 'Developed and maintained various web applications using Flask and React.'
            }
        ],
        'education': [
            {
                'degree': 'Bachelor of Science in Computer Science',
                'institution': 'University of Technology',
                'year': '2015'
            }
        ],
        'skills': ['Python', 'Flask', 'JavaScript', 'React', 'SQL', 'Git']
    }
    return render_template('resume.html', resume=resume_data)

if __name__ == '__main__':
    app.run(debug=True)

# Save this in a file named 'resume.html' in a 'templates' folder
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ resume.name }} - Resume</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 20px; }
        .container { max-width: 800px; margin: auto; }
        h1, h2 { color: #333; }
        .section { margin-bottom: 20px; }
        .job, .education { margin-bottom: 15px; }
        .skills { display: flex; flex-wrap: wrap; }
        .skill { background-color: #f4f4f4; padding: 5px 10px; margin: 5px; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{ resume.name }}</h1>
        <h2>{{ resume.title }}</h2>
        
        <div class="section">
            <h3>Summary</h3>
            <p>{{ resume.summary }}</p>
        </div>
        
        <div class="section">
            <h3>Experience</h3>
            {% for job in resume.experience %}
                <div class="job">
                    <h4>{{ job.title }} at {{ job.company }}</h4>
                    <p>{{ job.period }}</p>
                    <p>{{ job.description }}</p>
                </div>
            {% endfor %}
        </div>
        
        <div class="section">
            <h3>Education</h3>
            {% for edu in resume.education %}
                <div class="education">
                    <h4>{{ edu.degree }}</h4>
                    <p>{{ edu.institution }}, {{ edu.year }}</p>
                </div>
            {% endfor %}
        </div>
        
        <div class="section">
            <h3>Skills</h3>
            <div class="skills">
                {% for skill in resume.skills %}
                    <span class="skill">{{ skill }}</span>
                {% endfor %}
            </div>
        </div>
    </div>
</body>
</html>
"""