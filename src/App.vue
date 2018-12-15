<template>
    <div id="app">
        <div class="header">
            <router-link tag="h1"  to="/" class="heading">
                🦄 gogogo
            </router-link>
            <div style="display: flex; justify-content: center; align-content: center">
                <template v-if="$store.state.user.id">
                    <div class="block">
                        <router-link class="button-kek" to="/cabinet">Profile</router-link>
                        <a @click="logout" class="button-kek">Logout</a>
                    </div>
                </template>
                <template v-else>
                    <div class="block">
                        <router-link to="/auth" class="button-kek">Sign in</router-link>
                        <router-link to="/auth/registration" class="button-kek">Sign up</router-link>
                    </div>
                </template>
            </div>
        </div>
        <router-view></router-view>
    </div>
</template>

<script>
    export default {
        name: "App",
        methods: {
            logout() {
                this.$store.commit('setUser', '');
            }
        },
        created() {
            let user = this.$store.user;

            if (!user) {
                user = localStorage.getItem('user');
                if (user) {
                    user = JSON.parse(user);
                    this.$store.commit('setUser', user);
                }
            }

            if (user) {
                this.$api.get(`/get_user_movies?user=${user.id}`)
                    .then(response=> {
                        let movies = response.data.map(el => ({
                                ...el.fields,
                                pk: el.pk
                        }));

                        this.$store.commit('setMovies', movies);
                    });
            }

        }
    }
</script>

<style>
    * {
        font-family: 'Roboto', sans-serif;
        margin: 0;
        padding: 0;
    }

    :root {
        --dark: #2d3436;
        --shadow: 0 5px 5px rgba(0, 0, 0, .1), 0 3px 5px rgba(0, 0, 0, .3);
        --radius: 3px;
        --loader-fill: #fff;
        --accent: #3F51B5;
    }

    body {
        background: var(--dark);
    }

    #app {
        display: flex;
        align-items: center;
        flex-direction: column;
        padding-top: 100px;
        /*height: 100vh;*/
        width: 100vw;
        background: var(--dark);
        box-sizing: border-box;
    }

    .header {
        width: 800px;
        display: flex;
        justify-content: space-between;
    }

    .heading {
        cursor: pointer;
    }


    .block {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .button-kek {
        display: block;
        border: 1px solid orangered;
        color: orangered;
        text-decoration: none;
        padding: 5px 20px;
        border-radius: 3px;
        margin: 0 5px;
        transition: .3s ease-in-out;
        cursor: pointer;
    }

    .button-kek:hover {
        color: white;
        background: orangered;
    }

    h1 {
        margin-bottom: 20px;
    }
</style>