<template>
    <div class="about-me-container">
      <!-- Introduction Section -->
      <section class="introduction">
        <h1>About Me</h1>
        <p>
          Hi, I'm <strong>Gage Chisholm</strong>, a passionate and dedicated 
          <span class="highlight">Full-Stack Developer</span>. With a strong foundation in 
          web development and an eye for sleek, scalable designs, I specialize in turning 
          ideas into reality.
        </p>
        <p>
          Over the years, I've honed my skills in frameworks like 
          <strong>Django</strong>, <strong>Vue.js</strong>, and <strong>React</strong>. 
          My mission is to deliver clean, efficient, and reliable code that empowers 
          businesses and individuals to achieve their goals.
        </p>
      </section>
  
      <!-- Skills Section -->
      <section class="skills">
        <h2>What I Bring to the Table</h2>
        <div class="skills-grid">
          <div class="skill-card">
            <h3>Backend Development</h3>
            <p>
              Expertise in Python, Django, and RESTful API design, delivering scalable 
              and secure backend solutions.
            </p>
          </div>
          <div class="skill-card">
            <h3>Frontend Development</h3>
            <p>
              Proficient in modern JavaScript frameworks like Vue.js and React, creating 
              interactive and dynamic user experiences.
            </p>
          </div>
          <div class="skill-card">
            <h3>Database Management</h3>
            <p>
              Skilled in SQL and NoSQL databases, ensuring efficient data storage and 
              retrieval for all projects.
            </p>
          </div>
          <div class="skill-card">
            <h3>Problem Solver</h3>
            <p>
              Known for tackling complex challenges and delivering innovative solutions 
              under tight deadlines.
            </p>
          </div>
        </div>
      </section>
  
      <!-- Call-to-Action Section -->
      <section class="call-to-action">
        <p>Interested in working together?</p>
        <router-link to="/contact" class="cta-button">Contact Me</router-link>
        <a href="/assets/resume.pdf" target="_blank" class="cta-button secondary">
          View My Resume
        </a>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    name: "AboutMe",
  };
  </script>
  
  <style scoped>
  /* General Styling */
  .about-me-container {
    color: #eaeaea;
    font-family: 'Roboto', sans-serif;
    background-color: #1b1b1b;
    padding: 20px;
    line-height: 1.6;
  }
  
  /* Introduction Section */
  .introduction {
    text-align: center;
    margin-bottom: 40px;
  }
  
  .introduction h1 {
    font-size: 36px;
    color: #66c0f4;
    margin-bottom: 20px;
  }
  
  .introduction p {
    font-size: 18px;
    margin-bottom: 20px;
  }
  
  .highlight {
    color: #66c0f4;
  }
  
  /* Skills Section */
  .skills {
    margin-bottom: 40px;
  }
  
  .skills h2 {
    text-align: center;
    font-size: 28px;
    margin-bottom: 20px;
    color: #66c0f4;
  }
  
  .skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
  }
  
  .skill-card {
    background-color: #232323;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    transition: transform 0.3s ease;
    text-align: center;
  }
  
  .skill-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 6px 10px rgba(0, 0, 0, 0.5);
  }
  
  .skill-card h3 {
    font-size: 20px;
    color: #ffffff;
    margin-bottom: 10px;
  }
  
  .skill-card p {
    font-size: 16px;
    color: #bbbbbb;
  }
  
  /* Call-to-Action Section */
  .call-to-action {
    text-align: center;
    padding: 20px;
    background-color: #232323;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
  }
  
  .call-to-action p {
    font-size: 20px;
    margin-bottom: 20px;
    color: #eaeaea;
  }
  
  .cta-button {
    background-color: #66c0f4;
    color: #1b1b1b;
    padding: 10px 20px;
    border-radius: 5px;
    text-transform: uppercase;
    font-weight: bold;
    text-decoration: none;
    margin: 0 10px;
    transition: background-color 0.3s ease, transform 0.2s ease;
  }
  
  .cta-button:hover {
    background-color: #4093d0;
    transform: scale(1.05);
  }
  
  .cta-button.secondary {
    background-color: transparent;
    border: 1px solid #66c0f4;
    color: #66c0f4;
  }
  
  .cta-button.secondary:hover {
    background-color: #66c0f4;
    color: #1b1b1b;
  }
  </style>
  