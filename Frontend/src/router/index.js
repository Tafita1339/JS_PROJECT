import Vue from 'vue'
import VueRouter from 'vue-router'


import NotFound from '../views/NotFound'
import Acceuil from '../views/Acceuil'
import Modifier from '../views/Modifier'
import Supprimer from '../views/Supprimer'
import Ajouter from '../views/Ajouter'



Vue.use(VueRouter)


const routes = [
    { path: '/', name: 'Accueil',component: Acceuil},  
  
    { path: '/modifier/:id', name: 'Modifier',component: Modifier}, 

    { path: '/supprimer', name: 'Supprimer',component: Supprimer}, 

    { path: '/Ajouter', name: 'Ajouter',component: Ajouter},

    { path: '/404', name: 'NotFound',component: NotFound },

    { path: '*', redirect: '/404' },  
]
 
const router = new VueRouter({
    mode: 'history',
    routes
})

export default router