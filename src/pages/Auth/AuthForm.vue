<template>
    <form @submit.prevent="submit">
        <label for="">Login</label>
        <input type="text" v-model="user.login">
        <label for="">Password</label>
        <input type="password" v-model="user.password">
        <button>Submit</button>
    </form>
</template>

<script>
    export default {
        name: "AuthForm",
        data() {
            return {
                user: {
                    login: '',
                    password: ''
                }
            }
        },
        methods: {
            submit() {
                this.$emit('submit', this.user);
            }
        }
    }
</script>

<style scoped>
    form {
        display: flex;
        justify-content: flex-start;
        align-items: flex-start;
        flex-direction: column;
    }

    label {
        color: #ffffff;
    }

    input {
        border: none;
        padding: 5px 15px;
        border-radius: 3px;
        height: 40px;
        font-size: 16px;
        margin: 5px 0 10px 0;
    }

    button {
        border-radius: 3px;
        border: none;
        width: 100%;
        height: 40px;
        transition: .3s ease-in-out;
        cursor: pointer;
        font-size: 16px;
    }

    button:hover {
        color: white;
        background: orangered;
    }
</style>