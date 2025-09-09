// Frecuuency Platform JavaScript

document.addEventListener('DOMContentLoaded', function() {
    console.log('🎵 Frecuuency Platform loaded - Professional DJ Interface');

    // Initialize all components
    initializeAnimations();
    initializeFilters();
    initializeSearch();
    initializePlayer();
    initializeProfessionalEffects();
    initializeParticles();
});

// ===== PROFESSIONAL EFFECTS =====
function initializeProfessionalEffects() {
    // Enhanced hover effects for glass elements
    document.querySelectorAll('.set-card, .participant-card, .featured-card').forEach(element => {
        element.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
            this.style.boxShadow = '0 0 30px rgba(108, 92, 231, 0.4), 0 20px 40px rgba(0, 0, 0, 0.3)';
        });

        element.addEventListener('mouseleave', function() {
            this.style.transform = '';
            this.style.boxShadow = '';
        });
    });

    // Dynamic navbar effects
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const navbar = document.querySelector('.navbar');

        if (scrolled > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
}

// ===== PARTICLE SYSTEM =====
function initializeParticles() {
    const particleBg = document.getElementById('particleBg');
    if (!particleBg) return;

    for (let i = 0; i < 30; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.animationDelay = Math.random() * 20 + 's';
        particle.style.animationDuration = (Math.random() * 15 + 15) + 's';

        // Random colors from our palette
        const colors = ['#6c5ce7', '#00d4ff', '#ff6b35', '#fd79a8'];
        particle.style.background = colors[Math.floor(Math.random() * colors.length)];

        particleBg.appendChild(particle);
    }
}

// ===== ANIMATIONS =====
function initializeAnimations() {
    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe all cards for scroll animations
    document.querySelectorAll('.set-card, .participant-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(50px) scale(0.9)';
        card.style.transition = 'opacity 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94), transform 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
        observer.observe(card);
    });

    // Enhanced hover effects
    document.querySelectorAll('.set-card, .participant-card').forEach((card, index) => {
        // Staggered animation delay
        card.style.animationDelay = `${index * 0.05}s`;

        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-12px) scale(1.03)';
            this.style.boxShadow = '0 0 30px rgba(108, 92, 231, 0.4), 0 25px 50px rgba(0,0,0,0.3)';
            this.style.borderColor = 'rgba(108, 92, 231, 0.5)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = '';
            this.style.boxShadow = '';
            this.style.borderColor = '';
        });
    });

    // Magnetic effect for buttons
    document.querySelectorAll('.btn, .filter-btn, .play-button').forEach(btn => {
        btn.addEventListener('mousemove', function(e) {
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;

            this.style.transform = `translate(${x * 0.15}px, ${y * 0.15}px) scale(1.05)`;
        });

        btn.addEventListener('mouseleave', function() {
            this.style.transform = '';
        });
    });
}

// ===== FILTERS =====
function initializeFilters() {
    const filterBtns = document.querySelectorAll('.filter-btn');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Add loading state
            const originalText = this.textContent;
            this.innerHTML = '<span><i class="fas fa-spinner fa-spin"></i> Cargando...</span>';

            // Reset after navigation (this won't execute due to page change, but good practice)
            setTimeout(() => {
                this.innerHTML = originalText;
            }, 100);
        });
    });
}

// ===== SEARCH =====
function initializeSearch() {
    const searchForms = document.querySelectorAll('.search-form, .search-form-page');

    searchForms.forEach(form => {
        const input = form.querySelector('input[name="q"], input[name="search"]');
        const button = form.querySelector('button');

        if (input && button) {
            // Enhanced search feedback
            input.addEventListener('input', function() {
                const query = this.value.trim();
                if (query.length > 2) {
                    console.log('🔍 Searching for:', query);

                    // Add visual feedback
                    input.parentElement.style.borderColor = '#6c5ce7';
                    input.parentElement.style.boxShadow = '0 0 30px rgba(108, 92, 231, 0.4)';
                } else {
                    input.parentElement.style.borderColor = '';
                    input.parentElement.style.boxShadow = '';
                }
            });

            // Search form submission
            form.addEventListener('submit', function() {
                const query = input.value.trim();
                if (query) {
                    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
                } else {
                    event.preventDefault();
                    input.focus();
                }
            });
        }
    });
}

