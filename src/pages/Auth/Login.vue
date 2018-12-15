<template>
    <div>
        <h1 class="auth1">Login</h1>
        <auth-form @submit="send"></auth-form>
    </div>
</template>

<script>
    import AuthForm from './AuthForm';
    export default {
        name: "Login",
        components: {
            AuthForm
        },
        methods: {
            send($event) {
               this.$api.post('auth/login', $event)
                   .then(response => {
                       console.log(response);

                       let { data: user } = response;

                       this.$store.commit('setUser', user);

                       this.$router.push('/');
                   });
            }
        }
    }
</script>

<style>
    .auth1 {
        color: #fff;
        margin-bottom: 20px;
    }
</style>