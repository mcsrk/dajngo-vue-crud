<template>
    <div>
      <h2>Companies</h2>
      <DataTable :items="companies" />
    </div>
</template>
  
<script>
    import DataTable from "@/components/common/DataTable.vue";
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
    async mounted() {
        try {
            const data = await api.getCompanies();
            this.companies = data;
        } catch (error) {
            console.log(error);
        }
    },
    };
</script>