class DivisionZero
{
	public static void main(String args[])
	{
		int a, b, c;
		a = Integer.parseInt(args[0]);
		b = Integer.parseInt(args[1]);
		
		try
		{
			c = a / b;
			System.out.println("a / b= "+c);
		}
		catch(ArithmeticException x)
		{
			System.out.println("Cannot divide by zero "+x);
		}
	}
}
		