const fs = require('fs');

const countStudents = (aPath) => {
  try {
    let data = fs.readFileSync(aPath, 'utf8').toString().split('\n');
    data = data.slice(1, data.length - 1);
    console.log(`Number of students: ${data.length}`);
    const courses = {};
    for (const row of data) {
      const student = row.split(',');
      if (!courses[student[3]]) courses[student[3]] = [];
      courses[student[3]].push(student[0]);
    }
    for (const course in courses) {
      if (course) {
        console.log(
          `Number of students in ${course}: ${
            courses[course].length
          }. List: ${courses[course].join(', ')}`,
        );
      }
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
