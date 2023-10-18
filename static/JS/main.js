document.addEventListener("DOMContentLoaded", function() {
    // Selectors
    const toDoInput = document.querySelector('.todo-input');
    const toDoBtn = document.querySelector('.todo-btn');
    const standardTheme = document.querySelector('.standard-theme');
    const lightTheme = document.querySelector('.light-theme');
    const darkerTheme = document.querySelector('.darker-theme');

    // Check if one theme has been set previously and apply it (or std theme if not found):
    let savedTheme = localStorage.getItem('savedTheme');
    savedTheme === null ?
        changeTheme('standard')
        : changeTheme(savedTheme);

    // Event Listeners
    standardTheme.addEventListener('click', () => changeTheme('standard'));
    lightTheme.addEventListener('click', () => changeTheme('light'));
    darkerTheme.addEventListener('click', () => changeTheme('darker'));

// Functions;
// Change theme function:
function changeTheme(color) {
    localStorage.setItem('savedTheme', color);
    savedTheme = localStorage.getItem('savedTheme');

    // Change theme for body
    document.body.className = color;

    // Change input color
    toDoInput.className = `todo-input ${color}-input`;

    // Change todo color without changing their status (completed or not)
    document.querySelectorAll('.todo').forEach(todo => {
        Array.from(todo.classList).some(item => item === 'completed') ? 
            todo.className = `todo ${color}-todo completed`
            : todo.className = `todo ${color}-todo`;
    });

    // Change buttons color according to their type (todo, check, or delete)
    document.querySelectorAll('.check-btn').forEach(button => {
        button.className = `check-btn ${color}-button`;
    });

    document.querySelectorAll('.delete-btn').forEach(button => {
        button.className = `delete-btn ${color}-button`;
    });

    toDoBtn.className = `todo-btn ${color}-button`;
}
}); 