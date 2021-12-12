//method overloading

class Display
{	
	void disp(int x)
	{
		System.out.println("Displaying integer: " + x);
	}
	void disp(String y)
	{
		System.out.println("Displaying string: " + y);
	}
	void disp(float z)
	{
		System.out.println("Displaying float: " + z);
	}
}

class StrIntFloatOverload
{
	public static void main(String args[])
	{
		String a = args[0];
		int x1 = Integer.parseInt(a);
		String b = args[1];
		String c = args[2];
		float z = Float.parseFloat(c);
		
		Display ob = new Display();
		ob.disp(x1);
		ob.disp(b);
		ob.disp(z);
	}
}