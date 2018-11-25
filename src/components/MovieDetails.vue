<template>
    <div class="movie">
        <div class="movie__side movie__side--left">
            <img :src="movie.Poster" alt="" class="movie__poster">
        </div>
        <div class="movie__side movie__side--right">
            <h2 class="movie__title">{{ movie.Title }}</h2>
            <span class="movie__param">
                <strong>Production</strong>: {{ movie.Production }}
            </span>
            <span class="movie__param">
                <strong>Actors:</strong>
                {{ movie.Actors }}
            </span>
            <span class="movie__param">
                <strong>Released</strong>: {{ movie.Released }}
            </span>
            <span class="movie__param">
                <strong>Director</strong>: {{ movie.Director }}
            </span>
            <span class="movie__param">
                <strong>Country</strong>: {{ movie.Country }}
            </span>
            <span class="movie__param">
                <strong>Duration</strong>: {{ movie.Runtime }}
            </span>
            <span class="movie__param">
                <strong>Rated</strong>: {{ movie.Rated }}
            </span>
            <div class="movie-param-block">
                <strong>Genres:</strong>
                <span
                        v-for="genre in movie.Genre.split(', ')"
                        class="movie-genre"
                >{{ genre }}</span>
            </div>
            <div class="movie-param-block movie-param-block--column">
                <strong>Ratings</strong>
                <div
                        v-for="rating in movie.Ratings"
                        class="movie-rating"
                >
                    <span class="movie-rating__source">{{ rating.Source }}</span>
                    <span class="movie-rating__value">{{ rating.Value }}</span>
                </div>
            </div>
            <p class="movie__plot">{{ movie.Plot }}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: "MovieDetails",
        props: {
            movie: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style>

    .movie {
        display: flex;
        font-size: 14px;
    }

    .movie__side--right {
        padding: 0 20px;
    }

    .movie__poster {
        border-radius: var(--radius);
        box-shadow: var(--shadow);
        object-fit: cover;
        object-position: center;
        width: 300px;
        height: 456px;
    }

    .movie__param {
        display: block;
        margin: 10px 0;
    }

    .movie__plot {
        padding: 10px;
        border-left: 5px solid var(--dark);
    }

    .movie-param-block {
        display: flex;
        flex-wrap: wrap;
        margin: 5px 0;
        align-items: center;
    }

    .movie-param-block--column {
        flex-direction: column;
        align-items: initial;
        justify-content: center;
    }

    .movie-genre {
        padding: 5px;
        margin: 2.5px;
        border-radius: var(--radius);
        background: #2ecc71;
        color: #fff;
    }

    .movie-rating {
        margin: 5px 0;
    }

    @media screen and (max-width: 800px) {
        .movie {
            flex-direction: column;
        }

        .movie__poster {
            width: 100%;
            height: auto;
            margin-top: 20px;
        }

        .movie__side--right {
            margin-top: 20px;
            padding: 0;
        }
    }
</style>