/*
MongoDB - Document Modelling, CRUD & Aggregation
*/

// Task 1


// Switch to database
use college_nosql

// Create collection
db.createCollection("feedback")

// Insert feedback documents
db.feedback.insertMany([
{
    student_id: 1,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 5,
    comments: "Excellent teaching. Would recommend.",
    tags: ["challenging","well-structured","good-examples"],
    submitted_at: ISODate("2022-11-30T10:15:00Z"),
    attachments: [
        {
            filename: "notes.pdf",
            size_kb: 240
        }
    ]
},
{
    student_id: 2,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 4,
    comments: "Very informative course.",
    tags: ["challenging","good-examples"],
    submitted_at: ISODate("2022-11-28T09:00:00Z"),
    attachments: [
        {
            filename: "assignment.pdf",
            size_kb: 120
        }
    ]
},
{
    student_id: 3,
    course_code: "CS101",
    semester: "2022-EVEN",
    rating: 2,
    comments: "Needs more practical sessions.",
    tags: ["challenging","average"],
    submitted_at: ISODate("2022-12-01T14:20:00Z"),
    attachments: [
        {
            filename: "feedback.txt",
            size_kb: 15
        }
    ]
},
{
    student_id: 4,
    course_code: "CS102",
    semester: "2022-ODD",
    rating: 5,
    comments: "Loved the lab exercises.",
    tags: ["practical","excellent"],
    submitted_at: ISODate("2022-11-29T11:45:00Z"),
    attachments: [
        {
            filename: "lab.pdf",
            size_kb: 180
        }
    ]
},
{
    student_id: 5,
    course_code: "CS102",
    semester: "2022-ODD",
    rating: 3,
    comments: "Good overall.",
    tags: ["interesting","clear"],
    submitted_at: ISODate("2022-11-27T13:10:00Z"),
    attachments: [
        {
            filename: "course.pdf",
            size_kb: 200
        }
    ]
},
{
    student_id: 6,
    course_code: "CS103",
    semester: "2022-ODD",
    rating: 1,
    comments: "Very difficult.",
    tags: ["hard","challenging"],
    submitted_at: ISODate("2022-11-26T08:30:00Z")
},
{
    student_id: 7,
    course_code: "CS104",
    semester: "2022-EVEN",
    rating: 3,
    comments: "Average experience.",
    tags: ["interesting"],
    submitted_at: ISODate("2022-11-24T09:00:00Z"),
    attachments: [
        {
            filename: "report.pdf",
            size_kb: 90
        }
    ]
},
{
    student_id: 8,
    course_code: "CS105",
    semester: "2021-EVEN",
    rating: 2,
    comments: "Outdated syllabus.",
    tags: ["theory","challenging"],
    submitted_at: ISODate("2021-12-10T09:30:00Z"),
    attachments: [
        {
            filename: "old.pdf",
            size_kb: 150
        }
    ]
},
{
    student_id: 9,
    course_code: "CS106",
    semester: "2022-ODD",
    rating: 5,
    comments: "Excellent content.",
    tags: ["good-examples","supportive"],
    submitted_at: ISODate("2022-11-18T12:45:00Z"),
    attachments: [
        {
            filename: "guide.pdf",
            size_kb: 210
        }
    ]
},
{
    student_id: 10,
    course_code: "CS107",
    semester: "2022-ODD",
    rating: 4,
    comments: "Nice explanations.",
    tags: ["challenging","well-structured"],
    submitted_at: ISODate("2022-11-16T16:20:00Z"),
    attachments: [
        {
            filename: "notes2.pdf",
            size_kb: 160
        }
    ]
}
])

// Verify document count
db.feedback.countDocuments()


// Task 2 - CRUD Operations

// Find rating 5
db.feedback.find({
    rating: 5
})

// Find CS101 with challenging tag
db.feedback.find({
    course_code: "CS101",
    tags: "challenging"
})

// Projection
db.feedback.find(
{},
{
    student_id:1,
    course_code:1,
    rating:1,
    _id:0
}
)

// Update low ratings
db.feedback.updateMany(
{
    rating:{
        $lt:3
    }
},
{
    $set:{
        needs_review:true
    }
}
)

// Push reviewed tag
db.feedback.updateMany(
{
    needs_review:true
},
{
    $push:{
        tags:"reviewed"
    }
}
)

// Delete old semester
db.feedback.deleteMany({
    semester:"2021-EVEN"
})

// Task 3 - Aggregation


// Average rating by course
db.feedback.aggregate([
{
    $match:{
        semester:"2022-ODD"
    }
},
{
    $group:{
        _id:"$course_code",
        avg_rating:{
            $avg:"$rating"
        },
        total_feedback:{
            $sum:1
        }
    }
},
{
    $sort:{
        avg_rating:-1
    }
}
])

// Average rating with projection
db.feedback.aggregate([
{
    $match:{
        semester:"2022-ODD"
    }
},
{
    $group:{
        _id:"$course_code",
        avg_rating:{
            $avg:"$rating"
        },
        total_feedback:{
            $sum:1
        }
    }
},
{
    $sort:{
        avg_rating:-1
    }
},
{
    $project:{
        _id:0,
        course_code:"$_id",
        average_rating:{
            $round:["$avg_rating",1]
        },
        total_feedback:1
    }
}
])

// Tag frequency
db.feedback.aggregate([
{
    $unwind:"$tags"
},
{
    $group:{
        _id:"$tags",
        count:{
            $sum:1
        }
    }
},
{
    $sort:{
        count:-1
    }
}
])


// Task 4 - Index

// Create Index
db.feedback.createIndex({
    course_code:1
})

// Verify Index
db.feedback.find({
    course_code:"CS101"
}).explain("executionStats")

/*
During execution, MongoDB returned:

MongoServerError: OutOfDiskSpace

Hence the index could not be created,
and explain() displayed COLLSCAN instead
of IXSCAN.
*/