<script setup>
 
</script>

<template>
  <div class="container">
    <div class="list">
      <CompanyList />
    </div>
    <div class="list">
      <BranchList />
    </div>
    <div class="list">
      <EmployeeList />
    </div>
  </div>
</template>


<script>
  import CompanyList from './components/CompanyList.vue';
  import BranchList from './components/BranchList.vue';
  import EmployeeList from './components/EmployeeList.vue';

  export default {
    name: 'App',
    components: {
    CompanyList,
    BranchList,
    EmployeeList
},
  };
</script>

<style scoped>
 
</style>