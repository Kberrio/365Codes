document.addEventListener('DOMContentLoaded', loadTasks);

document.getElementById('task-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const taskInput = document.getElementById('task-input');
    const task = taskInput.value;

    addTaskToList(task);
    saveTask(task);

    taskInput.value = '';
});

document.getElementById('task-list').addEventListener('click', function (e) {
    if (e.target.tagName === 'BUTTON') {
        const task = e.target.parentElement.textContent.slice(0, -4);
        removeTaskFromList(e.target.parentElement);
        removeTaskFromStorage(task);
    }
});

function addTaskToList(task) {
    const li = document.createElement('li');
    li.textContent = task;
    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Delete';
    li.appendChild(deleteBtn);
    document.getElementById('task-list').appendChild(li);
}

function saveTask(task) {
    let tasks = getTasksFromStorage();
    tasks.push(task);
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

function getTasksFromStorage() {
    let tasks;
    if (localStorage.getItem('tasks') === null) {
        tasks = [];
    } else {
        tasks = JSON.parse(localStorage.getItem('tasks'));
    }
    return tasks;
}

function loadTasks() {
    const tasks = getTasksFromStorage();
    tasks.forEach(task => addTaskToList(task));
}

function removeTaskFromList(taskElement) {
    taskElement.remove();
}

function removeTaskFromStorage(task) {
    let tasks = getTasksFromStorage();
    tasks = tasks.filter(t => t !== task);
    localStorage.setItem('tasks', JSON.stringify(tasks));
}
