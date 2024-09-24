const express = require('express');
const app = express();
const port = 3000;

// Set EJS as the view engine
app.set('view engine', 'ejs');

// Serve static files from the 'public' directory
app.use(express.static('public'));

app.get('/', (req, res) => {
    const resumeData = {
        name: 'John Doe',
        title: 'Software Developer',
        summary: 'Experienced software developer with a passion for creating efficient and scalable web applications.',
        experience: [
            {
                title: 'Senior Software Developer',
                company: 'Tech Corp',
                period: '2018 - Present',
                description: 'Lead development of enterprise-level web applications using Node.js and React.'
            },
            {
                title: 'Software Developer',
                company: 'StartUp Inc',
                period: '2015 - 2018',
                description: 'Developed and maintained various web applications using Express.js and Vue.js.'
            }
        ],
        education: [
            {
                degree: 'Bachelor of Science in Computer Science',
                institution: 'University of Technology',
                year: '2015'
            }
        ],
        skills: ['JavaScript', 'Node.js', 'Express.js', 'React', 'MongoDB', 'Git']
    };

    res.render('resume', { resume: resumeData });
});

app.listen(port, () => {
    console.log(`Resume website listening at http://localhost:${port}`);
});

// Save this in a file named 'resume.ejs' in a 'views' folder
/*
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><%= resume.name %> - Resume</title>
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
        <h1><%= resume.name %></h1>
        <h2><%= resume.title %></h2>
        
        <div class="section">
            <h3>Summary</h3>
            <p><%= resume.summary %></p>
        </div>
        
        <div class="section">
            <h3>Experience</h3>
            <% resume.experience.forEach(function(job) { %>
                <div class="job">
                    <h4><%= job.title %> at <%= job.company %></h4>
                    <p><%= job.period %></p>
                    <p><%= job.description %></p>
                </div>
            <% }); %>
        </div>
        
        <div class="section">
            <h3>Education</h3>
            <% resume.education.forEach(function(edu) { %>
                <div class="education">
                    <h4><%= edu.degree %></h4>
                    <p><%= edu.institution %>, <%= edu.year %></p>
                </div>
            <% }); %>
        </div>
        
        <div class="section">
            <h3>Skills</h3>
            <div class="skills">
                <% resume.skills.forEach(function(skill) { %>
                    <span class="skill"><%= skill %></span>
                <% }); %>
            </div>
        </div>
    </div>
</body>
</html>
*/