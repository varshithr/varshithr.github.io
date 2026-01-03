mermaid.initialize({ startOnLoad: true, theme: 'default' });
document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('sidebar');
    const sidebarToggleMobile = document.getElementById('sidebarToggleMobile');
    const sidebarToggleDesktop = document.getElementById('sidebarToggleDesktop');
    const sidebarClose = document.getElementById('sidebarClose');
    const mainContent = document.querySelector('.main-content');

    function toggleSidebar() {
        sidebar.classList.toggle('collapsed');
        if (mainContent) {
            mainContent.classList.toggle('sidebar-collapsed');
        }
    }

    function expandSidebar() {
        sidebar.classList.add('expanded');
    }

    function collapseSidebar() {
        sidebar.classList.remove('expanded');
    }

    // Mobile toggle
    if (sidebarToggleMobile) {
        sidebarToggleMobile.addEventListener('click', function() {
            sidebar.classList.toggle('expanded');
        });
    }

    // Desktop toggle
    if (sidebarToggleDesktop) {
        sidebarToggleDesktop.addEventListener('click', toggleSidebar);
    }

    // Close button in sidebar
    if (sidebarClose) {
        sidebarClose.addEventListener('click', function() {
            if (window.innerWidth <= 1024) {
                collapseSidebar();
            } else {
                toggleSidebar();
            }
        });
    }

    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', function(event) {
        if (window.innerWidth <= 1024) {
            const isClickInsideSidebar = sidebar && sidebar.contains(event.target);
            const isClickOnToggle = sidebarToggleMobile && sidebarToggleMobile.contains(event.target);
            if (!isClickInsideSidebar && !isClickOnToggle && sidebar.classList.contains('expanded')) {
                collapseSidebar();
            }
        }
    });

    // Update active link on scroll
    const headings = document.querySelectorAll('.content h1, .content h2, .content h3, .content h4');
    const sidebarLinks = document.querySelectorAll('.sidebar-nav a');

    function updateActiveLink() {
        let current = '';
        headings.forEach(heading => {
            const rect = heading.getBoundingClientRect();
            if (rect.top <= 100) {
                current = heading.id;
            }
        });

        sidebarLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + current) {
                link.classList.add('active');
            }
        });
    }

    window.addEventListener('scroll', updateActiveLink);
    updateActiveLink();

    // Smooth scroll for sidebar links
    sidebarLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href.startsWith('#')) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    const headerOffset = 80;
                    const elementPosition = target.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });

                    // Close sidebar on mobile after click
                    if (window.innerWidth <= 1024) {
                        sidebar.classList.remove('expanded');
                    }
                }
            }
        });
    });
});
