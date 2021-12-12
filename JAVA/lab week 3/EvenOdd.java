class Outer
{
	int x;
	Outer(int a)
	{
		x = a;
	}
	void check()
	{
		Inner ob = new Inner();
		ob.evenodd();
	}
	class Inner
	{
		void evenodd()
		{
			if(x % 2 == 0)
				System.out.println("The number is a even number");
			else
				System.out.println("The number is an odd number");
		}
	}
}

		
		
		
class EvenOdd
{
	public static void main(String args[])
	{
		
		int m = Integer.parseInt(args[0]);
		Outer ob1 = new Outer(m);
		ob1.check();
	}
}
