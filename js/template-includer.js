// Template inclusion system
class TemplateIncluder {
    constructor() {
        this.templates = {};
        this.loadPromises = {};
    }

    async loadTemplate(templateName) {
        if (this.templates[templateName]) {
            return this.templates[templateName];
        }

        if (this.loadPromises[templateName]) {
            return await this.loadPromises[templateName];
        }

        this.loadPromises[templateName] = fetch(`templates/${templateName}.html`)
            .then(response => response.text())
            .then(template => {
                this.templates[templateName] = template;
                return template;
            })
            .catch(error => {
                console.error(`Error loading template ${templateName}:`, error);
                return '';
            });

        return await this.loadPromises[templateName];
    }

    async includeTemplate(elementId, templateName, variables = {}) {
        const template = await this.loadTemplate(templateName);
        if (!template) return;

        let processedTemplate = template;
        for (const [key, value] of Object.entries(variables)) {
            const regex = new RegExp(`{{${key}}}`, 'g');
            processedTemplate = processedTemplate.replace(regex, value);
        }

        const element = document.getElementById(elementId);
        if (element) {
            element.innerHTML = processedTemplate;
        }
    }

    async includeHeader(homeUrl = 'index.html', homeLinkClass = '', titleClass = 'class="gradient-text"', aboutUrl = 'aboutme.html', caseStudiesUrl = 'case_studies.html', hoverColor = '#bc5090') {
        await this.includeTemplate('header-placeholder', 'header', {
            home_url: homeUrl,
            home_link_class: homeLinkClass,
            title_class: titleClass,
            about_url: aboutUrl,
            case_studies_url: caseStudiesUrl,
            hover_color: hoverColor
        });
    }

    async includeFooter() {
        await this.includeTemplate('footer-placeholder', 'footer', {});
    }

    async includeStyles(gradientColor1 = '#58508d', gradientColor2 = '#bc5090', additionalStyles = '') {
        await this.includeTemplate('styles-placeholder', 'styles', {
            gradient_color_1: gradientColor1,
            gradient_color_2: gradientColor2,
            additional_styles: additionalStyles
        });
    }

    async includeScripts(additionalScripts = '') {
        await this.includeTemplate('scripts-placeholder', 'scripts', {
            additional_scripts: additionalScripts
        });
    }
}

// Global instance
const templateIncluder = new TemplateIncluder();