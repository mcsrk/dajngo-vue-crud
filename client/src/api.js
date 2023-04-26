import axios from 'axios'
import config from './config'

const api = axios.create({
  baseURL: config.apiUrl
})

const handleResponse = (response) => {
  console.log(response.data)
  return response.data
}

const handleError = (error) => {
  console.log(error)
  return []
}

export default {
  async getCompanies() {
    try {
      const response = await api.get('/companies/')
      return handleResponse(response)
    } catch (error) {
      return handleError(error)
    }
  },
  async getBranches() {
    try {
      const response = await api.get('/branches/')
      return handleResponse(response)
    } catch (error) {
      return handleError(error)
    }
  },
  async getEmployees() {
    try {
      const response = await api.get('/employees/')
      return handleResponse(response)
    } catch (error) {
      return handleError(error)
    }
  }
}
