class FibonacciOp
{
	int fib(int num)
	{
		if(num <= 1)
		{
			return num;
		}
			return fib(num -1) + fib(num - 2);
	}
}

class FibonacciRecursive
{
	public static void main(String args[])
	{
		int n3, i;
		String a = args[0];
		int x = Integer.parseInt(a);
		
		FibonacciOp ob = new FibonacciOp();
		for(i=0;i<x;i++){
		System.out.println(ob.fib(i));
		}
	}
}