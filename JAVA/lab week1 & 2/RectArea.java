class Rectangle
{
	int l, b;
	
	void set_var(int l, int b)
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

class RectArea
{
	public static void main(String args[])
	{
		Rectangle ob = new Rectangle();
		ob.set_var(5, 6);
		ob.get_var();
		ob.area();
		Rectangle ob1 = new Rectangle();
		ob1.set_var(10,20);
		ob1.get_var();
		ob1.area();
	}
}
		