<template>
    <div class="search-results">
        <div v-if="results.Response === 'True'"
             class="search-results__container"
        >
            <movie-card
                    v-for="movie in results.Search"
                    :key="movie.key"
                    :movie="movie"
                    @click.native="$emit('show-details', movie.imdbID)"
            ></movie-card>
        </div>
        <transition name="error">
            <div v-if="results.Response === 'False'"
                 class="search-results__error"
            >
                {{ results.Error }}
            </div>
        </transition>
    </div>
</template>

<script>
    import MovieCard from './MovieCard';

    export default {
        name: "SearchResults",
        components: {
            MovieCard
        },
        props: {
            results: {
                type: Object,
                default: {}
            }
        }
    }
</script>

<style >
    .search-results {
        width: 1080px;
    }

    .search-results__container {
        display: flex;
        flex-wrap: wrap;
    }

    .search-results__error {
        position: absolute;
        top: 20px;
        right: 20px;
        display: block;
        min-width: 100px;
        padding: 10px;
        border-radius: var(--radius);
        text-align: center;
        box-sizing: border-box;
        color: #fff;
        font-weight: 600;
        font-size: 18px;
        background: #ff460073;
        transition: .5s ease-in-out;
    }

    .error-enter-active, .error-leave-active {
        transform: translateX(300px)
    }

    @media screen and (max-width: 1100px) {
        .search-results {
            width: 810px;
        }
    }

    @media screen and (max-width: 800px) {
        .search-results__container {
            justify-content: space-between;
        }

        .search-results {
            width: 90%;
        }

    }
</style>