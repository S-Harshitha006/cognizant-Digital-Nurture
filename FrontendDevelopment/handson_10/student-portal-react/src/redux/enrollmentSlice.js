import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { getAllCourses } from "../api/courseApi";

// Task 143 - Async Thunk
export const fetchAllCourses = createAsyncThunk(
  "courses/fetchAll",
  async (_, { rejectWithValue }) => {
    try {
      return await getAllCourses();
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

const enrollmentSlice = createSlice({
  name: "enrollment",

  initialState: {
    enrolledCourses: [],
    courses: [],
    loading: false,
    error: null,
  },

  reducers: {
    enrollCourse: (state, action) => {
      state.enrolledCourses.push(action.payload);
    },

    removeCourse: (state, action) => {
      state.enrolledCourses = state.enrolledCourses.filter(
        (course) => course.id !== action.payload
      );
    },
  },

  // Task 144 - Async Thunk Lifecycle
  extraReducers: (builder) => {
    builder
      .addCase(fetchAllCourses.pending, (state) => {
        state.loading = true;
        state.error = null;
      })

      .addCase(fetchAllCourses.fulfilled, (state, action) => {
        state.loading = false;
        state.courses = action.payload;
      })

      .addCase(fetchAllCourses.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  },
});

export const { enrollCourse, removeCourse } = enrollmentSlice.actions;

// Task 146 - Selectors
export const selectCourses = (state) => state.enrollment.courses;

export const selectCoursesLoading = (state) =>
  state.enrollment.loading;

export const selectCoursesError = (state) =>
  state.enrollment.error;

export default enrollmentSlice.reducer;