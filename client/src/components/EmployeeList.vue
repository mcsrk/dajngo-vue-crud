<template>
    <div>
      <h2>Employees</h2>
      <DataTable :items="employees" />
    </div>
</template>
  
<script>

    import DataTable from "@/components/common/DataTable.vue";
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
    async mounted() {
        try {
            const data = await api.getEmployees();
            this.employees = data;
        } catch (error) {
            console.log(error);
        }
    },
    };
</script>