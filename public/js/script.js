// ========================================
// NAVIGATION AND HAMBURGER MENU
// ========================================

const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');
const navLinks = document.querySelectorAll('.nav-link');

// Toggle menu
hamburger.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    hamburger.classList.toggle('active');
});

// Close menu when clicking on a link
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        hamburger.classList.remove('active');
    });
});

// ========================================
// NAVBAR SCROLL EFFECT
// ========================================

const navbar = document.querySelector('.navbar');
let lastScrollTop = 0;

window.addEventListener('scroll', () => {
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > 100) {
        navbar.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.15)';
    } else {
        navbar.style.boxShadow = 'var(--shadow-md)';
    }

    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop; // For mobile or negative scrolling
});

// ========================================
// ACTIVE LINK INDICATOR
// ========================================

const sections = document.querySelectorAll('section');

window.addEventListener('scroll', () => {
    let current = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').slice(1) === current) {
            link.classList.add('active');
        }
    });
});

// ========================================
// CONTACT FORM
// ========================================

const contactForm = document.getElementById('contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const subject = document.getElementById('subject').value.trim();
        const message = document.getElementById('message').value.trim();

        // Simple validation
        if (!name || !email || !subject || !message) {
            showFormStatus('Please fill in all fields', 'error');
            return;
        }

        if (!isValidEmail(email)) {
            showFormStatus('Please enter a valid email address', 'error');
            return;
        }

        // Disable submit button
        const submitBtn = contactForm.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;
        submitBtn.disabled = true;
        submitBtn.textContent = 'Sending...';

        try {
            const response = await fetch('/api/contact', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name, email, subject, message })
            });

            const data = await response.json();

            if (response.ok && data.success) {
                showFormStatus(data.message, 'success');
                contactForm.reset();
            } else {
                showFormStatus(data.error || 'An error occurred', 'error');
            }
        } catch (error) {
            console.error('Error:', error);
            showFormStatus('Error sending message', 'error');
        } finally {
            submitBtn.disabled = false;
            submitBtn.textContent = originalText;
        }
    });
}

function showFormStatus(message, type) {
    const statusDiv = document.getElementById('form-status');
    statusDiv.textContent = message;
    statusDiv.className = `form-status ${type}`;
    statusDiv.style.display = 'block';

    if (type === 'success') {
        setTimeout(() => {
            statusDiv.style.display = 'none';
        }, 5000);
    }
}

function isValidEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// ========================================
// SCROLL ANIMATIONS
// ========================================

const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeIn 0.6s ease forwards';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observer les cartes
document.querySelectorAll('.education-card, .certification-card, .skill-category, .stat').forEach(el => {
    observer.observe(el);
});

// ========================================
// DARK MODE (OPTIONNEL)
// ========================================

let darkMode = localStorage.getItem('darkMode') === 'true';

function toggleDarkMode() {
    darkMode = !darkMode;
    localStorage.setItem('darkMode', darkMode);
    applyDarkMode();
}

function applyDarkMode() {
    if (darkMode) {
        document.body.style.backgroundColor = 'var(--dark-bg)';
        document.body.style.color = 'white';
        document.querySelector('.navbar').style.background = 'rgba(15, 23, 42, 0.95)';
        document.querySelector('.navbar').style.color = 'white';
    } else {
        document.body.style.backgroundColor = 'var(--light-bg)';
        document.body.style.color = 'var(--text-dark)';
        document.querySelector('.navbar').style.background = 'rgba(255, 255, 255, 0.95)';
        document.querySelector('.navbar').style.color = 'var(--text-dark)';
    }
}

// Appliquer le mode sombre au chargement
if (darkMode) {
    applyDarkMode();
}

// ========================================
// SMOOTH SCROLL
// ========================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#') {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                const offsetTop = target.offsetTop - 80;
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        }
    });
});

// ========================================
// LOADER D'ANIMATION AU CHARGEMENT
// ========================================

window.addEventListener('load', () => {
    document.body.style.opacity = '1';
});

// ========================================
// COUNTING ANIMATION POUR LES STATS
// ========================================

const stats = document.querySelectorAll('.stat h3');
let hasAnimated = false;

const statObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting && !hasAnimated) {
            hasAnimated = true;
            stats.forEach(stat => {
                const target = parseInt(stat.textContent);
                const increment = target / 30;
                let current = 0;

                const timer = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        stat.textContent = target + '+';
                        clearInterval(timer);
                    } else {
                        stat.textContent = Math.floor(current) + '+';
                    }
                }, 30);
            });
            statObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

document.querySelector('.about-stats')?.parentElement && 
    statObserver.observe(document.querySelector('.about-stats'));

// ========================================
// UTILITÉS
// ========================================

// Log pour confirmer que le script est chargé
console.log('Portfolio script loaded successfully!');
