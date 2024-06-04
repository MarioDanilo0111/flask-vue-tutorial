import Vue from "vue";
import VueRouter from "vue-router";
import Shark from "../components/Shark.vue";
import GameLibrary from "../components/GameLibrary.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/shark",
    name: "SharkComponent",
    component: Shark,
  },
  {
    path: "/games",
    name: "GamesComponent",
    component: GameLibrary,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
