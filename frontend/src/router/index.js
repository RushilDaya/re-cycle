import Vue from 'vue'
import Router from 'vue-router'
import MainPage from '@/components/MainPage'
import InformationPage from '@/components/InformationPage'
import SocialPage from '@/components/SocialPage'
import ActivityTracker from '@/components/ActivityTracker'
import ProfilePage from '@/components/ProfilePage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'MainPage',
      component: MainPage
    },
    {
      path: '/social',
      name:'SocialPage',
      component: SocialPage
    },
    {
      path: '/information',
      name:'InformationPage',
      component:InformationPage
    },
    {
      path: '/activity',
      name:'ActivityTracker',
      component:ActivityTracker
    },
    {
      path: '/profile',
      name: 'ProfilePage',
      component: ProfilePage
    }
  ]
})
