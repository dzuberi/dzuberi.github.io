// Your JavaScript file (e.g., app.js)

const myHTML = `
<div class="site-nav">
<ul class="jaja">
    <li><a href="index.html">About</a></li>
    <li><a href="experience.html">Experience</a></li>
    <li><a href="projects.html">Projects</a></li>
    <li><a href="blog.html">Blog</a></li>
</ul>
</div>
<div class="side-panel">
<!-- Content for the side panel goes here -->
    <ul>
    <li>Danial Zuberi</li>
    <li style="font-size: 24px;"><a href="https://www.linkedin.com/in/danial-zuberi/" target="_blank"><i class="fa-brands fa-linkedin-in"></i></a></li>
    <li style="font-size: 24px;"><a href="https://github.com/dzuberi/" target="_blank"><i class="fa-brands fa-github"></i></a></li>
    <li><a href="mailto:dzuberi(at)ucsd(dot)edu"><i class="fa fa-envelope" aria-hidden="true"></i>
    </a></li>
</ul>
</div>
`;

document.body.innerHTML = myHTML;