/* eslint-disable vue/multi-word-component-names */


<template>
    <div>
      <h1>Projects</h1>
      <div v-for="project in projects" :key="project.id">
        <h3>{{ project.title }}</h3>
        <img :src="project.image" :alt="project.title" />
        <p>{{ project.description }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import { fetchProjects } from '@/services/api';
  
  export default {
    data() {
      return { projects: [] };
    },
    mounted() {
      fetchProjects().then((response) => {
        this.projects = response.data;
      });
    },
  };
  </script>
  