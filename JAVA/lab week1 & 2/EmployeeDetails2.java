//week1 Q3.2
class Employee
{
	int emp_id;
	int sal;
	String desig;
	String name;

	void set_emp(int a, String b, String c, int d)
	{
		emp_id = a;
		name = b;
		desig = c;
		sal = d;
	}
	void get_emp()
	{
		System.out.println("Employee Details");
		System.out.println("Employee id: "+emp_id);
		System.out.println("Employee Name: "+name);
		System.out.println("Employee Designation: "+desig);
		System.out.println("Employee Salary: "+sal);
	}
}
class EmployeeDetails2
{
	public static void main(String args[])
	{
		Employee object = new Employee();
		object.set_emp(129794,"Mike","CEO", 100000);
		object.get_emp();
		Employee object2 = new Employee();
		object2.set_emp(67899,"Tony","HR", 50000);
		object2.get_emp();
	}
}
