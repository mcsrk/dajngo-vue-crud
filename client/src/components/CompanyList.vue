<template>
    <div>
      <h2>Companies</h2>
      <DataTable :items="companies" />
    </div>
</template>
  
<script>
    import DataTable from "@/components/DataTable.vue";
    import api from '../api'

    export default {
    name: "CompanyList",
    components: {
        DataTable,
    },
    data() {
        return {
            companies: [],
        };
    },
    mounted() {
            api.getCompanies()
            .then(data => {
                this.companies =  data
            })
        },
    };
</script>