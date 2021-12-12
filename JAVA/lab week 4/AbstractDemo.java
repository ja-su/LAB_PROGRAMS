abstract class Shape
{
	int a, b;
	abstract void printArea();

}

class Rectangle extends Shape
{
	Rectangle(int x, int y)
	{
		a = x;
		b = y;
	}
	void printArea()
	{
		double area = a * b;
		System.out.println("Area of the Rectangle is: " + area);
	}
}
class Triangle extends Shape
{
	Triangle(int m,int n)
	{
		a = m;
		b = n;
	}
	void printArea()
	{
		double area = 0.5 * a * b;
		System.out.println("Area of the Triangle is: " + area);
	}
}
class Circle extends Shape
{	
	Circle(int p)
	{
		a = p;
	}
	void printArea()
	{
		double area = 3.14 * a * a;
		System.out.println("Area of the Circle is: " + area);
	}
}

class AbstractDemo
{
	public static void main(String args[])
	{
		int x = Integer.parseInt(args[0]);
		int y = Integer.parseInt(args[1]);
		Rectangle ob1 = new Rectangle(x,y);
		Triangle ob2 = new Triangle(x,y);
		Circle ob3 = new Circle(x);
		ob1.printArea();
		ob2.printArea();
		ob3.printArea();
	}
}