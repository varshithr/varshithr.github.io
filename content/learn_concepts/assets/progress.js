        // Progress tracking with localStorage
        document.addEventListener('DOMContentLoaded', function() {
            const checkboxes = document.querySelectorAll('.progress-checkbox');
            const storageKey = 'learn_concepts_progress';

            // Load saved progress
            function loadProgress() {
                try {
                    const saved = localStorage.getItem(storageKey);
                    if (saved) {
                        const progress = JSON.parse(saved);
                        checkboxes.forEach(checkbox => {
                            const id = checkbox.id;
                            if (progress[id] !== undefined) {
                                checkbox.checked = progress[id];
                            }
                        });
                    }
                } catch (e) {
                    console.error('Error loading progress:', e);
                }
            }

            // Save progress
            function saveProgress() {
                try {
                    const progress = {};
                    checkboxes.forEach(checkbox => {
                        progress[checkbox.id] = checkbox.checked;
                    });
                    localStorage.setItem(storageKey, JSON.stringify(progress));
                } catch (e) {
                    console.error('Error saving progress:', e);
                }
            }

            // Load progress on page load
            loadProgress();

            // Save progress when checkbox changes
            checkboxes.forEach(checkbox => {
                checkbox.addEventListener('change', saveProgress);
            });

            // Calculate and display progress percentage
            function updateProgressStats() {
                const total = checkboxes.length;
                const completed = Array.from(checkboxes).filter(cb => cb.checked).length;
                const percentage = total > 0 ? Math.round((completed / total) * 100) : 0;

                // Update or create progress stats element
                let statsEl = document.getElementById('progress-stats');
                if (!statsEl) {
                    statsEl = document.createElement('div');
                    statsEl.id = 'progress-stats';
                    statsEl.style.cssText = 'background-color: #EEF2FF; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1.5rem; border-left: 4px solid #58508d;';
                    const contentDiv = document.querySelector('.content');
                    if (contentDiv && contentDiv.firstChild) {
                        contentDiv.insertBefore(statsEl, contentDiv.firstChild.nextSibling);
                    }
                }
                statsEl.innerHTML = `<strong>Progress:</strong> ${completed} of ${total} completed (${percentage}%)`;
            }

            // Update stats on load and change
            updateProgressStats();
            checkboxes.forEach(checkbox => {
                checkbox.addEventListener('change', updateProgressStats);
            });
        });