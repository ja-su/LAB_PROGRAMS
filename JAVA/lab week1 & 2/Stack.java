class StackOp
{
	int arr[] = new int[50];
	int top = -1;
	
	void push(int x)
	{
		System.out.println("Inserting : " + x);
		arr[++top] = x;
	}
	int pop()
	{
		return arr[top--];
		
	}
	void print()
	{
		for (int i = 0;i <= top;i++)
		{
			System.out.println(arr[i] +  "\n");
		}
	}
}

class Stack
{
	public static void main(String args[])
	{
		StackOp ob = new StackOp();
		ob.push(6);
		ob.push(5);
		ob.push(10);
		System.out.println("Printing Stack");
		ob.print();
		System.out.println("Popping a number");
		int y = ob.pop();
		System.out.println("Poppped element is: "+y);
		System.out.println("Printing Stack");
		ob.print();
		ob.push(15);
		System.out.println("Printing stack");
		ob.print();
		System.out.println("Popping a number");
		int z = ob.pop();
		System.out.println("Popped element is: " + z);
		System.out.println("Printing Stack");
		ob.print();
	}
}
		