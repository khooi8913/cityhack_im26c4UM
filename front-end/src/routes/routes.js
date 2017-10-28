import DashboardLayout from '../components/Dashboard/Layout/DashboardLayout.vue'
// GeneralViews
import NotFound from '../components/GeneralViews/NotFoundPage.vue'

// Admin pages
import Overview from 'src/components/Dashboard/Views/Overview.vue'
// import UserProfile from 'src/components/Dashboard/Views/UserProfile.vue'
// import Notifications from 'src/components/Dashboard/Views/Notifications.vue'
// import Icons from 'src/components/Dashboard/Views/Icons.vue'
import Maps from 'src/components/Dashboard/Views/Maps.vue'
import Video from 'src/components/Dashboard/Views/Video.vue'
import Typography from 'src/components/Dashboard/Views/Typography.vue'
// import TableList from 'src/components/Dashboard/Views/TableList.vue'

const routes = [
  {
    path: '/',
    component: DashboardLayout,
    redirect: '/admin/overview'
  },
  {
    path: '/admin',
    component: DashboardLayout,
    redirect: '/admin/stats',
    children: [
      {
        path: 'overview',
        name: 'overview',
        component: Overview
      },
      {
        path: 'maps',
        name: 'maps',
        component: Maps
      },
      {
        path: 'video',
        name: 'Traffic',
        component: Video
      }
    ]
  },
  { path: '*', component: NotFound }
]

/**
 * Asynchronously load view (Webpack Lazy loading compatible)
 * The specified component must be inside the Views folder
 * @param  {string} name  the filename (basename) of the view to load.
function view(name) {
   var res= require('../components/Dashboard/Views/' + name + '.vue');
   return res;
};**/

export default routes
