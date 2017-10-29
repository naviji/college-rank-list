

drop table dept_course;
drop table student_marks;
drop table dept_student;
drop table course;
drop table department;
drop table college;


CREATE TABLE college (
    college_id  serial PRIMARY KEY,
    college_name   varchar(80) NOT NULL
);

CREATE TABLE department (
     dept_id   serial PRIMARY KEY,
     dept_name   varchar(50) NOT NULl,
     colleg_id  serial references college(college_id)
);

CREATE TABLE course (
    course_id serial PRIMARY KEY,
    course_code varchar(20) UNIQUE
);

CREATE TABLE dept_student (
    register_id varchar(15) PRIMARY KEY,
    dept_id serial references department(dept_id)
);

CREATE TABLE student_marks (
    mark_id serial PRIMARY KEY,
    register_id varchar(15) references dept_student(register_id),
    course_id serial references course(course_id)
);

CREATE TABLE dept_course (
    dc_id serial PRIMARY KEY,
    dept_id serial references department(dept_id),
    course_id serial references course(course_id)
);
        