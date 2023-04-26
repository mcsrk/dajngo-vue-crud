import axios from 'axios'
import config from './config'

const api = axios.create({
  baseURL: config.apiUrl
})

export default {
  getCompanies() {
    return api
      .get('/companies/')
      .then((response) => {
        console.log(response.data)
        return response.data
      })
      .catch((error) => {
        console.log(error)
        return []
      })
  },
  getBranches() {
    return api
      .get('/branches/')
      .then((response) => {
        console.log(response.data)
        return response.data
      })
      .catch((error) => {
        console.log(error)
        return []
      })
  },
  getEmployees() {
    return api
      .get('/employees/')
      .then((response) => {
        console.log(response.data)
        return response.data
      })
      .catch((error) => {
        console.log(error)
        return []
      })
  }
}
