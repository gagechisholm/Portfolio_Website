<template>
  <div id="app" class="app-container">
    <!-- Header -->
    <header class="header">
      <div class="header-content">
        <h1 class="logo">{{ currentSection }}</h1>
        <nav class="nav">
          <router-link to="/" class="nav-link">Home</router-link>
          <router-link to="/about" class="nav-link">About</router-link>
          <router-link to="/skills" class="nav-link">Skills</router-link>
          <router-link to="/projects" class="nav-link">Projects</router-link>
          <router-link to="/contact" class="nav-link">Contact</router-link>
        </nav>
      </div>
    </header>

    <!-- Main Content -->
    <main class="main-content">
      <router-view />
    </main>

    <!-- Footer -->
    <footer class="footer">
      <p>&copy; {{ new Date().getFullYear() }} Gage Chisholm - All rights reserved.</p>
      <div class="social-links">
        <a href="https://linkedin.com/in/yourprofile" target="_blank" class="social-link">
          LinkedIn
          <img src="/assets/qr-codes/linkedin.png" alt="LinkedIn QR" class="qr-code">
        </a>
        <a href="https://github.com/gagechisholm" target="_blank" class="social-link">
          GitHub
          <img src="/assets/qr-codes/github.png" alt="GitHub QR" class="qr-code">
        </a>
        <a href="https://www.instagram.com/gagechisholm/?hl=en" target="_blank" class="social-link">
          Instagram
          <img src="/assets/qr-codes/instagram.png" alt="Instagram QR" class="qr-code">
        </a>
        <a href="https://www.snapchat.com/add/gagechisholm" target="_blank" class="social-link">
          Snapchat
          <img src="/assets/qr-codes/snapchat.png" alt="Snapchat QR" class="qr-code">
        </a>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      currentSection: "Portfolio", // Default title
    };
  },
  watch: {
    $route(to) {
      this.updateCurrentSection(to.name);
    },
  },
  mounted() {
    this.updateCurrentSection(this.$route.name); // Set the initial title
  },
  methods: {
    updateCurrentSection(routeName) {
      const sectionTitles = {
        Home: "Home",
        About: "About Me",
        Skills: "Skills & Expertise",
        Projects: "My Projects",
        Contact: "Contact Me",
      };
      this.currentSection = sectionTitles[routeName] || "Portfolio";
    },
  },
};
</script>

<style>
/* General Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Roboto', sans-serif;
  background-color: #1b1b1b; /* Steam-like dark background */
  color: #eaeaea; /* Light text */
  margin: 0;
}

a {
  text-decoration: none;
}

/* App Container */
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

/* Header */
.header {
  background-color: #232323;
  padding: 10px 20px;
  position: sticky;
  top: 0;
  z-index: 1000;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 24px;
  font-weight: bold;
  color: #66c0f4; /* Steam's signature blue */
}

.nav {
  display: flex;
  gap: 20px;
}

.nav-link {
  color: #eaeaea;
  font-size: 16px;
  font-weight: 500;
  transition: color 0.3s ease, transform 0.3s ease;
}

.nav-link:hover {
  color: #66c0f4;
  transform: scale(1.1);
}

/* Main Content */
.main-content {
  flex: 1;
  padding: 20px;
}

/* Footer */
.footer {
  background-color: #232323;
  color: #eaeaea;
  text-align: center;
  padding: 15px 20px;
  border-top: 1px solid #444;
}

.social-links {
  margin-top: 10px;
  display: flex;
  justify-content: center;
  gap: 15px;
}

.social-link {
  display: flex;
  align-items: center;
  color: #eaeaea;
  font-size: 16px;
  transition: color 0.3s ease, transform 0.3s ease;
}

.social-link:hover {
  color: #66c0f4;
  transform: scale(1.1);
}

.qr-code {
  margin-left: 8px;
  width: 20px; /* Adjust for mini QR codes */
  height: 20px;
  transition: transform 0.3s ease;
}

.qr-code:hover {
  transform: scale(1.2); /* Slight zoom effect on hover */
}
</style>
