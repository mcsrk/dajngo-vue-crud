<template>
    <div>
      <h2>Branches</h2>
      <DataTable :items="branches" />
    </div>
</template>
  
<script>
    import DataTable from "@/components/common/DataTable.vue";
    import api from '../api'

    export default {
        name: "BranchList",
        components: {
            DataTable,
        },
        data() {
            return {
                branches: [],
            };
        },
        async mounted() {
            try {
                const data = await api.getBranches();
                this.branches = data;
            } catch (error) {
                console.log(error);
            }
        },
    };
</script>
  