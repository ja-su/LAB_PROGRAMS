class Person
{
	String name, gender, dob;
	int age;
	Person(String a, int b, String c, String d)
	{
		name = a;
		age = b;
		gender = c;
		dob = d;
	}
	void display()
	{
		System.out.println("----- EMPLOYEE DETAILS -----");
		System.out.println("Name: "+name);
		System.out.println("Age: "+age);
		System.out.println("Gender: "+gender);
		System.out.println("DOB: "+dob);
	}
		
}

class AssistantProfessor extends Person
{
	String department;
	int sal;
	AssistantProfessor(String a1,int a2,String a3,String a4,String a5,int a6)
	{
		super(a1,a2,a3,a4);
		department = a5;
		sal = a6;
	}
	void show_assprof()
	{
		System.out.println("Department: "+department);
		System.out.println("Salary "+sal);
	}
}
class AssociateProfessor extends Person
{
	String department;
	int sal;
	AssociateProfessor(String b1,int b2,String b3,String b4,String b5,int b6)
	{
		super(b1,b2,b3,b4);
		department = b5;
		sal = b6;
	}
	void show_assoprof()
	{
		System.out.println("Department: "+department);
		System.out.println("Salary: "+sal);
	}
}
class Professor extends Person
{		
	String department;
	int sal;
	Professor(String c1,int c2,String c3,String c4,String c5,int c6)
	{
		super(c1,c2,c3,c4);
		department = c5;
		sal = c6;
	}
	void show_prof()
	{
		System.out.println("Department: "+department);
		System.out.println("Salary: "+sal);
	}
}

class PersonDemo
{
	public static void main(String args[])
	{
		int c = Integer.parseInt(args[0]);
		if(c == 1)
		{
			AssistantProfessor ob1[] = new AssistantProfessor[5];
			ob1[0] = new AssistantProfessor("Tony",25,"M","1-01-1994","Mechanical Department",100000);
			ob1[1] = new AssistantProfessor("Mathew",24,"M","2-02-1995","IT Department",90000);
			ob1[2] = new AssistantProfessor("Carl",23,"M","3-03-1996","Civil Department",80000);
			ob1[3] = new AssistantProfessor("Katie",22,"F","4-04-1997","EEE Department",70000);
			ob1[4] = new AssistantProfessor("Chandler",21,"M","5-05-1998","EC Department",85000);
			for(int i = 0;i < 5;i ++)
			{
				ob1[i].display();
				ob1[i].show_assprof();
			}		
		}
		else if(c == 2)
		{
			AssociateProfessor ob2[] = new AssociateProfessor[5];
			ob2[0] = new AssociateProfessor("Joey",25,"M","1-01-1999","Mechanical Department",100000);
			ob2[1] = new AssociateProfessor("Rachael",24,"F","1-01-2000","IT Department",90000);
			ob2[2] = new AssociateProfessor("Mona",23,"F","1-01-2001","Civil Department",80000);
			ob2[3] = new AssociateProfessor("Monica",22,"F","1-01-2002","EEE Department",70000);
			ob2[4] = new AssociateProfessor("Geller",21,"M","1-01-2003","EC Department",75000);
			for(int i = 0;i < 5;i ++)
			{
				ob2[i].display();
				ob2[i].show_assoprof();
			}		
		}
		else
		{
			Professor ob3[] = new Professor[5];
			ob3[0] = new Professor("Dincy",25,"F","1-01-1999","Mechanical Department",100000);
			ob3[1] = new Professor("Mindy",24,"F","1-01-2000","IT Department",90000);
			ob3[2] = new Professor("Manny",23,"M","1-01-2001","Civil Department",800000);
			ob3[3] = new Professor("Greg",22,"M","1-01-2002","EEE Department",70000);
			ob3[4] = new Professor("John",21,"M","1-01-2003","EC Department",750000);
			for(int i = 0;i < 5;i ++)
			{
				ob3[i].display();
				ob3[i].show_prof();
			}		
		}
	}
}

