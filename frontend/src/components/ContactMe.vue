<template>
  <div class="contact-container">
    <!-- Contact Section -->
    <section class="contact">
      <div class="contact-grid">

        <!-- Freelance Inquiry Card -->
        <div class="contact-card">
          <h2>Freelance Inquiry</h2>
          <form @submit.prevent="handleFreelanceSubmit">
            <label for="freelance-name">Name:</label>
            <input id="freelance-name" v-model="freelance.name" type="text" placeholder="Your Name" required />

            <label for="freelance-email">Email:</label>
            <input id="freelance-email" v-model="freelance.email" type="email" placeholder="Your Email" required />

            <label for="freelance-message">Message:</label>
            <textarea id="freelance-message" v-model="freelance.message" placeholder="Describe your project..." required></textarea>

            <button type="submit">Send Inquiry</button>
          </form>
        </div>

        <!-- Email Card -->
        <div class="contact-card">
          <h2>Email Me</h2>
          <p>
            <strong>gagesmicrosoft@gmail.com</strong><br />
            <strong>gagechisholm218@coastalcarolina.edu</strong><br />
            <strong>gage.chisholm@usmc.mil</strong>
          </p>
        </div>

        <!-- Information Request Card -->
        <div class="contact-card">
          <h2>Request More Information</h2>
          <form @submit.prevent="handleInfoRequestSubmit">
            <label for="info-name">Name:</label>
            <input id="info-name" v-model="infoRequest.name" type="text" placeholder="Your Name" required />

            <label for="info-email">Email:</label>
            <input id="info-email" v-model="infoRequest.email" type="email" placeholder="Your Email" required />

            <label for="info-message">Message:</label>
            <textarea id="info-message" v-model="infoRequest.message" placeholder="What information do you need?" required></textarea>

            <button type="submit">Request Info</button>
          </form>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
export default {
  methods: {
  async handleFreelanceSubmit() {
    try {
      const response = await axios.post('/api/freelance-inquiry/', this.freelance);
      alert(response.data.message);
      this.freelance = { name: "", email: "", message: "" };
    } catch (error) {
      console.error(error);
      alert("Error submitting freelance inquiry. Please try again later.");
    }
  },
  async handleInfoRequestSubmit() {
    try {
      const response = await axios.post('/api/info-request/', this.infoRequest);
      alert(response.data.message);
      this.infoRequest = { name: "", email: "", message: "" };
    } catch (error) {
      console.error(error);
      alert("Error submitting information request. Please try again later.");
    }
  },
},

</script>

<style scoped>
/* General Styling */
.contact-container {
  color: #eaeaea;
  font-family: "Roboto", sans-serif;
  background-color: #1b1b1b;
  padding: 20px;
  line-height: 1.6;
}

/* Contact Section */
.contact {
  margin: 0 auto;
  max-width: 1200px;
}

.contact-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

/* Contact Card Styling */
.contact-card {
  background-color: #232323;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  text-align: center;
}

.contact-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.5);
}

.contact-card h2 {
  font-size: 24px;
  color: #66c0f4;
  margin-bottom: 20px;
}

.contact-card p {
  font-size: 16px;
  color: #bbbbbb;
  line-height: 1.5;
}

form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

form label {
  text-align: left;
  font-size: 14px;
  margin-bottom: 5px;
  color: #eaeaea;
}

form input,
form textarea {
  padding: 10px;
  border: 1px solid #444;
  border-radius: 5px;
  background-color: #1b1b1b;
  color: #eaeaea;
}

form button {
  padding: 10px;
  background-color: #66c0f4;
  color: #1b1b1b;
  font-weight: bold;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

form button:hover {
  background-color: #4093d0;
  transform: scale(1.05);
}
</style>
