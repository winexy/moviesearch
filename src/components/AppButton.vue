<template>
    <button class="button" :class="classes">
        <slot></slot>
    </button>
</template>

<script>
    export default {
        name: "AppButton",
        props: {
            invert: {
                type: Boolean,
                default: false
            },
            mobile: {
                type: Boolean,
                default: false
            }
        },
        computed: {
            classes() {
                return {
                    'button--invert': this.invert,
                    'mobile': this.mobile
                }
            }
        }
    }
</script>

<style>
    .button {
        display: flex;
        border: 1px solid var(--accent);
        border-radius: var(--radius);
        padding: 10px;
        width: 100%;
        color: var(--accent);
        font-size: 14px;
        justify-content: center;
        margin-top: 10px;
        font-weight: 600;
        box-sizing: border-box;
        cursor: pointer;
        transition: .3s ease-in-out;
        outline: none;
    }

    .button:hover, .button:active {
        color: #ffffff;
        background: var(--accent);
    }

    .button--invert {
        background: none;
        border-color: #fff;
        color: #fff
    }

    .button--invert:hover {
        background: #fff;
        color: var(--accent);
    }

</style>