import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

import Mainpage from '../pages/Mainpage';
import AuthContainer from '../pages/Auth';
import Login from '../pages/Auth/Login';
import Registration from '../pages/Auth/Registration';
import CabinetPage from '../pages/CabinetPage';


export default new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: Mainpage
        },
        {
            path: '/auth',
            component: AuthContainer,
            children: [
                {
                    path: '',
                    component: Login,
                },
                {
                    path: 'registration',
                    component: Registration
                }
            ]
        },
        {
            path: '/cabinet',
            component: CabinetPage
        }
    ]
})