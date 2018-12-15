<template>
    <div class="movie-card">
        <img
                :src="movie.Poster"
                :alt="movie.Title"
                class="movie-card__poster"
        />
        <span class="movie-card__title">{{ movie.Title }}</span>
        <span class="movie-card__year">{{ movie.Year }}</span>
        <app-button mobile>Show more</app-button>
        <heart-button
            v-if="$store.state.user.id"
            @click="like"
            :active="active"
        />
    </div>
</template>

<script>
    import AppButton from './AppButton';
    import HeartButton from './HeartButton';

    export default {
        name: "MovieCard",
        components: {
            HeartButton,
            AppButton
        },
        props: {
            movie: {
                type: Object,
                required: true
            },
        },
        data() {
            return {
                active: false
            }
        },
        methods: {
            like(state) {
                let user = this.$store.state.user.id;

                if (!user) return;

                this.$api.get(`/like?id=${this.movie.imdbID}&like=${state}&user=${user}`)
                    .then(response => {
                        let { data } = response;
                        this.active = !!data;
                        console.log(response);
                    });
            }
        },
        created() {
            let movies = this.$store.state.movies;
            if (movies.length) {
                this.active = movies.some(movie => movie.movie_id === this.movie.imdbID);
            }
        }
    }
</script>

<style>

    .movie-card {
        box-shadow: var(--shadow);
        background: #fff;
        padding: 15px;
        margin: 5px;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        position: relative;
        flex-direction: column;
        box-sizing: border-box;
        width: 260px;
        border-radius: var(--radius);
        overflow: hidden;
        cursor: pointer;
    }

    .movie-card__title {
        margin: 5px;
        font-weight: 600;
    }

    .movie-card__year {
        opacity: .6;
    }

    .movie-card__poster {
        border-radius: var(--radius);
        width: 230px;
        height: 330px;
        object-fit: cover;
        object-position: center;
    }

    @media screen and (max-width: 800px) {

        .movie-card {
            margin: 7px 0;
            width: 49%;
        }

        .movie-card__poster {
            width: 100%;
            height: auto;
        }

    }

    @media screen and (max-width: 500px) {
        .movie-card {
            margin: 7px 0;
            width: 100%
        }
    }


</style>