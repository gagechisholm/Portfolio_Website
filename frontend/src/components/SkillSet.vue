/* eslint-disable vue/multi-word-component-names */


<template>
    <div>
      <h1>Skills</h1>
      <ul>
        <li v-for="skill in skills" :key="skill.id">
          {{ skill.name }} ({{ skill.proficiency }}%)
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import { fetchSkills } from '@/services/api';
  
  export default {
    data() {
      return { skills: [] };
    },
    mounted() {
      fetchSkills().then((response) => {
        this.skills = response.data;
      });
    },
  };
  </script>
  