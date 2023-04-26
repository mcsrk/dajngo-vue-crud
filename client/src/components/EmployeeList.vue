<template>
    <div>
      <h2>Employees</h2>
      <DataTable :items="employees" />
    </div>
</template>
  
<script>

    import DataTable from "@/components/DataTable.vue";
    import api from '../api'

    export default {
    name: "EmployeeList",
    components: {
        DataTable,
    },
    data() {
        return {
            employees: [],
        };
    },
    mounted() {
            api.getEmployees()
            .then(data => {
                this.employees =  data
            })
        },
    };
</script>