// ===== MEDIA PLAYER =====
function initializePlayer() {
    // Audio player enhancements
    const audioPlayers = document.querySelectorAll('.audio-player');
    audioPlayers.forEach(player => {
        player.addEventListener('loadstart', function() {
            console.log('🎵 Loading audio...');
            showLoadingState(this);
        });

        player.addEventListener('canplay', function() {
            console.log('🎵 Audio ready to play');
            hideLoadingState(this);
        });

        player.addEventListener('error', function() {
            console.error('❌ Error loading audio');
            showErrorState(this);
        });
    });

    // Video player enhancements
    const videoPlayers = document.querySelectorAll('.video-player');
    videoPlayers.forEach(player => {
        player.addEventListener('loadstart', function() {
            console.log('🎬 Loading video...');
            showLoadingState(this);
        });

        player.addEventListener('canplay', function() {
            console.log('🎬 Video ready to play');
            hideLoadingState(this);
        });

        player.addEventListener('error', function() {
            console.error('❌ Error loading video');
            showErrorState(this);
        });
    });
}

function showLoadingState(element) {
    // Add loading indicator
    const loader = document.createElement('div');
    loader.className = 'media-loader';
    loader.innerHTML = `
        <div class="music-bars">
            <div class="music-bar"></div>
            <div class="music-bar"></div>
            <div class="music-bar"></div>
            <div class="music-bar"></div>
            <div class="music-bar"></div>
        </div>
        <p style="margin-top: 16px; color: #6c5ce7; font-weight: 600;">Loading...</p>
    `;
    loader.style.cssText = `
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: #6c5ce7;
        font-weight: 600;
        z-index: 10;
        text-align: center;
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 16px;
        padding: 30px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    `;

    const container = element.parentElement;
    if (container && !container.querySelector('.media-loader')) {
        container.style.position = 'relative';
        container.appendChild(loader);
    }
}

function hideLoadingState(element) {
    const container = element.parentElement;
    const loader = container?.querySelector('.media-loader');
    if (loader) {
        loader.remove();
    }
}

function showErrorState(element) {
    hideLoadingState(element);

    const error = document.createElement('div');
    error.className = 'media-error';
    error.innerHTML = `
        <i class="fas fa-exclamation-triangle" style="font-size: 2rem; margin-bottom: 12px;"></i>
        <p style="color: white;">Error loading media file</p>
        <button onclick="location.reload()" class="btn btn-primary" style="margin-top: 16px;">
            <i class="fas fa-redo"></i>
            <span>Retry</span>
        </button>
    `;
    error.style.cssText = `
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        font-weight: 600;
        z-index: 10;
        text-align: center;
        background: rgba(255, 107, 53, 0.9);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 107, 53, 0.3);
        border-radius: 16px;
        padding: 30px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    `;

    const container = element.parentElement;
    if (container && !container.querySelector('.media-error')) {
        container.appendChild(error);
    }
}

// ===== UTILITY FUNCTIONS =====
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Smooth scroll for internal links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + K to focus search
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        const searchInput = document.querySelector('input[name="q"], input[name="search"]');
        if (searchInput) {
            searchInput.focus();
            searchInput.select();
        }
    }
});

// Performance monitoring
if ('performance' in window) {
    window.addEventListener('load', function() {
        const loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;
        console.log(`🎵 Frecuuency loaded in ${loadTime}ms - Professional DJ Platform Ready`);
    });
}

// ===== KEYBOARD SHORTCUTS =====
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + K to focus search
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        const searchInput = document.querySelector('input[name="q"], input[name="search"]');
        if (searchInput) {
            searchInput.focus();
            searchInput.select();
        }
    }

    // Space to play/pause (if media player is visible)
    if (e.code === 'Space' && !e.target.matches('input, textarea')) {
        e.preventDefault();
        const audioPlayer = document.querySelector('.audio-player');
        const videoPlayer = document.querySelector('.video-player');

        if (audioPlayer && !audioPlayer.paused) {
            audioPlayer.pause();
        } else if (audioPlayer) {
            audioPlayer.play();
        } else if (videoPlayer && !videoPlayer.paused) {
            videoPlayer.pause();
        } else if (videoPlayer) {
            videoPlayer.play();
        }
    }
});