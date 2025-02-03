async function loadProjects() {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/projects');
        const projects = await response.json();
        const projectList = document.getElementById('project-list');
        projectList.innerHTML = '';

        projects.forEach(proj => {
            const projectItem = document.createElement('div');
            projectItem.classList.add('project');
            projectItem.innerHTML = `
                <h3>${proj.name}</h3>
                <p>${proj.description}</p>
                <a href="${proj.url}" target="_blank">Ver no GitHub</a>
            `;
            projectList.appendChild(projectItem);
        });
    } catch (error) {
        console.error("Erro ao carregar projetos:", error);
        document.getElementById('project-list').innerHTML = '<p>Erro ao carregar projetos.</p>';
    }
}

loadProjects();
