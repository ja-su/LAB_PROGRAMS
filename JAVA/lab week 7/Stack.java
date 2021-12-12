class StackDemo
{
	int stack[],top = -1,n;
	void set_data(int size)
	{
		stack = new int[size];
		n = size;
	}
	void push(int item)
	{
		try
		{
			if(top <= n)	
			{
				top += 1;
				stack[top] = item;
			}
		}
		catch(ArrayIndexOutOfBoundsException e)
		{
			System.out.println("Stack Overflow " );
		}
	}    
	void pop()
	{
		try
		{
				int i;
				i = stack[top--];
				System.out.println("Element popped: "+i);
		}
		catch(ArrayIndexOutOfBoundsException e)
		{
			System.out.println("Stack Underflow ");
		}
	}
	void stack_disp(){
	try{
	System.out.print("\n stack:");
	for(int i=0;i<=top;i++)
		System.out.print(" "+stack[i]);
	}
	catch(ArrayIndexOutOfBoundsException e){
		System.out.println("Exception");
	}
}
}

class Stack
{
	public static void main(String args[])
	{
		StackDemo ob = new StackDemo();
		
			ob.set_data(4);
			ob.push(1);
			ob.push(2);
			ob.push(3);
			//ob.push(4);
			//ob.push(5);
			ob.stack_disp();
			ob.pop();
			ob.pop();
			ob.pop();
			ob.pop(); 
				
			
		
	}
}