import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/item/:slug',
    name: 'item',
    meta: {
      title: 'Item'
    },
    component: () => import(/* webpackChunkName: "item" */ '../views/ItemView.vue'),
  },
  // {
  //   path: '*',
  //   name: 'not-found',
  //   meta: {
  //     title: 'Not Found'
  //   },
  //   component: () => import(/* webpackChunkName: "404" */ '../views/NotFoundView.vue'),
  // },
  {
    path: '/404',
    name: '404',
    meta: {
      title: 'Not Found'
    },
    component: () => import(/* webpackChunkName: "404" */ '../views/NotFoundView.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'Home'
  next()
})

export default router
