import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Course {
    private String id;
    private String name;
    private String instructor;

    public Course(String id, String name, String instructor) {
        this.id = id;
        this.name = name;
        this.instructor = instructor;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getInstructor() {
        return instructor;
    }

    @Override
    public String toString() {
        return "Course{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                ", instructor='" + instructor + '\'' +
                '}';
    }
}

class Student {
    private String id;
    private String name;
    private List<Course> enrolledCourses;

    public Student(String id, String name) {
        this.id = id;
        this.name = name;
        this.enrolledCourses = new ArrayList<>();
    }

    public void enrollCourse(Course course) {
        enrolledCourses.add(course);
    }

    public List<Course> getEnrolledCourses() {
        return enrolledCourses;
    }

    @Override
    public String toString() {
        return "Student{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                ", enrolledCourses=" + enrolledCourses +
                '}';
    }
}

class LMS {
    private List<Course> courses;
    private List<Student> students;

    public LMS() {
        courses = new ArrayList<>();
        students = new ArrayList<>();
    }

    public void addCourse(Course course) {
        courses.add(course);
    }

    public void addStudent(Student student) {
        students.add(student);
    }

    public void enrollStudentInCourse(Student student, Course course) {
        student.enrollCourse(course);
    }

    public void displayCourses() {
        System.out.println("Available Courses:");
        for (Course course : courses) {
            System.out.println(course);
        }
    }

    public void displayStudents() {
        System.out.println("Enrolled Students:");
        for (Student student : students) {
            System.out.println(student);
        }
    }
}

public class LMSApp {
    public static void main(String[] args) {
        LMS lms = new LMS();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n1. Add Course");
            System.out.println("2. Add Student");
            System.out.println("3. Enroll Student in Course");
            System.out.println("4. Display Courses");
            System.out.println("5. Display Students");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter course ID: ");
                    String courseId = scanner.nextLine();
                    System.out.print("Enter course name: ");
                    String courseName = scanner.nextLine();
                    System.out.print("Enter instructor name: ");
                    String instructor = scanner.nextLine();
                    lms.addCourse(new Course(courseId, courseName, instructor));
                    break;
                case 2:
                    System.out.print("Enter student ID: ");
                    String studentId = scanner.nextLine();
                    System.out.print("Enter student name: ");
                    String studentName = scanner.nextLine();
                    lms.addStudent(new Student(studentId, studentName));
                    break;
                case 3:
                    // Implement enrollment logic
                    break;
                case 4:
                    lms.displayCourses();
                    break;
                case 5:
                    lms.displayStudents();
                    break;
                case 6:
                    System.out.println("Exiting LMS. Goodbye!");
                    System.exit(0);
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}