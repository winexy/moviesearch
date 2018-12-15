<template>
    <div>
        <h1 class="auth1">Registration</h1>
        <auth-form @submit="send"></auth-form>
    </div>
</template>

<script>
    import AuthForm from './AuthForm';

    export default {
        name: "Registration",
        components: {
            AuthForm
        },
        methods: {
            send($event) {
                this.$api.post('auth/registration', $event)
                    .then(console.log);
            }
        }
    }
</script>

<style scoped>

</style>