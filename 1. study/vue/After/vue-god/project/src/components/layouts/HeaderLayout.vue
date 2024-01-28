<template>
  <div>
    <!-- <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/databinding/string">String</router-link> |
      <router-link to="/databinding/html">Html</router-link>
    </nav> -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">CHAFA</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a
                class="nav-link active"
                aria-current="page"
                @click="goToMenu('/')"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" @click="goToMenu('/about')">About</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" @click="goToMenu('/databinding/string')"
                >String</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" @click="goToMenu('/databinding/html')"
                >Html</a
              >
            </li>
          </ul>
          <form class="d-flex" role="search">
            <input
              class="form-control me-2"
              type="search"
              placeholder="Search"
              aria-label="Search"
            />
            <button class="btn btn-outline-success" type="submit">
              Search
            </button>
          </form>
        </div>
      </div>
    </nav>
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      sampleData: ''
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {
    goToMenu(path) {
      this.$router.push({ path: path })
    }
  }
}
</script>
