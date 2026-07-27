import axios from "axios";

const apiClient = axios.create({
  baseURL: "https://jsonplaceholder.typicode.com",
  timeout: 5000,
  headers: {
    "Content-Type": "application/json",
  },
});

// Task 141 - Request Interceptor
apiClient.interceptors.request.use(
  (config) => {
    config.headers.Authorization = "Bearer mock-token-123456";
    return config;
  },
  (error) => Promise.reject(error)
);

// Task 140 - Response Interceptor
apiClient.interceptors.response.use(
  (response) => {
    return response.data;
  },
  (error) => {
    throw {
      message:
        error.response?.data?.message ||
        error.message ||
        "Something went wrong",
      statusCode: error.response?.status || 500,
    };
  }
);

export default apiClient;