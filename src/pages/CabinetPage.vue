<template>
    <div>
        <h1>Your movies</h1>
        <div class="search-results__container">
             <movie-card
                v-for="movie in movieees"
                :key="movie.key"
                :movie="movie"
            ></movie-card>
        </div>
    </div>
</template>

<script>
    import MovieCard from '../components/MovieCard';
    import {mapState} from 'vuex';

    export default {
        name: "Cabinet",
        components: {
            MovieCard
        },
        data() {
            return {
                movieees: []
            }
        },
        computed: mapState({
            movies: state => state.movies
        }),
        mounted() {
            this.movies.forEach(async movie => {
                const {data} = await this.$api.get(`movie?id=${movie.movie_id}`);
                this.movieees.push(data);
            })
        }
    }
</script>

<style>
    h1  {
        color: #fff;
    }
</style>