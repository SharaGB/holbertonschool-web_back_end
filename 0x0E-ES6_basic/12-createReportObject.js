export default function createReportObject(employeesList) {
  return ({
    allEmployees: employeesList,
    getNumberOfDepartments: (all) => Object.keys(all).length,
  });
}
