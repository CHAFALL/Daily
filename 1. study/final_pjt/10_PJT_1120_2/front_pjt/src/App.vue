<template>
  <v-app style="background-color: black;">
  <header class="back">
    <nav>
      <div class="left-items">
        <RouterLink class="nav-link" :to="{ name: 'MovieView' }">Movies</RouterLink>
        <RouterLink class="nav-link" :to="{ name: 'ReviewView' }">Review</RouterLink>
      </div>
      <div class="right-items">
        <RouterLink class="nav-link" :to="{ name: 'SignUpView' }">SignUp</RouterLink>
        <RouterLink class="nav-link" :to="{ name: 'LogInView' }">LogIn</RouterLink>
      </div>
    </nav>
  </header>
  <RouterView />
</v-app>
</template>

<style>

.back {
  background-color: black;
  padding: 10px;
}

nav {
  display: flex;
  justify-content: space-between;
}

.left-items {
  display: flex;
}

.right-items {
  display: flex;
}

.nav-link {
  color: white;
  margin-right: 10px;
  text-decoration: none;
}
</style>
