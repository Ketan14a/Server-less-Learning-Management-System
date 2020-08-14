import Vue from "vue";
import Router from "vue-router";
import Login from "./views/Login.vue";
import Chat from "@/views/Chat.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "LoggedIn",
      component: Login
    },
    {
      path: '/Chat-room',
      name: 'Chat',
      component: Chat,
      props: true,
      beforeEnter: (to, from, next) => {
        if (to.params.name) {
          next();
        } else {
          next({name: 'LoggedIn'})
        }
      }
    }
  ]
});
