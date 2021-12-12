class Static
{
	static void sq(int a)
	{
		int sq = a * a;
		System.out.println("Square is: " + sq);
	}
	static void cube(int b)
	{
		int cube = b * b * b;
		System.out.println("Cube is: " + cube);
	}
	public static void main(String args[])
	{
		String a = args[0];
		int x = Integer.parseInt(a);
		String b = args[1];
		int y = Integer.parseInt(b);
		sq(x);
		cube(y);
	}
}