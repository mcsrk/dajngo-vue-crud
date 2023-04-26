<script setup>
 
</script>

<template>
  <div>
    <h1>Companies</h1>
    <ul>
      <li v-for="company in companies" :key="company.company_id">
        <h2>{{ company.company_name }}</h2>
        <p>{{ company.company_id }}</p>
        <p>{{ company.company_email }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import api from './api'

export default {
  data() {
    return {
      companies: []
    }
  },
  mounted() {
    api.getCompanies()
      .then(data => {
        this.companies =  data
      })
  }
}
</script>
<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
