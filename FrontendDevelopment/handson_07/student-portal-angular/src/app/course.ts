import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CourseService {

  constructor() { }

  getCourses() {
    return [
      {
        id: 1,
        title: 'Angular Fundamentals',
        instructor: 'John Smith',
        duration: '6 Weeks'
      },
      {
        id: 2,
        title: 'React Development',
        instructor: 'Sarah Johnson',
        duration: '8 Weeks'
      },
      {
        id: 3,
        title: 'Python Programming',
        instructor: 'David Wilson',
        duration: '5 Weeks'
      },
      {
        id: 4,
        title: 'Java Full Stack',
        instructor: 'Michael Brown',
        duration: '10 Weeks'
      }
    ];
  }
}