<template>
    <table>
      <thead>
        <tr>
          <th>Id</th>
          <th>Name</th> 
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ item.name }}</td> 
        </tr>
      </tbody>
    </table>
</template>

<script>
    export default {
      name: "DataTable",
      props: {
          items: Array,
      },
    };
</script>  

<style scoped>
table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  text-align: left;
  padding: 8px;
}

th {
  background-color: #4CAF50;
  color: white;
}
tr {
  border-bottom: 1px solid #d9d9d9;
}
tr:nth-child(even) {
  background-color: #f2f2f2;
}
</style>
