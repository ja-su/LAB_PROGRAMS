import java.util.Random;

class Square extends Thread
{
	int x;
	Square(int n)
	{
		x = n;
	}
	public void run()
	{
		int sqr = x * x;
		System.out.println("Square of " + x + " is: " + sqr);
	}
}

class Cube extends Thread
{
	int x;
	Cube(int n)
	{
		x = n;
	}
	public void run()
	{
		int cube = x * x * x;
		System.out.println("Cube of " + x + " is: " + cube);
	}
}

class Number extends Thread
{
	public synchronized void run()
	{
		Random obj = new Random();
		for(int i = 0;i < 5;i ++)
		{
			int a = obj.nextInt(100);
			System.out.println("Random number is : " + a);
			if(a % 2 == 0)
			{
				Square ob1 = new Square(a);
				ob1.start();
			}
			else
			{
				Cube ob2 = new Cube(a);
				ob2.start();
			}
			try
			{
				Thread.sleep(1000);
			}
			catch(InterruptedException e)
			{
				System.out.println("Interrupted e " + e);
			}
		}
	}
}
class RandomNumber
{
	public static void main(String args[])
	{
		Number p = new Number();
		p.start();
	}
}

			