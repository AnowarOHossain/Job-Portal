function searchJobs() {
    const input = document.getElementById('searchInput').value.toLowerCase();
    const jobCards = document.querySelectorAll('#jobList > div');
    jobCards.forEach(card => {
        const title = card.querySelector('h2').textContent.toLowerCase();
        const company = card.querySelector('p').textContent.toLowerCase();
        if (title.includes(input) || company.includes(input)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

// Add scroll effect to navbar
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});