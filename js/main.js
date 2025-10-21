/**
 * Fetches an HTML component, replaces placeholders, and injects it into a specified element.
 * @param {string} url - The URL of the HTML component to fetch.
 * @param {string} targetId - The ID of the HTML element where the component will be inserted.
 * @param {string} basePath - The base path for resolving relative links.
 */
async function loadComponent(url, targetId, basePath) {
    const targetElement = document.getElementById(targetId);
    if (!targetElement) return;

    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`Failed to fetch: ${response.statusText}`);

        let html = await response.text();
        html = html.replace(/{base_path}/g, basePath);
        targetElement.innerHTML = html;

        const scripts = targetElement.querySelectorAll('script');
        scripts.forEach(oldScript => {
            const newScript = document.createElement('script');
            Array.from(oldScript.attributes).forEach(attr => newScript.setAttribute(attr.name, attr.value));
            newScript.textContent = oldScript.textContent;
            oldScript.parentNode.replaceChild(newScript, oldScript);
        });
    } catch (error) {
        console.error(`Error loading component from ${url}:`, error);
    }
}

/**
 * Loads the common head content.
 * @param {string} basePath - The base path for resolving relative links.
 */
async function loadHeadContent(basePath) {
    try {
        const response = await fetch(`${basePath}/layouts/_head.html`);
        if (!response.ok) throw new Error(`Failed to fetch: ${response.statusText}`);
        let html = await response.text();
        html = html.replace(/{base_path}/g, basePath);
        document.head.insertAdjacentHTML('beforeend', html);
    } catch (error) {
        console.error(`Error loading head content:`, error);
    }
}

/**
 * Dynamically generates and loads the header content based on page type.
 * @param {string} basePath - The base path for resolving relative links.
 */
async function loadHeader(basePath) {
    const headerPlaceholder = document.getElementById('header-placeholder');
    if (!headerPlaceholder) return;

    const pageType = document.body.getAttribute('data-page-type') || 'root';
    const topicName = document.body.getAttribute('data-topic-name') || '';
    const topicColor = document.body.getAttribute('data-topic-color') || '#bc5090';

    let navTitle = '';
    let navLinks = '';

    const homeIcon = `<svg class="w-6 h-6 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"></path></svg>`;

    if (pageType === 'root') {
        navTitle = `
            <a href="${basePath}/index.html" class="flex items-center">
                ${homeIcon}
                <span class="gradient-text" style="background: linear-gradient(90deg, #58508d, #bc5090); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                    Data Engineering Concepts
                </span>
            </a>`;
        navLinks = `
            <li><a href="${basePath}/case_studies.html" class="hover:text-[#bc5090] font-semibold">Case Studies</a></li>
            <li><a href="${basePath}/aboutme.html" class="hover:text-[#bc5090] font-semibold">About Me</a></li>`;
    } else {
        const homeLink = pageType === 'topic-index' ? `${basePath}/index.html` : `../index.html`;
        const backText = pageType === 'deep-dive' || pageType === 'case-study'
            ? `Back to ${topicName} Topics`
            : 'Data Engineering Concepts';

        navTitle = `
            <a href="${homeLink}" class="flex items-center hover:text-gray-600">
                ${homeIcon}
                <span>${backText}</span>
            </a>`;
        navLinks = `
            <li><a href="${basePath}/aboutme.html" class="hover:text-[${topicColor}] font-semibold">About Me</a></li>`;
    }

    try {
        const response = await fetch(`${basePath}/layouts/_header.html`);
        if (!response.ok) throw new Error(`Failed to fetch header template: ${response.statusText}`);
        let headerHTML = await response.text();

        headerHTML = headerHTML.replace('{nav_title}', navTitle).replace('{nav_links}', navLinks);
        headerPlaceholder.innerHTML = headerHTML;
    } catch (error) {
        console.error('Error loading header:', error);
    }
}


/**
 * Loads all common components for the page.
 */
async function loadCommonComponents() {
    const basePath = document.body.getAttribute('data-base-path') || '.';

    if (!document.getElementById('header-placeholder')) {
        const header = document.createElement('div');
        header.id = 'header-placeholder';
        document.body.prepend(header);
    }
    if (!document.getElementById('footer-placeholder')) {
        const footer = document.createElement('div');
        footer.id = 'footer-placeholder';
        document.body.append(footer);
    }

    await loadHeadContent(basePath);
    await loadHeader(basePath); // Use the new header loading function

    loadComponent(`${basePath}/layouts/_footer.html`, 'footer-placeholder', basePath);

    if (document.querySelector('.card')) {
        if (!document.getElementById('card-script-placeholder')) {
            const scriptPlaceholder = document.createElement('div');
            scriptPlaceholder.id = 'card-script-placeholder';
            document.body.append(scriptPlaceholder);
        }
        loadComponent(`${basePath}/layouts/_card_script.html`, 'card-script-placeholder', basePath);
    }
}

document.addEventListener('DOMContentLoaded', loadCommonComponents);
