<template>
    <div>
        <div class="search-form">
            <input
                    type="text"
                    class="search-form__input"
                    placeholder="movie title"
                    v-model.trim="searchInput"
                    @input="search"
                    ref="input"
            >
        </div>
        <search-results
                :results="results"
                @show-details="showMovieDetails"
        ></search-results>
        <modal-window
                v-model="showModal"
                @input="movie = null"
        >
            <movie-details v-if="movie" :movie="movie"></movie-details>
        </modal-window>
    </div>
</template>

<script>
    import SearchResults from '../components/SearchResults';
    import AppButton from '../components/AppButton';
    import ModalWindow from '../components/ModalWindow';
    import MovieDetails from '../components/MovieDetails';
    // import AuthContainer from '../components/Auth/AuthContainer';
    import debounce from 'lodash/debounce';

    export default {
        name: "MainPage",
        components: {
            SearchResults,
            AppButton,
            ModalWindow,
            MovieDetails,
            // AuthContainer
        },
        data() {
            return {
                searchInput: '',
                results: {},
                showModal: false,
                movie: null
            }
        },
        methods: {
            search: debounce(async function () {
                if (!this.searchInput.length) {
                    this.results = {};
                    return;
                }

                const {data} = await this.$api.get(`search?value=${this.searchInput}`);

                if (data.Search) {
                    data.Search = data.Search.map((movie, i) => ({
                        ...movie,
                        key: movie.imdbID + i
                    }));
                }

                this.results = data;
            }, 500),
            async showMovieDetails(imdbID) {
                this.showModal = true;

                const {data} = await this.$api.get(`movie?id=${imdbID}`);

                this.movie = data;
            }
        },
        mounted() {
            this.$nextTick(() => {
                this.$refs.input.focus();
            })
        }
    }
</script>

<style>
    .search-form {
        width: 800px;
        margin: 0 auto 30px auto;
    }

    .search-form__input {
        width: 100%;
        padding: 20px;
        text-align: center;
        border-radius: var(--radius);
        border: none;
        outline: none;
        box-shadow: var(--shadow);
        font-size: 25px;
        box-sizing: border-box;
        opacity: .9;
    }

    .search-form__input:focus {
        opacity: 1;
    }

    .heading {
        text-align: center;
        color: #ffffff;
        margin: 10px;
    }

    .mobile {
        display: none;
    }

    @media screen and (max-width: 800px) {
        .search-form {
            width: 90%;
        }

         .mobile {
            display: flex;
        }
    }

</style>