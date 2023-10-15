function getListStudentIds() {
  if (Array.isArray(students)) {
    return students.map((student) => student.id);
  }
}

export default getListStudentIds;
