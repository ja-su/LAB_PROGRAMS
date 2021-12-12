//week1 Q3.1
class Employee
{
	int emp_id;
	int sal;
	String desig;
	String name;

	void set_emp()
	{
		emp_id = 482733;
		name = "Michael";
		desig = "CEO";
		sal = 100000;
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
class EmployeeDetails1
{
	public static void main(String args[])
	{
		Employee object = new Employee();
		object.set_emp();
		object.get_emp();
	}
}



