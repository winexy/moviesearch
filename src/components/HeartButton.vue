<template>
    <div class="fav" @click.stop="like">
        <img
                :src="icon"
                class="fav__img"
        >
    </div>
</template>

<script>
    const PATH = '/static/images/';
    const DEFAULT_PATH = PATH + 'like--outline.svg';
    const ACTIVE_PATH = PATH + 'like.svg';

    export default {
        name: "HeartButton",
        props: {
            active: {
                type: Boolean,
                default: false
            }
        },
        methods: {
            like() {
                this.$emit('click', !this.active);
            }
        },
        computed: {
            icon() {
                return this.active ? ACTIVE_PATH : DEFAULT_PATH;
            }
        }
    }
</script>

<style scoped>
    .fav {
        position: absolute;
        top: 5px;
        right: 5px;
        width: 40px;
        height: 40px;
        display: flex;
        justify-content: center;
        align-items: center;
        background: #fff;
        border-radius: 50%;
        box-shadow: 0 2px 1px rgba(0, 0, 0, .2);
    }

    .fav__img {
        width: 60%;
    }
</style>