//fibonacci
class Fibonacci
{
	public static void main(String args[])
	{
		int n1 = 0, n2 = 1;
		String a = args[0];
		int x = Integer.parseInt(a);
		System.out.println(n1);
		System.out.println(n2);
		for(int i = 2; i < x; i++)
		{
			int n3 = n1 + n2;
			System.out.println(n3);
			n1 = n2;
			n2 = n3;
		}
	}
}