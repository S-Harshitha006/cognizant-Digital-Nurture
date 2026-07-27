import apiClient from "./apiClient";

// Task 139 - Get all courses
export const getAllCourses = async () => {
  return await apiClient.get("/posts");
};

// Task 139 - Get course by ID
export const getCourseById = async (id) => {
  return await apiClient.get(`/posts/${id}`);
};

// Task 139 - Enroll student (Mock API)
export const enrollStudent = async (studentId, courseId) => {
  return await apiClient.post("/posts", {
    studentId,
    courseId,
    status: "Enrolled",
  });
};