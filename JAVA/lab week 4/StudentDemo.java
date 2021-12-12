class Person
{
	String name;
	int age;
	String gender;
	Person(String a, int b, String c)
	{
		name = a;
		age = b;
		gender = c;
	}
}
class Student extends Person
{
	double mark1, mark2, mark3, total_marks;
	String grade;
	Student(String a1, int a2, String a3, double a4, double a5, double a6)
	{
		super(a1,a2,a3);
		mark1 = a4;
		mark2 = a5;
		mark3 = a6;
	}
	double total_marks()
	{
		total_marks = mark1 + mark2 + mark3;
		return total_marks;
	}
	void grade()
	{
		double marks = (total_marks / 300) * 100;
		if(marks >= 90)
			System.out.println("Grade: A");
		else if(marks >= 80 && marks < 90)
			System.out.println("Grade: B");
		else if(marks >= 70 && marks < 80)
			System.out.println("Grade: C");
		else if(marks >= 60 && marks < 70)
			System.out.println("Grade: D");
		else if(marks >= 50 && marks < 60)
			System.out.println("Grade: E");
		else
			System.out.println("Fail");
	}
	void display()
	{
		System.out.println("Name: "+name);
		System.out.println("Age: "+age);
		System.out.println("Gender: "+gender);
		double z = total_marks();
		System.out.println("Total Marks "+total_marks);
		grade();
	}
}
class StudentDemo
{
	public static void main(String args[])
	{
		String a = args[0];
		int x = Integer.parseInt(args[1]);
		String b = args[2];
		int m1 = Integer.parseInt(args[3]);
		int m2 = Integer.parseInt(args[4]);
		int m3 = Integer.parseInt(args[5]);
		Student ob = new Student(a,x,b,m1,m2,m3);
		
		ob.display();
		
	}
}
