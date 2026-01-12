        mermaid.initialize({ startOnLoad: true, theme: 'default' });

        // Sidebar toggle functionality
        document.addEventListener('DOMContentLoaded', function() {
            const sidebar = document.getElementById('sidebar');
            const sidebarOverlay = document.getElementById('sidebarOverlay');
            const sidebarToggleMobile = document.getElementById('sidebarToggleMobile');
            const sidebarToggleDesktop = document.getElementById('sidebarToggleDesktop');
            const sidebarClose = document.getElementById('sidebarClose');
            const mainContent = document.querySelector('.main-content');

            function isMobile() {
                return window.innerWidth <= 1024;
            }

            function toggleSidebar() {
                if (isMobile()) {
                    sidebar.classList.toggle('expanded');
                    if (sidebarOverlay) {
                        sidebarOverlay.classList.toggle('active');
                    }
                    // Prevent body scroll when sidebar is open
                    if (sidebar.classList.contains('expanded')) {
                        document.body.style.overflow = 'hidden';
                    } else {
                        document.body.style.overflow = '';
                    }
                } else {
                    sidebar.classList.toggle('collapsed');
                    if (mainContent) {
                        mainContent.classList.toggle('sidebar-collapsed');
                    }
                    // Update desktop toggle button position
                    if (sidebarToggleDesktop) {
                        if (sidebar.classList.contains('collapsed')) {
                            sidebarToggleDesktop.classList.add('sidebar-collapsed');
                        } else {
                            sidebarToggleDesktop.classList.remove('sidebar-collapsed');
                        }
                    }
                }
            }

            function closeSidebar() {
                if (isMobile()) {
                    sidebar.classList.remove('expanded');
                    if (sidebarOverlay) {
                        sidebarOverlay.classList.remove('active');
                    }
                    document.body.style.overflow = '';
                } else {
                    sidebar.classList.add('collapsed');
                    if (mainContent) {
                        mainContent.classList.add('sidebar-collapsed');
                    }
                    if (sidebarToggleDesktop) {
                        sidebarToggleDesktop.classList.add('sidebar-collapsed');
                    }
                }
            }

            function openSidebar() {
                if (isMobile()) {
                    sidebar.classList.add('expanded');
                    if (sidebarOverlay) {
                        sidebarOverlay.classList.add('active');
                    }
                    document.body.style.overflow = 'hidden';
                } else {
                    sidebar.classList.remove('collapsed');
                    if (mainContent) {
                        mainContent.classList.remove('sidebar-collapsed');
                    }
                    if (sidebarToggleDesktop) {
                        sidebarToggleDesktop.classList.remove('sidebar-collapsed');
                    }
                }
            }

            // Mobile toggle
            if (sidebarToggleMobile) {
                sidebarToggleMobile.addEventListener('click', function(e) {
                    e.stopPropagation();
                    toggleSidebar();
                });
            }

            // Desktop toggle
            if (sidebarToggleDesktop) {
                sidebarToggleDesktop.addEventListener('click', function(e) {
                    e.stopPropagation();
                    toggleSidebar();
                });
            }

            // Close button in sidebar
            if (sidebarClose) {
                sidebarClose.addEventListener('click', function(e) {
                    e.stopPropagation();
                    closeSidebar();
                });
            }

            // Overlay click to close on mobile
            if (sidebarOverlay) {
                sidebarOverlay.addEventListener('click', function(e) {
                    e.stopPropagation();
                    closeSidebar();
                });
            }

            // Handle window resize
            let resizeTimer;
            window.addEventListener('resize', function() {
                clearTimeout(resizeTimer);
                resizeTimer = setTimeout(function() {
                    if (!isMobile()) {
                        // On desktop, ensure sidebar state is correct
                        if (sidebarOverlay) {
                            sidebarOverlay.classList.remove('active');
                        }
                        document.body.style.overflow = '';
                        // Ensure toggle button position matches sidebar state
                        if (sidebarToggleDesktop && sidebar) {
                            if (sidebar.classList.contains('collapsed')) {
                                sidebarToggleDesktop.classList.add('sidebar-collapsed');
                            } else {
                                sidebarToggleDesktop.classList.remove('sidebar-collapsed');
                            }
                        }
                    } else {
                        // On mobile, close sidebar if open
                        closeSidebar();
                    }
                }, 250);
            });

            // Initialize desktop toggle button position on load
            if (!isMobile() && sidebarToggleDesktop && sidebar) {
                if (sidebar.classList.contains('collapsed')) {
                    sidebarToggleDesktop.classList.add('sidebar-collapsed');
                }
            }

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
                            if (isMobile()) {
                                closeSidebar();
                            }
                        }
                    }
                });
            });
        });