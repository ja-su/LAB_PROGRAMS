class Rectangle
{
	int l, b;
	Rectangle()
	{
		l = 5;
		b = 6;
		System.out.println("Area is: " + l*b);
	}
	Rectangle(int m)
	{
		l = m;
		b = m;
		System.out.println("Area is: " + l*b);
	}
	Rectangle(int p, int q)
	{
		l = p;
		b = q;
		System.out.println("Area is: " + l*b);
	}
}

class OverloadArea
{
	public static void main(String args[])
	{
		Rectangle ob1 = new Rectangle();
		Rectangle ob2 = new Rectangle(5);
		Rectangle ob3 = new Rectangle(10,20);
	}
}