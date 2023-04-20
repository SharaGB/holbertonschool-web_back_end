const fs = require('fs');

const countStudents = (aPath) => new Promise((resolve, reject) => {
  fs.readFile(aPath, 'utf8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const response = [];
    let msg;

    let lines = data.trim().split('\n');
    lines = lines.slice(1, lines.length);

    msg = `Number of students: ${lines.length}`;
    console.log(msg);
    response.push(msg);

    const courses = {};
    for (const row of lines) {
      const student = row.split(',');
      if (!courses[student[3]]) courses[student[3]] = [];
      courses[student[3]].push(student[0]);
    }
    for (const course in courses) {
      if (course) {
        msg = `Number of students in ${course}: ${
          courses[course].length
        }. List: ${courses[course].join(', ')}`;

        console.log(msg);
        response.push(msg);
      }
    }
    resolve(response);
  });
});

module.exports = countStudents;
