class Rectangle
{
	int l, b;
	
	Rectangle(int l, int b)
	{
		this.l = l;
		this.b = b;
	}
	void get_var()
	{
		System.out.println("Length is: " + l);
		System.out.println("Breadth is: " + b);
	}
	void area()
	{
		int area = l * b;
		System.out.println("Area is: " + area);
	}
}

class RectArea2
{
	public static void main(String args[])
	{
		Rectangle ob = new Rectangle(10, 20);
		ob.get_var();
		ob.area();
		Rectangle ob1 = new Rectangle(100, 200);
		ob1.get_var();
		ob1.area();
	}
}
		