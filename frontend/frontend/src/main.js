import Vue from "vue";
import App from "./App.vue";
import router from "./router";
// install bootstrap
import "bootstrap/dist/css/bootstrap.css";
// Import the BootstrapVue library
import BootstrapVue from "bootstrap-vue";

Vue.config.productionTip = false;
Vue.use(BootstrapVue);
new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
