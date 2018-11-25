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
    </div>
</template>

<script>
    import AppButton from './AppButton';

    export default {
        name: "MovieCard",
        components: {
            AppButton
        },
        props: {
            movie: {
                type: Object,
                required: true
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