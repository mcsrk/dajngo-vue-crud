<template>
    <div>
      <h2>Branches</h2>
      <DataTable :items="branches" />
    </div>
</template>
  
<script>
    import DataTable from "@/components/DataTable.vue";
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
        mounted() {
            api.getBranches()
            .then(data => {
                this.branches =  data
            })
        },
    };
</script>
  