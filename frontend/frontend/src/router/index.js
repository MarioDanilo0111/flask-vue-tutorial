import Vue from "vue";
import VueRouter from "vue-router";

// Import Components
// import Shark from "../components/Shark.vue";
// import GameLibrary from "../components/GameLibrary.vue";

// Use VueRouter plugin
Vue.use(VueRouter);

// Define routes
const routes = [
  {
    path: "/shark",
    name: "SharkComponent",
    component: () =>
      import(/* webpackChunkName: "shark */ "../components/Shark.vue"),
  },
  {
    path: "/games",
    name: "GamesComponent",
    component: () =>
      import(/* webpackChunkName: "games */ "../components/GameLibrary.vue"),
  },
];

// Create router instance
const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
