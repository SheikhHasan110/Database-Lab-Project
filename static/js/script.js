const container = document.querySelector('.container');
const registerBtn = document.querySelector('.register-btn');
const loginBtn = document.querySelector('.login-btn');

registerBtn.addEventListener('click',() => {
    container.classList.add('active');
});

loginBtn.addEventListener('click',() => {
    container.classList.remove('active');
});

// window.onload = function() {
//     const flashMessageText = document.getElementById('flash-message-text');
//     const flashMessageModal = document.getElementById('flash-message-modal');
//     if (flashMessageText && flashMessageText.innerText.trim() !== '') {
//         flashMessageModal.style.display = 'block';
//     }
// };

// function closeModal() {
//     document.getElementById('flash-message-modal').style.display = 'none';
// }

window.onload = function() {
    const flashMessageText = document.getElementById('flash-message-text');
    const flashMessageModal = document.getElementById('flash-message-modal');
    if (flashMessageText && flashMessageText.innerText.trim() !== '') {
        flashMessageModal.classList.add('show');
    }
};

function closeModal() {
    const flashMessageModal = document.getElementById('flash-message-modal');
    flashMessageModal.classList.remove('show');
    setTimeout(() => {
        flashMessageModal.style.display = 'none';
    }, 300); // Match the transition duration
}