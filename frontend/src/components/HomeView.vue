<template>
    <div class="home-container">
      <!-- Hero Section -->
      <section class="hero">
        <div class="hero-content">
          <h1>Hi, I'm <span class="highlight">Gage Chisholm</span></h1>
          <p class="tagline">
            A <strong>Full-Stack Developer</strong> passionate about 
            <span id="dynamic-text"></span>
          </p>
          <div class="hero-buttons">
            <a href="/assets/resume.pdf" target="_blank" class="btn-primary">View My Resume</a>
            <router-link to="/projects" class="btn-secondary">Explore My Projects</router-link>
          </div>
        </div>
      </section>
  
      <!-- Key Highlights Section -->
      <section class="highlights">
        <h2>Why Choose Me?</h2>
        <div class="highlight-cards">
          <div class="card">
            <div class="icon-circle">🏆</div>
            <h3>Professional Experience</h3>
            <p>Over 5 years of experience building web and mobile applications using modern frameworks like Vue.js, Django, and React.</p>
          </div>
          <div class="card">
            <div class="icon-circle">💻</div>
            <h3>Top-Notch Skills</h3>
            <p>Expertise in Python, JavaScript, Vue.js, Django, and more. I deliver clean, efficient, and scalable code.</p>
          </div>
          <div class="card">
            <div class="icon-circle">⚡</div>
            <h3>Reliable and Efficient</h3>
            <p>On-time delivery and attention to detail, ensuring every project exceeds expectations.</p>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    name: "HomeView",
    mounted() {
  const texts = [
    "building innovative solutions.",
    "developing sleek designs.",
    "crafting scalable applications.",
  ];
  let index = 0;

  const changeText = () => {
    const dynamicTextElement = document.getElementById("dynamic-text");
    if (dynamicTextElement) {
      dynamicTextElement.textContent = texts[index];
      index = (index + 1) % texts.length;
    }
  };

  changeText(); // Set the initial text
  setInterval(changeText, 5000); // Change text every 5 seconds
},

  };
  </script>
  <style scoped>
  /* General Styling */
  .home-container {
    color: #eaeaea;
    font-family: 'Roboto', sans-serif;
  }
  
  /* Hero Section */
  .hero {
    background: linear-gradient(135deg, #1b1b1b, #232323);
    padding: 50px 20px;
    text-align: center;
    color: #eaeaea;
    position: relative;
    overflow: hidden;
  }
  
  .hero::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle, rgba(0, 0, 0, 0.5), transparent);
    z-index: 0;
  }
  
  .hero-content {
    position: relative;
    z-index: 1;
  }
  
  .hero-content h1 {
    font-size: 48px;
    margin-bottom: 20px;
  }
  
  .hero-content .highlight {
    color: #66c0f4; /* Steam-like blue */
  }
  
  .tagline {
    font-size: 18px;
    margin-bottom: 30px;
    color: #bbbbbb;
  }
  
  .hero-buttons {
    display: flex;
    justify-content: center;
    gap: 15px;
  }
  
  .btn-primary, .btn-secondary {
    padding: 10px 20px;
    border-radius: 5px;
    text-transform: uppercase;
    font-weight: bold;
    text-decoration: none;
    transition: all 0.3s ease;
  }
  
  .btn-primary {
    background-color: #66c0f4;
    color: #1b1b1b;
  }
  
  .btn-primary:hover {
    background-color: #4093d0;
  }
  
  .btn-secondary {
    border: 1px solid #66c0f4;
    color: #66c0f4;
  }
  
  .btn-secondary:hover {
    background-color: #66c0f4;
    color: #1b1b1b;
  }
  
  /* Highlights Section */
  .highlights {
    padding: 50px 20px;
    background-color: #1b1b1b;
  }
  
  .highlights h2 {
    text-align: center;
    font-size: 36px;
    margin-bottom: 40px;
    color: #66c0f4;
  }
  
  .highlight-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
  }
  
  .card {
    background-color: #232323;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    transition: all 0.3s ease;
  }
  
  .card:hover {
    transform: translateY(-10px);
    box-shadow: 0 6px 10px rgba(0, 0, 0, 0.5);
  }
  
  .icon-circle {
    font-size: 40px;
    color: #66c0f4;
    margin-bottom: 15px;
  }
  </style>
  