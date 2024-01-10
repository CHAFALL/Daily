import { createStore } from "vuex";
import accountStore from "./accountStore";
import menuStore from "./menuStore";
import platformInfoStore from "./platformInfoStore";
import authStore from "./authStore";

export default createStore({
  modules: {
    accountStore,
    menuStore,
    platformInfoStore,
    authStore
  }
});
