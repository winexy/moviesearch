<template>
    <div class="modal-wrapper" v-if="value">
        <template v-if="$slots.default">
            <div class="modal">
                <div class="modal__close" @click="close">
                    <svg enable-background="new 0 0 469.785 469.785" viewBox="0 0 469.785 469.785"
                         xmlns="http://www.w3.org/2000/svg">
                        <path d="m228.294-151.753 139.195 139.195c11.116 11.105 11.116 29.116 0 40.22-11.105 11.116-29.104 11.116-40.22 0l-139.196-139.195-139.207 139.196c-11.093 11.116-29.116 11.116-40.22 0-11.105-11.105-11.105-29.116 0-40.22l139.207-139.196-139.515-139.515c-11.116-11.116-11.116-29.116 0-40.22 5.552-5.564 12.834-8.34 20.116-8.34 7.27 0 14.552 2.776 20.105 8.34l139.514 139.514 139.196-139.196c5.564-5.552 12.834-8.34 20.116-8.34 7.27 0 14.552 2.788 20.105 8.34 11.116 11.105 11.116 29.104 0 40.22z"
                              fill="#34495e" transform="matrix(1.25 0 0 -1.25 0 45)"/>
                    </svg>
                </div>
                <div class="button mobile" @click="close">Close</div>
                <slot></slot>
            </div>
        </template>
        <template v-else>
            <loader/>
        </template>
        <div class="modal-overlay" @click="close"></div>
    </div>
</template>

<script>
    import Loader from './Loader';

    export default {
        name: "ModalWindow",
        components: {
            Loader
        },
        props: {
            value: {
                type: Boolean,
                default: false
            }
        },
        methods: {
            close() {
                this.$emit('input', false);
            }
        }
    }
</script>

<style >
    .modal-wrapper {
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        z-index: 100;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .modal-overlay {
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(0, 0, 0, .5);
    }

    .modal {
        border-radius: var(--radius);
        box-shadow: var(--shadow);
        padding: 30px;
        z-index: 101;
        background: #ffffff;
        width: 700px;
        box-sizing: border-box;
        position: relative;
        overflow: scroll;
    }

    .modal__close {
        width: 20px;
        position: absolute;
        top: 15px;
        right: 15px;
        cursor: pointer;
    }

    .modal__close path {
        transition: .3s ease-in-out;
    }

    .modal__close:hover path {
        fill: rgba(221, 46, 68, 0.70);
    }

    .modal__close:active {
        transform: scale(.9);
    }

    @media screen and (max-width: 800px) {
        .modal {
            width: 90%;
        }

        .modal-wrapper {
            padding: 30px 0;
            align-items: initial;
        }

        .modal__close {
            display: none;
        }
    }
</style>