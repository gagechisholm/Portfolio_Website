// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/components/HomeView.vue';
import SkillSet from '@/components/SkillSet.vue';
import ProjectList from '@/components/ProjectList.vue';
import AboutMe from '@/components/AboutMe.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView,
  },
  {
    path: '/skills',
    name: 'SkillSet',
    component: SkillSet,
  },
  {
    path: '/projects',
    name: 'ProjectList',
    component: ProjectList,
  },
  {
    path: '/about',
    name: 'AboutMe',
    component: AboutMe,
  }
  // Add other routes here...
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});


export default router;
